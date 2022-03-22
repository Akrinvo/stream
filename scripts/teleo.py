import rospy  # !/usr/bin/env python
from geometry_msgs.msg import Twist
import math as m
import time
import websocket
ws1=websocket.WebSocket()
ws1.connect("ws://192.168.194.61 ")
print("connected to websocket server")

def vel_info_callback(info):
    x = info.linear.x
    yaw = info.angular.z
    if x<0:
       ws1.send('-'+str(int(m.ceil(abs(x))))+" "+str(int(m.degrees(yaw))))
    else: 
        ws1.send(str(int(m.ceil(x)))+" "+str(int(m.degrees(yaw))))
    # ws1.send(str(int(m.degrees(yaw))))
    print("linear speed ",x,"angular speed ",yaw)
    

def cmd():
    rospy.init_node("start", anonymous=False)
    vel_sub = rospy.Subscriber("cmd_vel", Twist, vel_info_callback)
    rospy.loginfo("Starting name_node.")
   
    # if rospy.is_shutdown:
    #     ws1.close()
    #     return
    # else: 
    rospy.spin()


if __name__ == "__main__":
    cmd()
