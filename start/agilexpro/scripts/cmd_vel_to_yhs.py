#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math
from geometry_msgs.msg import Twist
from yhs_can_msgs.msg import ctrl_cmd

class CmdVelToYhsConverter:
    def __init__(self):
        rospy.init_node('cmd_vel_to_yhs_converter', anonymous=True)

        # 1. 订阅 move_base
        rospy.Subscriber("/cmd_vel", Twist, self.cmd_vel_callback)

        # 2. 发布到底盘
        self.yhs_pub = rospy.Publisher("/ctrl_cmd", ctrl_cmd, queue_size=10)

        # 状态变量
        self.target_linear = 0.0
        self.target_angular = 0.0
        self.last_cmd_time = rospy.Time.now()

        # 3. 设置高频定时器 (100Hz = 10ms)
        # 必须满足底盘的 100Hz 要求 [cite: 20]
        self.rate = rospy.Rate(100) 

        rospy.loginfo("YHS Converter Running: 100Hz with Timeout Protection")
        
        self.control_loop()

    def cmd_vel_callback(self, msg):
        self.target_linear = msg.linear.x
        # 弧度转角度: degree = rad * (180/pi) [cite: 27]
        self.target_angular = msg.angular.z * (180.0 / math.pi)
        # 更新最后接收命令的时间
        self.last_cmd_time = rospy.Time.now()

    def control_loop(self):
        while not rospy.is_shutdown():
            yhs_msg = ctrl_cmd()

            # --- 超时保护逻辑 ---
            # 如果超过 0.2秒 没收到 move_base 的指令，说明导航可能暂停了或卡顿了
            # 此时强制发 0，防止车子因为执行旧指令而“抖动”
            if (rospy.Time.now() - self.last_cmd_time).to_sec() > 1.0:
                self.target_linear = 0.0
                self.target_angular = 0.0

            # --- 1. 设置档位 ---
            # 03: 运动学控制模式 (Kinematic control) [cite: 474]
            yhs_msg.ctrl_cmd_gear = 3 

            # --- 2. 赋值速度 ---
            yhs_msg.ctrl_cmd_linear = self.target_linear
            yhs_msg.ctrl_cmd_angular = self.target_angular

            # --- 3. 发布 ---
            self.yhs_pub.publish(yhs_msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        CmdVelToYhsConverter()
    except rospy.ROSInterruptException:
        pass
