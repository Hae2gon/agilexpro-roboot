;; Auto-generated. Do not edit!


(when (boundp 'yhs_can_msgs::l_wheel_fb)
  (if (not (find-package "YHS_CAN_MSGS"))
    (make-package "YHS_CAN_MSGS"))
  (shadow 'l_wheel_fb (find-package "YHS_CAN_MSGS")))
(unless (find-package "YHS_CAN_MSGS::L_WHEEL_FB")
  (make-package "YHS_CAN_MSGS::L_WHEEL_FB"))

(in-package "ROS")
;;//! \htmlinclude l_wheel_fb.msg.html


(defclass yhs_can_msgs::l_wheel_fb
  :super ros::object
  :slots (_l_wheel_fb_velocity _l_wheel_fb_pulse ))

(defmethod yhs_can_msgs::l_wheel_fb
  (:init
   (&key
    ((:l_wheel_fb_velocity __l_wheel_fb_velocity) 0.0)
    ((:l_wheel_fb_pulse __l_wheel_fb_pulse) 0)
    )
   (send-super :init)
   (setq _l_wheel_fb_velocity (float __l_wheel_fb_velocity))
   (setq _l_wheel_fb_pulse (round __l_wheel_fb_pulse))
   self)
  (:l_wheel_fb_velocity
   (&optional __l_wheel_fb_velocity)
   (if __l_wheel_fb_velocity (setq _l_wheel_fb_velocity __l_wheel_fb_velocity)) _l_wheel_fb_velocity)
  (:l_wheel_fb_pulse
   (&optional __l_wheel_fb_pulse)
   (if __l_wheel_fb_pulse (setq _l_wheel_fb_pulse __l_wheel_fb_pulse)) _l_wheel_fb_pulse)
  (:serialization-length
   ()
   (+
    ;; float32 _l_wheel_fb_velocity
    4
    ;; int32 _l_wheel_fb_pulse
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _l_wheel_fb_velocity
       (sys::poke _l_wheel_fb_velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _l_wheel_fb_pulse
       (write-long _l_wheel_fb_pulse s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _l_wheel_fb_velocity
     (setq _l_wheel_fb_velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _l_wheel_fb_pulse
     (setq _l_wheel_fb_pulse (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get yhs_can_msgs::l_wheel_fb :md5sum-) "9e8be88b3dcd0f2ea8c445a8c67235d0")
(setf (get yhs_can_msgs::l_wheel_fb :datatype-) "yhs_can_msgs/l_wheel_fb")
(setf (get yhs_can_msgs::l_wheel_fb :definition-)
      "float32    l_wheel_fb_velocity
int32      l_wheel_fb_pulse

")



(provide :yhs_can_msgs/l_wheel_fb "9e8be88b3dcd0f2ea8c445a8c67235d0")


