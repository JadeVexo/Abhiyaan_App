#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("team_abhiyaan", String, queue_size=10)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        str = "Team Abhiyaan rocks:" 
        rospy.loginfo(str)
        pub.publish(str)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass