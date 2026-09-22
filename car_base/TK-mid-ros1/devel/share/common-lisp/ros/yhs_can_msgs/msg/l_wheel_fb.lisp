; Auto-generated. Do not edit!


(cl:in-package yhs_can_msgs-msg)


;//! \htmlinclude l_wheel_fb.msg.html

(cl:defclass <l_wheel_fb> (roslisp-msg-protocol:ros-message)
  ((l_wheel_fb_velocity
    :reader l_wheel_fb_velocity
    :initarg :l_wheel_fb_velocity
    :type cl:float
    :initform 0.0)
   (l_wheel_fb_pulse
    :reader l_wheel_fb_pulse
    :initarg :l_wheel_fb_pulse
    :type cl:integer
    :initform 0))
)

(cl:defclass l_wheel_fb (<l_wheel_fb>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <l_wheel_fb>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'l_wheel_fb)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name yhs_can_msgs-msg:<l_wheel_fb> is deprecated: use yhs_can_msgs-msg:l_wheel_fb instead.")))

(cl:ensure-generic-function 'l_wheel_fb_velocity-val :lambda-list '(m))
(cl:defmethod l_wheel_fb_velocity-val ((m <l_wheel_fb>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader yhs_can_msgs-msg:l_wheel_fb_velocity-val is deprecated.  Use yhs_can_msgs-msg:l_wheel_fb_velocity instead.")
  (l_wheel_fb_velocity m))

(cl:ensure-generic-function 'l_wheel_fb_pulse-val :lambda-list '(m))
(cl:defmethod l_wheel_fb_pulse-val ((m <l_wheel_fb>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader yhs_can_msgs-msg:l_wheel_fb_pulse-val is deprecated.  Use yhs_can_msgs-msg:l_wheel_fb_pulse instead.")
  (l_wheel_fb_pulse m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <l_wheel_fb>) ostream)
  "Serializes a message object of type '<l_wheel_fb>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'l_wheel_fb_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'l_wheel_fb_pulse)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <l_wheel_fb>) istream)
  "Deserializes a message object of type '<l_wheel_fb>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'l_wheel_fb_velocity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'l_wheel_fb_pulse) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<l_wheel_fb>)))
  "Returns string type for a message object of type '<l_wheel_fb>"
  "yhs_can_msgs/l_wheel_fb")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'l_wheel_fb)))
  "Returns string type for a message object of type 'l_wheel_fb"
  "yhs_can_msgs/l_wheel_fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<l_wheel_fb>)))
  "Returns md5sum for a message object of type '<l_wheel_fb>"
  "9e8be88b3dcd0f2ea8c445a8c67235d0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'l_wheel_fb)))
  "Returns md5sum for a message object of type 'l_wheel_fb"
  "9e8be88b3dcd0f2ea8c445a8c67235d0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<l_wheel_fb>)))
  "Returns full string definition for message of type '<l_wheel_fb>"
  (cl:format cl:nil "float32    l_wheel_fb_velocity~%int32      l_wheel_fb_pulse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'l_wheel_fb)))
  "Returns full string definition for message of type 'l_wheel_fb"
  (cl:format cl:nil "float32    l_wheel_fb_velocity~%int32      l_wheel_fb_pulse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <l_wheel_fb>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <l_wheel_fb>))
  "Converts a ROS message object to a list"
  (cl:list 'l_wheel_fb
    (cl:cons ':l_wheel_fb_velocity (l_wheel_fb_velocity msg))
    (cl:cons ':l_wheel_fb_pulse (l_wheel_fb_pulse msg))
))
