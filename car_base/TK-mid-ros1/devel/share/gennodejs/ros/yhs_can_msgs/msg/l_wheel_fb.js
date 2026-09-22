// Auto-generated. Do not edit!

// (in-package yhs_can_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class l_wheel_fb {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.l_wheel_fb_velocity = null;
      this.l_wheel_fb_pulse = null;
    }
    else {
      if (initObj.hasOwnProperty('l_wheel_fb_velocity')) {
        this.l_wheel_fb_velocity = initObj.l_wheel_fb_velocity
      }
      else {
        this.l_wheel_fb_velocity = 0.0;
      }
      if (initObj.hasOwnProperty('l_wheel_fb_pulse')) {
        this.l_wheel_fb_pulse = initObj.l_wheel_fb_pulse
      }
      else {
        this.l_wheel_fb_pulse = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type l_wheel_fb
    // Serialize message field [l_wheel_fb_velocity]
    bufferOffset = _serializer.float32(obj.l_wheel_fb_velocity, buffer, bufferOffset);
    // Serialize message field [l_wheel_fb_pulse]
    bufferOffset = _serializer.int32(obj.l_wheel_fb_pulse, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type l_wheel_fb
    let len;
    let data = new l_wheel_fb(null);
    // Deserialize message field [l_wheel_fb_velocity]
    data.l_wheel_fb_velocity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [l_wheel_fb_pulse]
    data.l_wheel_fb_pulse = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'yhs_can_msgs/l_wheel_fb';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9e8be88b3dcd0f2ea8c445a8c67235d0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32    l_wheel_fb_velocity
    int32      l_wheel_fb_pulse
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new l_wheel_fb(null);
    if (msg.l_wheel_fb_velocity !== undefined) {
      resolved.l_wheel_fb_velocity = msg.l_wheel_fb_velocity;
    }
    else {
      resolved.l_wheel_fb_velocity = 0.0
    }

    if (msg.l_wheel_fb_pulse !== undefined) {
      resolved.l_wheel_fb_pulse = msg.l_wheel_fb_pulse;
    }
    else {
      resolved.l_wheel_fb_pulse = 0
    }

    return resolved;
    }
};

module.exports = l_wheel_fb;
