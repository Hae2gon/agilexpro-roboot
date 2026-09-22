#!/usr/bin/env python3
import rospy
import yaml
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Bool
import tf
import sys

# 配置不要改动
WP_YAML = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/waypoints_0603.yaml"
# 外设→机器人：作业完成，触发下一点
TRIGGER_IN = "/next_point_trigger"
# 机器人→外设：到达点位
TRIGGER_OUT = "/waypoint_reached"

class StepNav:
    def __init__(self):
        rospy.init_node("waypoint_nav_node")
        # 加载路点
        with open(WP_YAML,"r") as f:
            data = yaml.safe_load(f)
        self.wplist = data["waypoints"]
        self.cur_idx = 0

        # move_base客户端
        self.client = actionlib.SimpleActionClient("move_base",MoveBaseAction)
        rospy.loginfo("等待move_base...")
        self.client.wait_for_server()

        # 订阅外部触发
        rospy.Subscriber(TRIGGER_IN,Bool,self.in_cb)
        # 发布到达信号
        self.pub_reach = rospy.Publisher(TRIGGER_OUT,Bool,queue_size=5)

        rospy.loginfo("导航就绪，自动前往第一个点位")
        self.goto_point()

    def goto_point(self):
        if self.cur_idx >= len(self.wplist):
            rospy.loginfo("所有路径全部跑完！")
            return
        wp = self.wplist[self.cur_idx]
        x = wp["x"]
        y = wp["y"]
        yaw = wp.get("yaw",0.0)
        name = wp["name"]
        rospy.loginfo(f"前往 {name} X:{x:.2f} Y:{y:.2f}")

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "world" # 修正坐标系，解决你报错
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        q = tf.transformations.quaternion_from_euler(0,0,yaw)
        goal.target_pose.pose.orientation = Quaternion(*q)

        self.client.send_goal(goal)
        res = self.client.wait_for_result(rospy.Duration(40))
        state = self.client.get_state()

        if state == actionlib.GoalStatus.SUCCEEDED:
            rospy.loginfo(f"已到达【{name}】，向外发送到位信号")
            self.pub_reach.publish(Bool(True))
            self.cur_idx += 1
            rospy.loginfo("等待外设作业完成信号...")
        else:
            rospy.logerr(f"{name}导航失败，等待再次触发")

    # 收到外部完工信号
    def in_cb(self,msg):
        if msg.data is True:
            rospy.loginfo("收到完工信号，前往下一途经点")
            self.goto_point()

if __name__ == "__main__":
    try:
        StepNav()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

