#!/usr/bin/env python

# How to run this file:
# 1. Make sure you can roscd turtlebot_gazebo
# 2. roslaunch turtlebot_gazebo turtlebot_world.launch 
#	export TURTLEBOT_GAZEBO_WORLD_FILE=/home/cuil/catkin/wsv2/src/turtlebot_gazebo/worlds/custom_corridorV1.world
# 3. Start the gmapping SLAM system (Starts the TF/odom system)
# 4. Start RVIZ to visualize the TF frames/odom system

# Basic Movements of Turtlebot robot.
# Note: These movements are enacted only by running putting in velocity to the move_base
# For more precision, the tf/odom data should be read


# API links 
# http://docs.ros.org/api/rospy/html/
# http://docs.ros.org/api/geometry_msgs/html/msg/;http://wiki.ros.org/geometry_msgs
#

# import the package rospy - which is a collection of helpful classes
import rospy

# import the class to make messages
from geometry_msgs.msg import Twist


def obj1():

	# register client node with the master - roscore
	rospy.init_node('obj1', anonymous=True)

	rospy.on_shutdown(cleanup)

	# create a object after registering as publisher to the master node
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

	# create a object of the Twist class
	msg = Twist()

	# convenience class to sleep in a loop at a specified rate
	r = rospy.Rate(10) # 10hz

	# The twist object has two vectors - linear and angular
	# Linear, angular have three float64 elements - x,y,z
	# The twist object is used to specifiy the linear and angular velocity

	# Go Forward 
	msg.linear.x= 0.5
	msg.angular.z= 0    
	for x in range(1, 30):
		pub.publish(msg)
		r.sleep()

	# Go Backward 
	msg.linear.x= -0.5
	msg.angular.z= 0    
	for x in range(1, 30):
		pub.publish(msg)
		r.sleep()

	# Make the robot turn
	for x in range(1, 30):
	    msg.linear.x= 0
	    msg.angular.z= 1
	    pub.publish(msg)
	    r.sleep()

	# Make sure the final twist message sent to the robot makes it stop
	msg.linear.x= 0
	msg.angular.z= 0
	pub.publish(msg)
	

if __name__ == '__main__':
	try:
		obj1()
	except rospy.ROSInterruptException: pass
