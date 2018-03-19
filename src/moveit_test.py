#!/usr/bin/env python

import sys, rospy, tf, moveit_commander, random

from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
#pose = Pose(Point(-.617511214138, -0.912743904483, 0.92032347395), orientation)
pose = Pose(Point(-.617511214138, -0.912743904483, 0.92032347395), Quaternion(0.369237115906, -0.594177966656, 0.714230696571, 0.0221587060407))
print("hi")
print(pose)
print("bye")


moveit_commander.roscpp_initialize(sys.argv)  # Python interface to MoveIt

rospy.init_node('wave_mobile_arm', anonymous = True)

group = moveit_commander.MoveGroupCommander("end_effector")

while not rospy.is_shutdown():
#    pose.position.z = 0.5 + random.uniform(-0.1, 0.1)
    group.set_pose_target(pose)
    group.go(True)
#    cur_pos = group.get_current_pose()
#    print(cur_pos)

moveit_commander.roscpp_shutdown()
