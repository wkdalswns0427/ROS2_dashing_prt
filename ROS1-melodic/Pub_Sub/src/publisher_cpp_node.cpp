#include <ros/ros.h>
#include <std_msgs/Int32.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "dyros_publisher_node");
    ros::NodeHandle nh;
    ros::Publisher helloros_pub = nh.advertise<std_msgs::Int32>("/helloros_topic", 1);
    ros::Rate rate(1);
    
    std_msgs::Int32 msg;
    int i = 1;

    while(ros::ok()) {
        helloros_pub.publish(msg);
        msg.data = i++;
        rate.sleep();
    }

return 0;
}