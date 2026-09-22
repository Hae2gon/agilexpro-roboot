#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import LaserScan
import os

# ========== 配置 ==========
SAVE_PATH = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/txt/scan_obst.txt"
# 过滤无效距离，避免噪声
MIN_RANGE = 0.1
# ===========================

def scan_cb(msg):
    points = []
    angle = msg.angle_min

    for r in msg.ranges:
        # 过滤超限/无效测距
        if MIN_RANGE < r < msg.range_max:
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append([x, y])
        angle += msg.angle_increment

    # 保存文件
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        for x, y in points:
            f.write(f"{x:.3f} {y:.3f}\n")

    rospy.loginfo(f"激光点提取完成，共 {len(points)} 个点，已保存至 {SAVE_PATH}")
    rospy.signal_shutdown("提取完毕，退出节点")

def main():
    rospy.init_node("extract_scan_obst_node", anonymous=True)
    rospy.Subscriber("/scan", LaserScan, scan_cb)
    rospy.loginfo("等待激光数据... 启动激光/建图/导航后会自动采集一帧数据")
    rospy.spin()

if __name__ == "__main__":
    main()

