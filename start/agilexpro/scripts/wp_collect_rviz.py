#!/usr/bin/env python3
import rospy
import yaml
import threading
import os
import tf
from subprocess import call
from geometry_msgs.msg import PoseWithCovarianceStamped
from visualization_msgs.msg import MarkerArray, Marker

WP_YAML = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/waypoints_0603.yaml"
SCRIPT_PATH = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/scripts/map_save_label.py"
FRAME_ID = "world"
MARK_TOPIC = "/collect_way_marker"
wp_list = []
marker_pub = None
marker_arr = MarkerArray()

def pose_callback(msg):
    global wp_list, marker_arr
    # 提取坐标
    x = round(msg.pose.pose.position.x, 3)
    y = round(msg.pose.pose.position.y, 3)
    # 四元数转欧拉角，获取航向角yaw
    quat = [
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w
    ]
    _, _, yaw = tf.transformations.euler_from_quaternion(quat)
    yaw = round(yaw, 3)

    index = len(wp_list) + 1
    # 存入点位，包含x/y/yaw完整朝向
    wp_list.append({
        "id": index,
        "name": f"点位{index}",
        "x": x,
        "y": y,
        "yaw": yaw
    })
    rospy.loginfo(f"采集点位{index}: X{x}, Y{y}, Yaw{yaw}")

    mk = Marker()
    mk.header.frame_id = FRAME_ID
    mk.header.stamp = rospy.Time.now()
    mk.ns = "collect_wp"
    mk.id = index
    mk.type = Marker.SPHERE
    mk.action = Marker.ADD
    mk.pose = msg.pose.pose
    mk.scale.x = 0.3
    mk.scale.y = 0.3
    mk.scale.z = 0.1
    mk.color.r = 0
    mk.color.g = 1
    mk.color.b = 1
    mk.color.a = 0.7
    marker_arr.markers.append(mk)
    marker_pub.publish(marker_arr)

def save_yaml():
    save_data = {"waypoints": wp_list}
    with open(WP_YAML, "w", encoding="utf-8") as f:
        yaml.dump(save_data, f, sort_keys=False, default_flow_style=False)
    rospy.loginfo(f"点位yaml保存完毕，合计{len(wp_list)}个（含朝向yaw）")
    # 自动生成标注地图
    rospy.loginfo("自动开始生成带点位标注地图...")
    call(["python3", SCRIPT_PATH])
    rospy.loginfo("标注地图 map_mark.png 生成完成")

def input_loop():
    while not rospy.is_shutdown():
        cmd = input("输入save保存点位：")
        if cmd == "save":
            save_yaml()

if __name__ == "__main__":
    rospy.init_node("waypoint_collect_node")
    marker_pub = rospy.Publisher(MARK_TOPIC, MarkerArray, queue_size=10)
    rospy.Subscriber("/initialpose", PoseWithCovarianceStamped, pose_callback)
    threading.Thread(target=input_loop, daemon=True).start()
    rospy.loginfo("启动采集：RViz使用2D Pose Estimate左键打点+拖拽设置朝向")
    rospy.spin()

