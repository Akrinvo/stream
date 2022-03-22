from tkinter import Frame
import rospy as rp
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys


cap=cv2.VideoCapture(0)
bridge=CvBridge()

def Image_callback():
    pub = rp.Publisher('/cam',Image,queue_size=1)
    rp.init_node('image',anonymous=False)
    while not rp.is_shutdown():
        ret,frame=cap.read()
    
        cv_image=bridge.cv2_to_imgmsg(frame,'bgr8')
       
        pub.publish(cv_image)
        


        cv2.imshow("image",frame)
        # cv2.imshow("immage",gray)

        if cv2.waitKey(1)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
      
        




if __name__=="__main__":
    Image_callback()