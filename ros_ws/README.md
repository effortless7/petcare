1.运行前先启动相机
cd ros_ws
./run_ascamera_node.sh

2.node介绍
ros_ws/src/camera_image_display/camera_image_display下的几个.py文件
需要ros2运行
rgbd_depth_reader_node：可以返回鼠标点击位置的（x，y）坐标及深度depth
ros_llm_inference_node：可以截取视频帧发送给大模型做图文理解，可以修改问题
yolo_depth_fusion_node：可以输出yolo目标检测到指定对象的中心坐标及深度，控制小车追踪
web_voice_node：接收远程消息并播报
llm_web_node：将大模型分析结果及图像push出去


yolo8：目标检测

3.运行方式
ros2 run camera_image_display ros_llm_inference_node 
ros2 run camera_image_display yolo_depth_fusion_node

注意使用大模型前先定位到主文件夹运行
./start.sh

4.功能及介绍
首先定位到主文件夹并启动大模型
cd
./start.sh
之后进入ros_ws启动相机
./run_ascamera_node.sh 
再之后启动核心脚本，有四个功能node
ros2 run camera_image_display yolo_depth_fusion_node
ros2 run camera_image_display llm_auto_node
ros2 run camera_image_display llm_web_node
ros2 run camera_image_display web_voice_node