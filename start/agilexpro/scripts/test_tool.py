#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

TRIGGER_IN = "/next_point_trigger"
TRIGGER_OUT = "/waypoint_reached"

def reach_callback(msg):
    if msg.data:
        rospy.loginfo("【模拟外设】收到机器人到位，开始作业")

if __name__ == "__main__":
    rospy.init_node("sim_external_device")
    pub = rospy.Publisher(TRIGGER_IN,Bool,queue_size=5)
    rospy.Subscriber(TRIGGER_OUT,Bool,reach_callback)
    rospy.loginfo("模拟外设启动：输入 done = 作业完成；exit=退出")
    while not rospy.is_shutdown():
        cmd = input(">")
        if cmd == "done":
            pub.publish(Bool(True))
            rospy.loginfo("发送完工指令，机器人继续走点")
        elif cmd == "exit":
            break

