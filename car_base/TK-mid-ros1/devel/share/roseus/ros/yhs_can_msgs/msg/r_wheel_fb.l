;; Auto-generated. Do not edit!


(when (boundp 'yhs_can_msgs::r_wheel_fb)
  (if (not (find-package "YHS_CAN_MSGS"))
    (make-package "YHS_CAN_MSGS"))
  (shadow 'r_wheel_fb (find-package "YHS_CAN_MSGS")))
(unless (find-package "YHS_CAN_MSGS::R_WHEEL_FB")
  (make-package "YHS_CAN_MSGS::R_WHEEL_FB"))

(in-package "ROS")
;;//! \htmlinclude r_wheel_fb.msg.html


(defclass yhs_can_msgs::r_wheel_fb
  :super ros::object
  :slots (_r_wheel_fb_velocity _r_wheel_fb_pulse ))

(defmethod yhs_can_msgs::r_wheel_fb
  (:init
   (&key
    ((:r_wheel_fb_velocity __r_wheel_fb_velocity) 0.0)
    ((:r_wheel_fb_pulse __r_wheel_fb_pulse) 0)
    )
   (send-super :init)
   (setq _r_wheel_fb_velocity (float __r_wheel_fb_velocity))
   (setq _r_wheel_fb_pulse (round __r_wheel_fb_pulse))
   self)
  (:r_wheel_fb_velocity
   (&optional __r_wheel_fb_velocity)
   (if __r_wheel_fb_velocity (setq _r_wheel_fb_velocity __r_wheel_fb_velocity)) _r_wheel_fb_velocity)
  (:r_wheel_fb_pulse
   (&optional __r_wheel_fb_pulse)
   (if __r_wheel_fb_pulse (setq _r_wheel_fb_pulse __r_wheel_fb_pulse)) _r_wheel_fb_pulse)
  (:serialization-length
   ()
   (+
    ;; float32 _r_wheel_fb_velocity
    4
    ;; int32 _r_wheel_fb_pulse
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _r_wheel_fb_velocity
       (sys::poke _r_wheel_fb_velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _r_wheel_fb_pulse
       (write-long _r_wheel_fb_pulse s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _r_wheel_fb_velocity
     (setq _r_wheel_fb_velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _r_wheel_fb_pulse
     (setq _r_wheel_fb_pulse (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get yhs_can_msgs::r_wheel_fb :md5sum-) "554b5bcb0c91910a2cd2cdb9481d63df")
(setf (get yhs_can_msgs::r_wheel_fb :datatype-) "yhs_can_msgs/r_wheel_fb")
(setf (get yhs_can_msgs::r_wheel_fb :definition-)
      "float32    r_wheel_fb_velocity
int32      r_wheel_fb_pulse

")



(provide :yhs_can_msgs/r_wheel_fb "554b5bcb0c91910a2cd2cdb9481d63df")


