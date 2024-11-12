import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_chair_circle_move = get_package_share_directory('robot_circle')
    pkg_robot_bringup = get_package_share_directory('robot_bringup')
    
    circle_move = Node(
        package='robot_circle',
        executable='circle_move',
        output='screen',
    )

    robot_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_robot_bringup, 'launch', 'diff_drive.launch.py')),
    )

    return LaunchDescription([
        robot_bringup,
        circle_move,
    ])