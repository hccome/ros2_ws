#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>
#include <functional>
#include "turtlesim/msg/pose.hpp"

using namespace std::chrono_literals;

class TurtlrControl : public rclcpp::Node
{
private:
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr subscriber_;

public:
    TurtlrControl(const std::string &node_name) : Node(node_name)
    {
        subscriber_ = this->create_subscription<geometry_msgs::msg::Twist>("turtle1/cmd_vel", 10, std::bind(&TurtlrControl::subscription_callback, this, std::placeholders::_1));
        timer_ = this->create_wall_timer(1000ms, std::bind(&TurtlrControl::timer_callback, this));
    }

    void subscription_callback(const geometry_msgs::msg::Twist::SharedPtr msg)
    {
        // Handle the received message
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TurtlrControl>("turtle_control_node");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}