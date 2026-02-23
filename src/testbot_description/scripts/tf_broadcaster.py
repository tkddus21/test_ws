#!/usr/bin/env python3

import rospy
import tf
from tf.transformations import quaternion_from_euler
import math
import time

class TFBroadcaster:
    def __init__(self):
        rospy.init_node('tf_broadcaster', anonymous=True)
        self.br = tf.TransformBroadcaster()
        self.rate = rospy.Rate(10)  # 10 Hz

    def broadcast(self):
        rospy.loginfo("TF Broadcaster started")
        
        while not rospy.is_shutdown():
            try:
                # Current time
                current_time = rospy.Time.now()
                
                # Broadcast transform from odom to base_link
                # In a real robot, this would come from odometry calculation
                quaternion = quaternion_from_euler(0, 0, 0)
                
                self.br.sendTransform(
                    (0.0, 0.0, 0.0),  # translation (x, y, z)
                    quaternion,        # rotation (qx, qy, qz, qw)
                    current_time,      # timestamp
                    "base_link",       # child frame
                    "odom"             # parent frame
                )
                
                self.rate.sleep()
                
            except Exception as e:
                rospy.logerr(f"Error in TF broadcaster: {e}")
                self.rate.sleep()

if __name__ == '__main__':
    try:
        broadcaster = TFBroadcaster()
        broadcaster.broadcast()
    except rospy.ROSInterruptException:
        rospy.loginfo("TF Broadcaster stopped")
