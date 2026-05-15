import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import TwistStamped


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.pub = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

        self.safe_distance = 0.5

        self.get_logger().info("Obstacle Avoidance Started")

    def scan_callback(self, msg):

        front_distance = min(msg.ranges[0:20])

        twist_msg = TwistStamped()

        if front_distance < self.safe_distance:
            self.get_logger().warn("Obstacle detected - turning")
            twist_msg.twist.angular.z = 0.8
        else:
            twist_msg.twist.linear.x = 0.2

        self.pub.publish(twist_msg)


def main():
    rclpy.init()
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()