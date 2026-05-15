import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger
from std_msgs.msg import String

class HistoryService(Node):

    def __init__(self):
        super().__init__('history_service')

        # store latest history coming from cmd_parser
        self.history = ""

        # subscribe to shared history topic
        self.sub = self.create_subscription(
            String,
            '/command_history',
            self.history_callback,
            10
        )

        # service
        self.srv = self.create_service(
            Trigger,
            '/get_history',
            self.callback
        )

        self.get_logger().info("History service ready")

    def history_callback(self, msg):
        self.history = msg.data

    def callback(self, request, response):
        response.success = True
        response.message = self.history
        return response


def main():
    rclpy.init()
    node = HistoryService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()