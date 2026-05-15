import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class CmdParser(Node):

    def __init__(self):
        super().__init__('cmd_parser')

        self.sub = self.create_subscription(
            String,
            '/cmd_text',
            self.callback,
            10
        )
        self.history_pub = self.create_publisher(
            String,
            '/command_history',
            10
        )
        self.pub = self.create_publisher(
            Twist,
            '/robot_response',
            10
        )
        
        self.history = []

        self.get_logger().info("Cmd Parser Ready")

    def callback(self, msg):
        text = msg.data.lower().strip()
        twist = Twist()

        if text.startswith("avance"):
            n = float(text.split()[1])
            twist.linear.x = n

        elif text.startswith("recule"):
            n = float(text.split()[1])
            twist.linear.x = -n

        elif text.startswith("tourne_gauche"):
            a = float(text.split()[1])
            twist.angular.z = a

        elif text.startswith("tourne_droite"):
            a = float(text.split()[1])
            twist.angular.z = -a

        elif text == "stop":
            pass  # all zero

        else:
            self.get_logger().warn("Unknown command")
            return

        self.history.append(text)
        self.history = self.history[-10:]
        msg = String()
        msg.data = "\n".join(self.history)
        self.history_pub.publish(msg)
        self.pub.publish(twist)
        self.get_logger().info(f"Executed: {text}")


def main():
    rclpy.init()
    node = CmdParser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()