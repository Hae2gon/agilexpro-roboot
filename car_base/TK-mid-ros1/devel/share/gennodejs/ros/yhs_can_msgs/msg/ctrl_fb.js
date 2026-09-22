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

class ctrl_fb {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ctrl_fb_target_gear = null;
      this.ctrl_fb_linear = null;
      this.ctrl_fb_angular = null;
    }
    else {
      if (initObj.hasOwnProperty('ctrl_fb_target_gear')) {
        this.ctrl_fb_target_gear = initObj.ctrl_fb_target_gear
      }
      else {
        this.ctrl_fb_target_gear = 0;
      }
      if (initObj.hasOwnProperty('ctrl_fb_linear')) {
        this.ctrl_fb_linear = initObj.ctrl_fb_linear
      }
      else {
        this.ctrl_fb_linear = 0.0;
      }
      if (initObj.hasOwnProperty('ctrl_fb_angular')) {
        this.ctrl_fb_angular = initObj.ctrl_fb_angular
      }
      else {
        this.ctrl_fb_angular = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ctrl_fb
    // Serialize message field [ctrl_fb_target_gear]
    bufferOffset = _serializer.uint8(obj.ctrl_fb_target_gear, buffer, bufferOffset);
    // Serialize message field [ctrl_fb_linear]
    bufferOffset = _serializer.float32(obj.ctrl_fb_linear, buffer, bufferOffset);
    // Serialize message field [ctrl_fb_angular]
    bufferOffset = _serializer.float32(obj.ctrl_fb_angular, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ctrl_fb
    let len;
    let data = new ctrl_fb(null);
    // Deserialize message field [ctrl_fb_target_gear]
    data.ctrl_fb_target_gear = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ctrl_fb_linear]
    data.ctrl_fb_linear = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ctrl_fb_angular]
    data.ctrl_fb_angular = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'yhs_can_msgs/ctrl_fb';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '56e80a3321683a07d7ec3d7ab4b9f489';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8    ctrl_fb_target_gear
    float32  ctrl_fb_linear
    float32  ctrl_fb_angular
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ctrl_fb(null);
    if (msg.ctrl_fb_target_gear !== undefined) {
      resolved.ctrl_fb_target_gear = msg.ctrl_fb_target_gear;
    }
    else {
      resolved.ctrl_fb_target_gear = 0
    }

    if (msg.ctrl_fb_linear !== undefined) {
      resolved.ctrl_fb_linear = msg.ctrl_fb_linear;
    }
    else {
      resolved.ctrl_fb_linear = 0.0
    }

    if (msg.ctrl_fb_angular !== undefined) {
      resolved.ctrl_fb_angular = msg.ctrl_fb_angular;
    }
    else {
      resolved.ctrl_fb_angular = 0.0
    }

    return resolved;
    }
};

module.exports = ctrl_fb;
