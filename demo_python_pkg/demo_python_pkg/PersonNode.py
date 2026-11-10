import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name: str,age: int):
        super().__init__("node_name")
        self.age = age

def main():
    rclpy.init()
    person = PersonNode("Huchen", 18)
    print(f"Age: {person.age}")
    rclpy.spin(person)
    rclpy.shutdown()