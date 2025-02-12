import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Leader Node
    leader_node = Node(
        package='motion_controller',          # Replace with your package name
        executable='Leader_node',             # Replace with your leader node executable name
        name='Leader_node',
        output='screen',
        parameters=[],
        remappings=[],
    )

    # Chaser Node
    chaser_node = Node(
        package='motion_controller',          # Replace with your package name
        executable='Chaser_node',             # Replace with your chaser node executable name
        name='Chaser_node',
        output='screen',
        parameters=[],
        remappings=[],
    )

    return LaunchDescription([
        leader_node,
        chaser_node
    ])

