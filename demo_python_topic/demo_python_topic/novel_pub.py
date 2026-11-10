import rclpy
from rclpy.node import Node
import requests
from queue import Queue
from example_interfaces.msg import String

class NovelPublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name},started")
        self.queue = Queue()
        #消息类型，话题名，队列长度
        self.novel_publisher = self.create_publisher(String, 'novel', 10)
        self.create_timer(5.0, self.default_callback)

    def default_callback(self):
        if self.queue.qsize() > 0:
            msg = String()
            msg.data = self.queue.get()
            self.novel_publisher.publish(msg)
            self.get_logger().info(f"publish novel:{msg.data}")


    def download(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        for line in text.splitlines():
            self.queue.put(line)

def main():
    rclpy.init()
    node = NovelPublisher("novel_pub")
    node.download("http://localhost:8000/novel1.txt")
    rclpy.spin(node)
    rclpy.shutdown()