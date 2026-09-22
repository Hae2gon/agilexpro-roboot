#!/usr/bin/env python3
import yaml
import os
from PIL import Image, ImageDraw, ImageFont

MAP_YAML = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/0525.yaml"
WP_YAML = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/waypoints_0603.yaml"
OUT_PIC = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/maps/map_mark.png"

# 世界坐标转图片像素
def world_to_pixel(world_x, world_y, orig_x, orig_y, res, img_h):
    pix_x = int((world_x - orig_x)/res)
    pix_y = img_h - int((world_y - orig_y)/res)
    return pix_x, pix_y

if __name__ == "__main__":
    # 读取地图配置
    with open(MAP_YAML, "r", encoding="utf-8") as f:
        map_cfg = yaml.safe_load(f)
    img_abs_path = os.path.join(os.path.dirname(MAP_YAML), map_cfg["image"])
    res = map_cfg["resolution"]
    ox, oy, _ = map_cfg["origin"]

    # 打开地图图片
    img = Image.open(img_abs_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    img_h, img_w = img.height, img.width

    # 读取途径点
    with open(WP_YAML, "r", encoding="utf-8") as f:
        wp_data = yaml.safe_load(f)["waypoints"]

    # 配色：起点绿、途经橙、终点红
    for idx, point in enumerate(wp_data):
        px, py = world_to_pixel(point["x"], point["y"], ox, oy, res, img_h)
        if idx == 0:
            fill_color = (0,255,0)    #绿色 起始点
        elif idx == len(wp_data)-1:
            fill_color = (255,0,0)    #红色 终点
        else:
            fill_color = (255,165,0)  #橙色 途经点
        #画圆点
        r = 6
        draw.ellipse([px-r,py-r,px+r,py+r], fill=fill_color)
        #写字
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",10)
        except:
            font = ImageFont.load_default()
        draw.text((px+8,py), point["name"], fill=fill_color, font=font)

    img.save(OUT_PIC)
    print("标注地图生成完毕，路径：",OUT_PIC)

