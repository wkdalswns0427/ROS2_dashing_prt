#!/usr/bin/env python
import sys
import rospy
import math
from dyros_practice_2.srv import *

def dyros_calc_client(a, b, angle):
    rospy.wait_for_service('/cosine_calc')
    try:
        dyros_calc = rospy.ServiceProxy('/cosine_calc', ABAngle)
        resp1 = dyros_calc(a, b, angle)
        return resp1.c
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [a b angle(degree)]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        angle = math.radians(float(sys.argv[3]))
    else:
        print usage()
        sys.exit(1)
    print ("Requesting with %s %s %s"%(a, b, math.degrees(angle)))
    print ("c = %s"%(dyros_calc_client(a, b, angle)))
