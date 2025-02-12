My basic approach to this problem was to use turtlebot3, spawining 2 of them in gazebo, 
1 being the leader second being the follower.

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