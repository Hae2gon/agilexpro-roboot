;; Auto-generated. Do not edit!


(when (boundp 'yhs_can_msgs::free_ctrl_cmd)
  (if (not (find-package "YHS_CAN_MSGS"))
    (make-package "YHS_CAN_MSGS"))
  (shadow 'free_ctrl_cmd (find-package "YHS_CAN_MSGS")))
(unless (find-package "YHS_CAN_MSGS::FREE_CTRL_CMD")
  (make-package "YHS_CAN_MSGS::FREE_CTRL_CMD"))

(in-package "ROS")
;;//! \htmlinclude free_ctrl_cmd.msg.html


(defclass yhs_can_msgs::free_ctrl_cmd
  :super ros::object
  :slots (_ctrl_cmd_gear _free_ctrl_cmd_velocity_l _free_ctrl_cmd_velocity_r ))

(defmethod yhs_can_msgs::free_ctrl_cmd
  (:init
   (&key
    ((:ctrl_cmd_gear __ctrl_cmd_gear) 0)
    ((:free_ctrl_cmd_velocity_l __free_ctrl_cmd_velocity_l) 0.0)
    ((:free_ctrl_cmd_velocity_r __free_ctrl_cmd_velocity_r) 0.0)
    )
   (send-super :init)
   (setq _ctrl_cmd_gear (round __ctrl_cmd_gear))
   (setq _free_ctrl_cmd_velocity_l (float __free_ctrl_cmd_velocity_l))
   (setq _free_ctrl_cmd_velocity_r (float __free_ctrl_cmd_velocity_r))
   self)
  (:ctrl_cmd_gear
   (&optional __ctrl_cmd_gear)
   (if __ctrl_cmd_gear (setq _ctrl_cmd_gear __ctrl_cmd_gear)) _ctrl_cmd_gear)
  (:free_ctrl_cmd_velocity_l
   (&optional __free_ctrl_cmd_velocity_l)
   (if __free_ctrl_cmd_velocity_l (setq _free_ctrl_cmd_velocity_l __free_ctrl_cmd_velocity_l)) _free_ctrl_cmd_velocity_l)
  (:free_ctrl_cmd_velocity_r
   (&optional __free_ctrl_cmd_velocity_r)
   (if __free_ctrl_cmd_velocity_r (setq _free_ctrl_cmd_velocity_r __free_ctrl_cmd_velocity_r)) _free_ctrl_cmd_velocity_r)
  (:serialization-length
   ()
   (+
    ;; uint8 _ctrl_cmd_gear
    1
    ;; float32 _free_ctrl_cmd_velocity_l
    4
    ;; float32 _free_ctrl_cmd_velocity_r
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _ctrl_cmd_gear
       (write-byte _ctrl_cmd_gear s)
     ;; float32 _free_ctrl_cmd_velocity_l
       (sys::poke _free_ctrl_cmd_velocity_l (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _free_ctrl_cmd_velocity_r
       (sys::poke _free_ctrl_cmd_velocity_r (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _ctrl_cmd_gear
     (setq _ctrl_cmd_gear (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _free_ctrl_cmd_velocity_l
     (setq _free_ctrl_cmd_velocity_l (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _free_ctrl_cmd_velocity_r
     (setq _free_ctrl_cmd_velocity_r (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get yhs_can_msgs::free_ctrl_cmd :md5sum-) "68b83acdb57acb7a34a55dd15082e20e")
(setf (get yhs_can_msgs::free_ctrl_cmd :datatype-) "yhs_can_msgs/free_ctrl_cmd")
(setf (get yhs_can_msgs::free_ctrl_cmd :definition-)
      "uint8    ctrl_cmd_gear
float32  free_ctrl_cmd_velocity_l
float32  free_ctrl_cmd_velocity_r

")



(provide :yhs_can_msgs/free_ctrl_cmd "68b83acdb57acb7a34a55dd15082e20e")


