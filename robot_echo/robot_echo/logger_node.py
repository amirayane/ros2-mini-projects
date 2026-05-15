import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Logger(Node):

    def __init__(self):
        super().__init__('logger')

        self.file = open("commands.log", "a")

        self.sub = self.create_subscription(
            String,
            '/cmd_text',
            self.log,
            10
        )

    def log(self, msg):
        self.file.write(msg.data + "\n")
        self.file.flush()


def main():
    rclpy.init()
    node = Logger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()