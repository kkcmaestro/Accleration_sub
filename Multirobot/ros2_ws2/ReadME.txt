My basic approach to this problem was to use turtlebot3, spawining 2 of them in gazebo, 
1 being the leader second being the follower.

First you have to create a repository and clone turtlebot3 in the workspace.
Build it and then source it. 

Run gazebo and turtlebot
export TURTLEBOT3_MODEL=burger  # Or waffle, waffle_pi
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

Spawn turtle 2 via 

ros2 run gazebo_ros spawn_entity.py -entity turtlebot3_2 \
-file `ros2 pkg prefix turtlebot3_gazebo`/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf \
-x 2 -y 0 -z 0 -robot_namespace turtlebot2

The leader would use the node via

ros2 run motion_control Leader_node

and chaser uses

ros2 run motion_control Chaser_node

the leader node publishes velocity to /cmd_vel for the leader

the chaser robot accesses the real time pose of leader via /odom publisher and then
uses a simple pid controller for following it

there are issues with the /odem pose data so it is not following it as required.


the packages required for this are 
turtlebot3 (and all included pakcages)
Nav2
gazebo