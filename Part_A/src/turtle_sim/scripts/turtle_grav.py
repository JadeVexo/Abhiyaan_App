#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PKG = 'turtle_sim'
import roslib; roslib.load_manifest(PKG)
import math
import numpy

motion1 = Twist()
motion2 = Twist()
G = 0.0005
M1 = 1
M2 = 1

x1,y1,x2,y2= 5,4,5,6

def callback1(data):
    global x1,y1
    x1 = data.x
    y1 = data.y
def callback2(data):
    global x2,y2
    x2 = data.x
    y2 = data.y
    
def move():
    global x1,y1,x2,y2,vel1,vel2
    
    rospy.Subscriber("t1/pose", Pose,callback1)
    rospy.Subscriber("t2/pose", Pose,callback2)

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    motion1.linear.x += G*M2/(distance**2)
    motion2.linear.x += - G*M1/(distance**2)
    motion1.angular.z = 1
    motion2.angular.z = 1

motion1.linear.x = 0
motion1.linear.y = 0
motion2.linear.x = 0
motion2.linear.y = 0
motion1.angular.z = 1
motion2.angular.z = 1

rospy.init_node('turtle_gravity')

pub1 = rospy.Publisher('t1/cmd_vel', Twist ,queue_size = 10)
pub2 = rospy.Publisher('t2/cmd_vel', Twist ,queue_size = 10)

rate = rospy.Rate(1000)

while not rospy.is_shutdown():

    move()
    pub1.publish(motion1)
    pub2.publish(motion2)
    rate.sleep()












