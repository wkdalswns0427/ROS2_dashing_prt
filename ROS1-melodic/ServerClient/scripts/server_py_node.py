#!/usr/bin/env python
from dyros_practice_2.srv import *
import rospy
from math import sqrt, pow, cos, degrees

def handle_calc_c(req):
    print ("Calculating c using law of cosine request: %s %s %s")%(req.a, req.b, degrees(req.angle))
    res = ABAngleResponse()
    res.c = sqrt(pow(req.a,2) + pow(req.b,2) - 2*req.a*req.b*cos(req.angle))
    return res

def dyros_calc_server():
    rospy.init_node('dyros_server')
    s = rospy.Service('/cosine_calc', ABAngle, handle_calc_c)
    print ("Ready to calculate the c.")
    rospy.spin()

if __name__ == "__main__":
    dyros_calc_server()
