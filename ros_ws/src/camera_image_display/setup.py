from setuptools import find_packages, setup

package_name = 'camera_image_display'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elf',
    maintainer_email='elf@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_image_display = camera_image_display.camera_image_display:main',
            'ros_llm_inference_node = camera_image_display.ros_llm_inference_node:main',
            'rgbd_depth_reader_node = camera_image_display.rgbd_depth_reader_node:main',
            'yolo8 = camera_image_display.yolo8:main',
            'yolo_depth_fusion_node = camera_image_display.yolo_depth_fusion_node:main',
            'test_voice_node = camera_image_display.test_voice_node:main',
            'speaker = camera_image_display.speaker:main',
            'web_camera_node = camera_image_display.web_camera_node:main',
            'llm_web_node = camera_image_display.llm_web_node:main',
            'web_voice_node = camera_image_display.web_voice_node:main',
            'llm_auto_node = camera_image_display.llm_auto_node:main',
            'feishu_logger = camera_image_display.feishu_logger:main',
            'unified_llm_node = camera_image_display.unified_llm_node:main',
        ],
    },
)
