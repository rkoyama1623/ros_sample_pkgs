#!/usr/bin/env python
import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    try:
        turtlename = rospy.get_param('~turtle')
    except:
        turtlename='turtle1'
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,# msg type
                     handle_turtle_pose,# callback function
                     turtlename)# additional args for callback function
    rospy.spin()
