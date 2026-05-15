from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='robot_echo',
            executable='cmd_parser',
            name='cmd_parser'
        ),
        Node(
            package='robot_echo',
            executable='logger_node',
            name='logger'
        ),
        Node(
            package='robot_echo',
            executable='history_service',
            name='history_service'
        ),
    ])