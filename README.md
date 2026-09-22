# 采摘机器人 ROS 工作空间（agilex_ws / src）

基于 ROS 1 的果园采摘机器人导航与底盘控制源码。履带差速底盘（`yhs_dgt001m_oc`），
采用 ROS Navigation Stack（AMCL + DWA）实现航点巡检导航。

## 目录结构

| 目录 | 说明 |
| --- | --- |
| `car_base/` | 底盘驱动与控制：`yhs_can_control`（YHS CAN 协议驱动）、`yocs_velocity_smoother`（速度平滑）、`TK-mid-ros1`（中层控制） |
| `sensors/lidar/` | 激光雷达驱动：`rslidar_sdk-v1.5.0`（RS16）、`lslidar_cx_driver` |
| `SLAM/` | 定位与建图：`rf2o_laser_odometry`（纯激光里程计，10Hz）、`pointcloud_to_laserscan`、`openslam_gmapping`、`laser_scan_matcher` |
| `start/agilexpro/` | 启动入口：launch 文件、生效参数（`param/4wd/`）、地图、rviz 配置 |
| `msg/` | 自定义消息：`agx_pick_msg`、`dh_gripper_msgs`（夹爪）、`ar_track_alvar_msgs` |
| `plugin/` | rviz 多目标点发布插件 |
| `yhs_msgs/` | YHS 底盘消息定义 |

## 启动顺序

```bash
roslaunch agilexpro base.launch        # 底盘 + 雷达 + 里程计
roslaunch agilexpro nav.launch         # AMCL + move_base（DWA）
roslaunch agilexpro nav_to_wp.launch   # 航点导航
```

## 控制链路

```
move_base (/cmd_vel) → cmd_vel_to_yhs.py → /ctrl_cmd → yhs_can_control → CAN 总线
```

底盘不直接订阅 `/cmd_vel`；velocity_smoother 处于旁路，下游节点自行做斜坡限幅兜底。
CAN 指令约定：角速度单位为度/秒（×100），线速度 ×1000，`gear=3` 表示运动学控制模式。
`/ctrl_cmd`、`/io_cmd` 需以 100Hz 发布。

## 关键配置说明

- **生效参数目录**：`start/agilexpro/param/4wd/`（DWA）。`param/carlike/`、`param/config/`
  及 `*(copy).yaml` 均为不生效的历史文件。
- **雷达视野**：RS16 仅 240°（±120°），车尾 120° 为盲区 → DWA 设 `min_vel_x: 0.0` 禁止倒车。
- **点云压平**：`point_to_scan.launch` 仅取雷达系 z∈[-0.1, 0.5] 的点，`range_min=0.2`。
- **坐标系**：AMCL 发布 `world → odom`，局部代价地图挂 `odom`，全局挂 `world`；
  `base_frame_id: rslidar`。启动须传 `initial_pose_x/y/a`。
- **遥控手柄**：必须切「自动挡」，否则 `joypad_ctrl=1`，底盘忽略 `/ctrl_cmd`。

## 依赖

- ROS 1（Noetic 推荐）
- 见各包 `package.xml`

## 编译

```bash
cd agilex_ws
catkin_make
source devel/setup.bash
```
