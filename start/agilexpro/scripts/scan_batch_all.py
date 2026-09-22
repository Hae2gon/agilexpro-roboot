#!/usr/bin/env python3
import os

SAVE_ROOT = "/home/test/agilex_ws/agilex_ws/src/start/agilexpro/txt/"
OUT_MERGE = os.path.join(SAVE_ROOT, "total_all_points.txt")

def merge_all():
    all_points = set()  # set自动去重重复坐标点
    # 遍历目录所有txt
    for filename in os.listdir(SAVE_ROOT):
        if filename.startswith("batch_") and filename.endswith(".txt"):
            file_path = os.path.join(SAVE_ROOT, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    # 跳过注释/空行
                    if not line or line.startswith("#"):
                        continue
                    all_points.add(line)
    # 写入合并文件
    with open(OUT_MERGE, "w", encoding="utf-8") as f:
        f.write(f"合并总点数：{len(all_points)}\n")
        f.write("x,y\n")
        for p in sorted(all_points):
            f.write(p + "\n")
    print(f"合并完成！总有效坐标点：{len(all_points)}，输出文件：{OUT_MERGE}")

if __name__ == "__main__":
    merge_all()

