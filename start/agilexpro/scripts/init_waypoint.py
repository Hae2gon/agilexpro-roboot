#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped

def goto_init_point():
    rospy.init_node('goto_init_point', anonymous=True)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(2)  

    # 初始化目标点
    goal = PoseStamped()
    goal.header.frame_id = "world"
    goal.header.stamp = rospy.Time.now()

    # 位置
    goal.pose.position.x = 4.72
    goal.pose.position.y = 0.08
    goal.pose.position.z = 0.0

    # 姿态
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.58
    goal.pose.orientation.w = 0.81

    pub.publish(goal)
    rospy.loginfo("已发布目标，自动前往初始化点")
    rospy.spin()

if __name__ == '__main__':
    try:
        goto_init_point()
    except rospy.ROSInterruptException:
        pass

