#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import math
import os
import tf.transformations as tf_trans
from tf import TransformListener

# 存储文件夹
SAVE_ROOT = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/txt/scan_data/"
# 修改批次号区分多组采集
BATCH_NAME = "batch_04"
# 雷达有效测距过滤
MIN_RANGE = 0.1
MAX_RANGE = 10.0
# 目标全局坐标系
TARGET_FRAME = "world"

def create_dir():
    if not os.path.exists(SAVE_ROOT):
        os.makedirs(SAVE_ROOT)

class ScanWorldRecorder:
    def __init__(self):
        self.tf_listener = TransformListener()
        rospy.Subscriber("/scan", LaserScan, self.scan_callback, queue_size=1)
        rospy.loginfo(f"全局坐标雷达采集启动 | 当前批次：{BATCH_NAME}")
        rospy.spin()

    def scan_callback(self, msg):
        # 查询雷达帧 -> world 坐标变换
        try:
            trans, rot = self.tf_listener.lookupTransform(TARGET_FRAME, msg.header.frame_id, rospy.Time(0))
        except Exception as e:
            rospy.logwarn(f"TF变换获取失败，跳过当前帧：{str(e)}")
            return
        
        tx, ty, _ = trans
        _, _, yaw = tf_trans.euler_from_quaternion(rot)
        point_list = []
        angle = msg.angle_min

        # 遍历雷达所有测距点
        for r in msg.ranges:
            if MIN_RANGE < r < MAX_RANGE:
                # 雷达本体局部坐标
                lx = r * math.cos(angle)
                ly = r * math.sin(angle)
                # 转换到world全局坐标
                wx = tx + lx * math.cos(yaw) - ly * math.sin(yaw)
                wy = ty + lx * math.sin(yaw) + ly * math.cos(yaw)
                point_list.append(f"{wx:.4f},{wy:.4f}")
            angle += msg.angle_increment
        
        # 追加写入对应批次文件
        file_path = os.path.join(SAVE_ROOT, f"{BATCH_NAME}.txt")
        frame_time = rospy.Time.now().to_sec()
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"# FrameTime={frame_time:.2f}, PointCount={len(point_list)}\n")
            f.write("\n".join(point_list))
            f.write("\n\n")
        rospy.loginfo(f"写入一帧，有效障碍物点数：{len(point_list)}")

if __name__ == "__main__":
    create_dir()
    rospy.init_node("scan_world_recorder")
    ScanWorldRecorder()

    rospy.spin()

