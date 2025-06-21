import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):
    def __init__(self):
        super().__init__("Node_Publisher")
        self.pub=self.create_publisher(String,"chat",10)
        self.count=0
        self.freq=1
        self.get_logger().info(f"Publsihing at {self.freq} Hz")
        self.timer=self.create_timer(1/self.freq,self.timercall)

    def timercall(self):
        msg=String()
        msg.data=f"Hello ROS2: {self.count}"
        self. count+=1
        self.pub.publish(msg)
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    publish=SimplePublisher()
    rclpy.spin(publish)
    publish.destroy_node()
    rclpy.shutdown()


if __name__=="__main__":
    main()
