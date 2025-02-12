import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64MultiArray, Bool
import random

class CircularMotion(Node):
    def __init__(self):
        super().__init__("Leaderbot_circular_motion")

        self.vel_publisher = self.create_publisher(Twist, "/cmd_vel", 10)
     
        self.timer = self.create_timer(0.01, self.Circular_motion)

        self.Radius = 1.0
        self.linear_velocity = 1.0  
        self.angular_velocity = self.linear_velocity / self.Radius 

    def Circular_motion(self):
        cmd_vel = Twist()
        cmd_vel.linear.x = self.linear_velocity 
        cmd_vel.angular.z = self.angular_velocity  
        self.vel_publisher.publish(cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    circular_turtle = CircularMotion()
    rclpy.spin(circular_turtle)
    rclpy.shutdown()

if __name__ == "__main__":
    main()