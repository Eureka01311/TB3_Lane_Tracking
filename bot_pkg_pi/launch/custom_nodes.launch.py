from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. 카메라 영상 발행 노드
        Node(
            package='bot_pkg_pi',
            executable='cam_pub',
            name='cam_pub_node',
            output='screen'
        ),
        # 2. 모터 제어 노드
        Node(
            package='bot_pkg_pi',
            executable='motor',
            name='motor_node',
            output='screen'
        ),
        # 3. 라이다 데이터 처리 노드
        Node(
            package='bot_pkg_pi',
            executable='lidar',
            name='lidar_node',
            output='screen'
        ),
    ])
