#!/usr/bin/env python3
import rospy
import yaml
import os
from PIL import Image, ImageDraw, ImageFont
from geometry_msgs.msg import PoseWithCovarianceStamped

# ================= 已经按你实际情况写好的路径 =================
MAP_FILE = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/0525"
# ==============================================================

# 全局变量存储当前位姿
current_x = 0.0
current_y = 0.0
pose_ready = False

def amcl_pose_cb(msg):
    """订阅 /amcl_pose 回调，获取map坐标系坐标"""
    global current_x, current_y, pose_ready
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y
    pose_ready = True

def main():
    global pose_ready
    pose_ready = False
    rospy.init_node("auto_map_label", anonymous=True)

    # 订阅机器人位姿
    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, amcl_pose_cb)
    rospy.loginfo("正在获取机器人当前位置...")

    # 等待位姿数据
    rospy.sleep(2)
    if not pose_ready:
        rospy.logerr("未获取到 /amcl_pose 数据，请检查AMCL是否正常运行！")
        return

    rospy.loginfo(f"获取到位姿：x = {current_x:.2f}, y = {current_y:.2f}")

    # 1. 读取地图yaml参数
    yaml_path = MAP_FILE + ".yaml"
    if not os.path.exists(yaml_path):
        rospy.logerr(f"地图配置文件不存在: {yaml_path}")
        return
    with open(yaml_path, "r") as f:
        map_cfg = yaml.safe_load(f)
    resolution = map_cfg["resolution"]
    origin_x, origin_y, _ = map_cfg["origin"]
    rospy.loginfo(f"地图参数：分辨率={resolution}, 原点=({origin_x}, {origin_y})")

    # 2. 读取pgm地图
    pgm_path = MAP_FILE + ".pgm"
    img = Image.open(pgm_path).convert("RGB")
    if img is None:
        rospy.logerr(f"地图图片不存在: {pgm_path}")
        return
    w, h = img.size
    rospy.loginfo(f"地图尺寸：宽={w}, 高={h}")

    # 3. 世界坐标转图像像素坐标（ROS地图Y轴与图像Y轴反向）
    def world2pixel(x, y):
        px = int((x - origin_x) / resolution)
        py = h - int((y - origin_y) / resolution)
        return (px, py)

    px, py = world2pixel(current_x, current_y)
    rospy.loginfo(f"转换后的像素坐标：px={px}, py={py}")

    # 4. 绘制标记：红色圆点 + 坐标文字
    draw = ImageDraw.Draw(img)
    # 画圆点
    draw.ellipse([(px-5, py-5), (px+5, py+5)], fill=(255, 0, 0))

    # 加载字体（Ubuntu默认字体，确保路径存在）
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    if not os.path.exists(font_path):
        # 备用：使用默认字体
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, 12)

    # 写文字
    text = f"Init Point\nx:{current_x:.2f} y:{current_y:.2f}"
    draw.text((px + 10, py), text, fill=(255, 0, 0), font=font)

    # 5. 保存带标注的图片
    SAVE_IMG = MAP_FILE + "_labeled.png"
    img.save(SAVE_IMG)
    rospy.loginfo(f"标注完成！图片已保存至：{SAVE_IMG}")

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

