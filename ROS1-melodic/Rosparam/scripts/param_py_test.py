#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def param_test():
    pub = rospy.Publisher('what_the_param', String, queue_size=10)
    rospy.init_node('dyros_param_test_node', anonymous=False)
    rospy.set_param('some_name', 'this_is_param')
    rospy.set_param('~private_int', 100)
    rospy.set_param('list_of_floats', [1., 2., 3., 4.])
    rospy.set_param('bool_true', True)
    rospy.set_param('gains', {'p': 100.0, 'i': 0.0, 'd': 20.0})
    rate = rospy.Rate(1) # 1 hz
    while not rospy.is_shutdown():
        text = rospy.get_param('some_name')
        p_gain = rospy.get_param('gains/p')
        rospy.loginfo(text)
        rospy.loginfo('P gain is ' + str(p_gain))
        pub.publish(text)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        param_test()
    except rospy.ROSInterruptException:
        pass
