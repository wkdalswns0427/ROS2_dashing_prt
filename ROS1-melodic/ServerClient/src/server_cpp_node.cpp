#include <ros/ros.h>
#include <dyros_practice_2/ABAngle.h>
#include <cmath>

using namespace std;

bool service_callback(dyros_practice_2::ABAngle::Request &req,
    dyros_practice_2::ABAngle::Response &res)
{
    res.c = sqrt(pow(req.a,2) + pow(req.b,2) - 2*req.a*req.b*cos(req.angle));
    ROS_INFO("Calculating c using law of cosine request: %.1lf %.1lf %.1lf",
        req.a, req.b, req.angle * 180.0 / M_PI);
    return true;
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "dyros_server");
    ros::NodeHandle nh;
    ros::ServiceServer srv_server = nh.advertiseService("/cosine_calc", service_callback);
    ros::spin();
    return 0;
}