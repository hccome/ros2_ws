import espeakng
import rclpy
import threading
import time
from rclpy.node import Node
from queue import Queue
from example_interfaces.msg import String

class NovelSubscriber(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.subscription = self.create_subscription(String, 'novel', self.novel_callback, 10)
        self.queue = Queue()
        self.speaker_thread = threading.Thread(target=self.speak)
        self.speaker_thread.start()

    def novel_callback(self, msg):
        self.get_logger().info(f"receive novel:{msg.data}")
        self.queue.put(msg.data)

    def speak(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'zh'
        while rclpy.ok():
            if self.queue.qsize() > 0:
                text = self.queue.get()
                self.get_logger().info(f"speaking novel:{text}")
                speaker.say(text)
                speaker.wait()
            else:
                #sleep
                time.sleep(1)


def main():
    rclpy.init()
    node = NovelSubscriber("novel_sub")
    rclpy.spin(node)
    rclpy.shutdown()
