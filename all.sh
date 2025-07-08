#!/bin/bash

# Step 1: 回到主目录并运行 start.sh（可能初始化环境变量）
cd ~ || { echo "回到主目录失败"; exit 1; }

echo "运行 start.sh..."
gnome-terminal -- bash -c "./start.sh; exec bash"

# 等待初始化完成（根据你 start.sh 内容调整等待时间）
sleep 3

# Step 2: 启动相机节点
cd ~/ros_ws || { echo "进入 ros_ws 目录失败"; exit 2; }

echo "运行相机节点..."
gnome-terminal -- bash -c "./run_ascamera_node.sh; exec bash"

# 等待相机初始化
sleep 3

# Step 3: 启动核心 unified_llm_node 节点
echo "运行 unified_llm_node 节点..."
gnome-terminal -- bash -c "cd ~/ros_ws && source install/setup.bash && ros2 run camera_image_display unified_llm_node; exec bash"
gnome-terminal -- bash -c "cd ~/ros_ws && source install/setup.bash && ros2 run camera_image_display yolo_depth_fusion_node; exec bash"