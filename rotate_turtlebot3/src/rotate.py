#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

rospy.init_node('rotate_turtlebot')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)

rot = Twist()
rot.angular.z = 0.5

full_rotation_angle = 2 * math.pi
current_angle = 0.0
target_angle = full_rotation_angle


while not rospy.is_shutdown() and current_angle < target_angle:
    pub.publish(rot)
    rate.sleep()

    # 루프 주기 동안 회전한 각도 누적
    current_angle += abs(rot.angular.z) * (1.0 / rate.sleep_dur.to_sec())

    rospy.loginfo("Current angle: %f", current_angle)

pub.publish(Twist())  # 회전을 멈추기 위해 빈 Twist 메시지 발행
rospy.loginfo("Rotation completed.")

rospy.spin()