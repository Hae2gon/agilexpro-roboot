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

class free_ctrl_cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ctrl_cmd_gear = null;
      this.free_ctrl_cmd_velocity_l = null;
      this.free_ctrl_cmd_velocity_r = null;
    }
    else {
      if (initObj.hasOwnProperty('ctrl_cmd_gear')) {
        this.ctrl_cmd_gear = initObj.ctrl_cmd_gear
      }
      else {
        this.ctrl_cmd_gear = 0;
      }
      if (initObj.hasOwnProperty('free_ctrl_cmd_velocity_l')) {
        this.free_ctrl_cmd_velocity_l = initObj.free_ctrl_cmd_velocity_l
      }
      else {
        this.free_ctrl_cmd_velocity_l = 0.0;
      }
      if (initObj.hasOwnProperty('free_ctrl_cmd_velocity_r')) {
        this.free_ctrl_cmd_velocity_r = initObj.free_ctrl_cmd_velocity_r
      }
      else {
        this.free_ctrl_cmd_velocity_r = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type free_ctrl_cmd
    // Serialize message field [ctrl_cmd_gear]
    bufferOffset = _serializer.uint8(obj.ctrl_cmd_gear, buffer, bufferOffset);
    // Serialize message field [free_ctrl_cmd_velocity_l]
    bufferOffset = _serializer.float32(obj.free_ctrl_cmd_velocity_l, buffer, bufferOffset);
    // Serialize message field [free_ctrl_cmd_velocity_r]
    bufferOffset = _serializer.float32(obj.free_ctrl_cmd_velocity_r, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type free_ctrl_cmd
    let len;
    let data = new free_ctrl_cmd(null);
    // Deserialize message field [ctrl_cmd_gear]
    data.ctrl_cmd_gear = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [free_ctrl_cmd_velocity_l]
    data.free_ctrl_cmd_velocity_l = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [free_ctrl_cmd_velocity_r]
    data.free_ctrl_cmd_velocity_r = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'yhs_can_msgs/free_ctrl_cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '68b83acdb57acb7a34a55dd15082e20e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8    ctrl_cmd_gear
    float32  free_ctrl_cmd_velocity_l
    float32  free_ctrl_cmd_velocity_r
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new free_ctrl_cmd(null);
    if (msg.ctrl_cmd_gear !== undefined) {
      resolved.ctrl_cmd_gear = msg.ctrl_cmd_gear;
    }
    else {
      resolved.ctrl_cmd_gear = 0
    }

    if (msg.free_ctrl_cmd_velocity_l !== undefined) {
      resolved.free_ctrl_cmd_velocity_l = msg.free_ctrl_cmd_velocity_l;
    }
    else {
      resolved.free_ctrl_cmd_velocity_l = 0.0
    }

    if (msg.free_ctrl_cmd_velocity_r !== undefined) {
      resolved.free_ctrl_cmd_velocity_r = msg.free_ctrl_cmd_velocity_r;
    }
    else {
      resolved.free_ctrl_cmd_velocity_r = 0.0
    }

    return resolved;
    }
};

module.exports = free_ctrl_cmd;
