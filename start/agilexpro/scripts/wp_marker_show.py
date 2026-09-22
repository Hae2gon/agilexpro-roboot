#!/usr/bin/env python3
import rospy
import yaml
from visualization_msgs.msg import MarkerArray, Marker

WP_YAML = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/waypoints_0603.yaml"
MARK_TOPIC = "/waypoints_markers"
FRAME = "world"

def load_waypoints():
    with open(WP_YAML, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["waypoints"]

if __name__ == "__main__":
    rospy.init_node("static_way_marker_node")
    pub = rospy.Publisher(MARK_TOPIC, MarkerArray, queue_size=5)
    wp_list = load_waypoints()
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        mar = MarkerArray()
        for idx, wp in enumerate(wp_list):
            # 圆点标记
            mk = Marker()
            mk.header.frame_id = FRAME
            mk.header.stamp = rospy.Time.now()
            mk.ns = "way_point_mark"
            mk.id = idx
            mk.type = Marker.SPHERE
            mk.action = Marker.ADD
            mk.pose.position.x = wp["x"]
            mk.pose.position.y = wp["y"]
            mk.pose.orientation.w = 1.0
            mk.scale.x = 0.3
            mk.scale.y = 0.3
            mk.scale.z = 0.15
            if idx == 0:
                mk.color.r = 0; mk.color.g = 1; mk.color.b = 0; mk.color.a = 0.8
            elif idx == len(wp_list)-1:
                mk.color.r = 1; mk.color.g = 0; mk.color.b = 0; mk.color.a = 0.8
            else:
                mk.color.r = 1; mk.color.g = 0.65; mk.color.b = 0; mk.color.a = 0.8
            mar.markers.append(mk)
            # 文字标注点位名称坐标
            text_mk = Marker()
            text_mk.header = mk.header
            text_mk.ns = "way_text"
            text_mk.id = idx + 100
            text_mk.type = Marker.TEXT_VIEW_FACING
            text_mk.action = Marker.ADD
            text_mk.pose.position.x = wp["x"]
            text_mk.pose.position.y = wp["y"]
            text_mk.pose.position.z = 0.2
            text_mk.scale.z = 0.2
            text_mk.color.r = 1; text_mk.color.g = 1; text_mk.color.b = 1; text_mk.color.a = 1
            text_mk.text = f"{wp['name']}"
            mar.markers.append(text_mk)
        pub.publish(mar)
        rate.sleep()

