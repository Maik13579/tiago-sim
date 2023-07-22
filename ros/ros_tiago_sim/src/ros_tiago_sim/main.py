#!/usr/bin/env python3

import rospy

from ros_tiago_sim_interfaces.msg import Example
from tiago_sim import example_function

class TiagoSim():
    def __init__(self):
        rospy.init_node("ros_tiago_sim", anonymous=True)
        rospy.loginfo("Starting")
        
        # Publisher
        #self.pub = rospy.Publisher(TOPIC, MSG, queue_size=10)

        # Subscriber
        #rospy.Subscriber(TOPIC, MSG, CALLBACK)

        #Execute main loop
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.loop()
            rate.sleep()

    def loop(self):
        '''
        main loop
        '''
        rospy.loginfo(Example())
        example_function()



if __name__ == '__main__':
    TiagoSim()

