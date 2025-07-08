cmake_minimum_required(VERSION 3.8)
project(camera_image_display)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/DetectionInfo.msg"
)

# Python installation
ament_python_install_package(${PROJECT_NAME}) 