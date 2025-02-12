import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class FollowerRobot(Node):
    def __init__(self):
        super().__init__("leader_subscriber")

        self.vel_publisher = self.create_publisher(Twist, "/turtlebot2/cmd_vel", 10)
        self.leader_pose_subscriber = self.create_subscription(Odometry, "/odom", self.leader_pose_callback, 10)
        self.follower_pose_subscriber = self.create_subscription(Odometry, "/turtlebot2/odom", self.follower_pose_callback, 10)

        self.timer = self.create_timer(0.1, self.chase_leader)

        self.kp_linear = 1.2
        self.kd_linear = 0.2
        
        self.kp_angular = 2.0
        self.kd_angular = 0.3

        self.leader_pose = None  
        self.follower_pose = None  
        self.prev_error_linear = 0.0
        self.prev_error_angular = 0.0

    def leader_pose_callback(self, msg):
        self.leader_pose = (msg.pose.pose.position.x, msg.pose.pose.position.y)

    def follower_pose_callback(self, msg):
        self.follower_pose = (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.orientation.z)

    def chase_leader(self):
        if self.leader_pose is None or self.follower_pose is None:
            return 

        leader_x, leader_y, police_theta = self.follower_pose
        error_x = self.leader_pose[0] - leader_x
        error_y = self.leader_pose[1] - leader_y
        error_dist = math.sqrt(error_x**2 + error_y**2)
        desired_angle = math.atan2(error_y, error_x)
        angle_error = desired_angle - police_theta
        angle_error = (angle_error + math.pi) % (2 * math.pi) - math.pi

        cmd_vel = Twist()
        cmd_vel.linear.x = min(1.0, error_dist * self.kp_linear + (error_dist - self.prev_error_linear) * self.kd_linear)
        cmd_vel.angular.z = self.kp_angular * angle_error + (angle_error - self.prev_error_angular) * self.kd_angular
        self.vel_publisher.publish(cmd_vel)

        self.prev_error_linear = error_dist
        self.prev_error_angular = angle_error


def main(args=None):
    rclpy.init(args=args)
    police_turtle = FollowerRobot()
    rclpy.spin(police_turtle)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
