#!/usr/bin/env python3

#######################
#                     # 
# Name: Jaayanth SK   #
# Roll No.: ED21B029  #
# Question: A.2       #
#                     #
#######################

import rospy
from std_msgs.msg import String


def callback(data):
    pub = rospy.Publisher("naayihba_maet", String, queue_size=10)
    rate = rospy.rate(0.5)
    info = "".join(reversed(data.data))
    pub.publish(info)
    rospy.loginfo(info)


def listener():
    rospy.init_node("str_rev", anonymous=True)
    rospy.Subscriber("team_abhiyaan", String, callback)
    rospy.spin()


if __name__ == "__main__":
    listener()
