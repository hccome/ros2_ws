#include "rclcpp/rclcpp.hpp"

class PersonNode : public rclcpp::Node
{
    private:
        std::string name_;
        int age_;

    public:
        PersonNode(const std::string &node_name,const std::string & name,const int age) : Node(node_name)
        {
            this -> name_ = name;
            this -> age_ = age;
            std::cout << "my name is" << name_ << " and age is " << age_ << std::endl;
        }
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PersonNode>("John", "John Doe", 30);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}