#include <ros/ros.h>
#include <std_msgs/Int32.h>

void helloros_callback(const std_msgs::Int32::ConstPtr &msg) {
    ROS_INFO("Hello ROS %d", msg->data);
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "dyros_subscriber_node");
    ros::NodeHandle nh;
    ros::Subscriber helloros_sub = nh.subscribe("/helloros_topic", 1, &helloros_callback);
    ros::spin();
    return 0;
}