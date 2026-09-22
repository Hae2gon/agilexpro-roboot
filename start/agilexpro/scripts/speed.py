#!/usr/bin/env python3
import rospy
import math
from nav_msgs.msg import Odometry
from collections import deque

# 轮距 根据你底盘实际修改
track_width = 0.45
# 采样缓存长度
buf_len = 10

# 历史数据缓存
vel_buf = deque(maxlen=buf_len)
time_buf = deque(maxlen=buf_len)

def odom_callback(msg):
    now = rospy.Time.now().to_sec()
    vx = msg.twist.twist.linear.x
    wz = msg.twist.twist.angular.z

    # 差速解算左右履带线速度
    v_left  = vx - (wz * track_width / 2.0)
    v_right = vx + (wz * track_width / 2.0)

    # 数值微分估算加速度
    acc = 0.0
    if len(vel_buf) >= 2:
        delta_t = now - time_buf[-1]
        if delta_t > 0:
            acc = (vx - vel_buf[-1]) / delta_t

    vel_buf.append(vx)
    time_buf.append(now)

    # 控制台格式化打印
    print("="*50)
    print(f"全局线速度 Vx:    {vx:.3f}  m/s")
    print(f"全局角速度 Wz:    {wz:.3f}  rad/s")
    print(f"估算加速度 Acc:   {acc:.3f}  m/s²")
    print("-"*30)
    print(f"左履带速度 V_L:    {v_left:.3f}  m/s")
    print(f"右履带速度 V_R:    {v_right:.3f}  m/s")
    print("="*50+"\n")

if __name__ == "__main__":
    rospy.init_node("chassis_crawl_speed_monitor")
    rospy.Subscriber("/odom", Odometry, odom_callback, queue_size=10)
    rospy.loginfo("履带速度&加速度监视器已启动")
    rospy.spin()

