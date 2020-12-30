# https://www.cs.unc.edu/~gb/blog/2007/02/11/ctypes-tricks/
# http://starship.python.net/crew/theller/ctypes/tutorial.html
"""
quicklink_types.py
.. file: https://github.com/peteristhegreat/ioHub/blob/master/devices/eyeTrackerInterface/HW/EyeTech/QuickLink/ql2types.py

Copyright (C) 2012 EyeTech Inc.
Distributed under the terms of the GNU General Public License (GPL version 3 or any later version).

.. fileauthor:: Eye Tech Inc. & Sol Simpson & Peter Hyatt
"""

from ctypes import *

def is_64bit():
    return sizeof(c_voidp) == 8

QLDeviceId = c_int # QLTypes.h: 316
QLDeviceGroupId = c_int # QLTypes.h: 327
QLDeviceOrGroupId = c_int # QLTypes.h: 341
QLSettingsId = c_int # QLTypes.h: 353
QLCalibrationId = c_int # QLTypes.h: 365
QLTargetId = c_int # QLTypes.h: 377

enum_anon_1 = c_int # QLTypes.h: 402
QL_CALIBRATION_STATUS_OK = 0 # QLTypes.h: 402
QL_CALIBRATION_STATUS_CALIBRATING = 1 # QLTypes.h: 402
QL_CALIBRATION_STATUS_NO_LEFT_DATA = 2 # QLTypes.h: 402
QL_CALIBRATION_STATUS_NO_RIGHT_DATA = 3 # QLTypes.h: 402
QL_CALIBRATION_STATUS_NO_DATA = 4 # QLTypes.h: 402
QLCalibrationStatus = enum_anon_1 # QLTypes.h: 402

def calibrationStatusToString(calStatus):
    return {
        QL_CALIBRATION_STATUS_OK: 'QL_CALIBRATION_STATUS_OK',
        QL_CALIBRATION_STATUS_CALIBRATING: 'QL_CALIBRATION_STATUS_CALIBRATING',
        QL_CALIBRATION_STATUS_NO_LEFT_DATA: 'QL_CALIBRATION_STATUS_NO_LEFT_DATA',
        QL_CALIBRATION_STATUS_NO_RIGHT_DATA: 'QL_CALIBRATION_STATUS_NO_RIGHT_DATA',
        QL_CALIBRATION_STATUS_NO_DATA: 'QL_CALIBRATION_STATUS_NO_DATA',
    }[calStatus]

enum_anon_2 = c_int # QLTypes.h: 421
QL_CALIBRATION_TYPE_5 = 0 # QLTypes.h: 421
QL_CALIBRATION_TYPE_9 = 1 # QLTypes.h: 421
QL_CALIBRATION_TYPE_16 = 2 # QLTypes.h: 421
QLCalibrationType = enum_anon_2 # QLTypes.h: 421

def calibrationTypeToString(calType):
    return {
        QL_CALIBRATION_TYPE_5: 'QL_CALIBRATION_TYPE_5',
        QL_CALIBRATION_TYPE_9: 'QL_CALIBRATION_TYPE_9',
        QL_CALIBRATION_TYPE_16: 'QL_CALIBRATION_TYPE_16',
    }[calType]

enum_anon_3 = c_int # QLTypes.h: 439
QL_DEVICE_BANDWIDTH_MODE_AUTO = 0 # QLTypes.h: 439
QL_DEVICE_BANDWIDTH_MODE_MANUAL = 1 # QLTypes.h: 439
QLDeviceBandwidthMode = enum_anon_3 # QLTypes.h: 439

def bandwidthModeToString(bandwidthMode):
    return {
        QL_DEVICE_BANDWIDTH_MODE_AUTO: 'QL_DEVICE_BANDWIDTH_MODE_AUTO',
        QL_DEVICE_BANDWIDTH_MODE_MANUAL: 'QL_DEVICE_BANDWIDTH_MODE_MANUAL',
    }[bandwidthMode]

enum_anon_4 = c_int # QLTypes.h: 463
QL_DEVICE_EYES_TO_USE_LEFT = 0 # QLTypes.h: 463
QL_DEVICE_EYES_TO_USE_RIGHT = 1 # QLTypes.h: 463
QL_DEVICE_EYES_TO_USE_LEFT_OR_RIGHT = 2 # QLTypes.h: 463
QL_DEVICE_EYES_TO_USE_LEFT_AND_RIGHT = 3 # QLTypes.h: 463
QLDeviceEyesToUse = enum_anon_4 # QLTypes.h: 463

def eyesToUseToString(eyes_to_use):
    return {
        QL_DEVICE_EYES_TO_USE_LEFT: 'QL_DEVICE_EYES_TO_USE_LEFT',
        QL_DEVICE_EYES_TO_USE_RIGHT: 'QL_DEVICE_EYES_TO_USE_RIGHT',
        QL_DEVICE_EYES_TO_USE_LEFT_OR_RIGHT: 'QL_DEVICE_EYES_TO_USE_LEFT_OR_RIGHT',
        QL_DEVICE_EYES_TO_USE_LEFT_AND_RIGHT: 'QL_DEVICE_EYES_TO_USE_LEFT_AND_RIGHT',
    }[eyes_to_use]

enum_anon_5 = c_int # QLTypes.h: 480
QL_DEVICE_GAIN_MODE_AUTO = 0 # QLTypes.h: 480
QL_DEVICE_GAIN_MODE_MANUAL = 1 # QLTypes.h: 480
QLDeviceGainMode = enum_anon_5 # QLTypes.h: 480

def gainModeToString(gain_mode):
    return {
        QL_DEVICE_GAIN_MODE_AUTO: 'QL_DEVICE_GAIN_MODE_AUTO',
        QL_DEVICE_GAIN_MODE_MANUAL: 'QL_DEVICE_GAIN_MODE_MANUAL',
    }[gain_mode]

enum_anon_6 = c_int # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_NONE = 0 # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_FRAMES = 1 # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_TIME = 2 # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_FRAMES = 3 # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_TIME = 4 # QLTypes.h: 537
QL_DEVICE_GAZE_POINT_FILTER_WEIGHTED_PREVIOUS_FRAME = 5 # QLTypes.h: 537
QLDeviceGazePointFilterMode = enum_anon_6 # QLTypes.h: 537

def gazePointFilterModeToString(filter_mode):
    return {
        QL_DEVICE_GAZE_POINT_FILTER_NONE: 'QL_DEVICE_GAZE_POINT_FILTER_NONE',
        QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_FRAMES: 'QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_FRAMES',
        QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_TIME: 'QL_DEVICE_GAZE_POINT_FILTER_MEDIAN_TIME',
        QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_FRAMES: 'QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_FRAMES',
        QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_TIME: 'QL_DEVICE_GAZE_POINT_FILTER_HEURISTIC_TIME',
        QL_DEVICE_GAZE_POINT_FILTER_WEIGHTED_PREVIOUS_FRAME: 'QL_DEVICE_GAZE_POINT_FILTER_WEIGHTED_PREVIOUS_FRAME',
    }[filter_mode]

enum_anon_7 = c_int # QLTypes.h: 554
QL_DEVICE_IR_LIGHT_MODE_OFF = 0 # QLTypes.h: 554
QL_DEVICE_IR_LIGHT_MODE_AUTO = 1 # QLTypes.h: 554
QLDeviceIRLightMode = enum_anon_7 # QLTypes.h: 554

def irLightModeToString(irLightMode):
    return {
        QL_DEVICE_IR_LIGHT_MODE_OFF: 'QL_DEVICE_IR_LIGHT_MODE_OFF',
        QL_DEVICE_IR_LIGHT_MODE_AUTO: 'QL_DEVICE_IR_LIGHT_MODE_AUTO',
    }

enum_anon_8 = c_int # QLTypes.h: 576
QL_DEVICE_STATUS_UNAVAILABLE = 0 # QLTypes.h: 576
QL_DEVICE_STATUS_STOPPED = 1 # QLTypes.h: 576
QL_DEVICE_STATUS_INITIALIZED = 2 # QLTypes.h: 576
QL_DEVICE_STATUS_STARTED = 3 # QLTypes.h: 576
QLDeviceStatus = enum_anon_8 # QLTypes.h: 576

def deviceStatusToString(device_status):
    return {
        QL_DEVICE_STATUS_UNAVAILABLE: 'QL_DEVICE_STATUS_UNAVAILABLE',
        QL_DEVICE_STATUS_STOPPED: 'QL_DEVICE_STATUS_STOPPED',
        QL_DEVICE_STATUS_INITIALIZED: 'QL_DEVICE_STATUS_INITIALIZED',
        QL_DEVICE_STATUS_STARTED: 'QL_DEVICE_STATUS_STARTED',
    }[device_status]

enum_anon_9 = c_int # QLTypes.h: 640
QL_ERROR_OK = 0 # QLTypes.h: 640
QL_ERROR_INVALID_DEVICE_ID = 1 # QLTypes.h: 640
QL_ERROR_INVALID_SETTINGS_ID = 2 # QLTypes.h: 640
QL_ERROR_INVALID_CALIBRATION_ID = 3 # QLTypes.h: 640
QL_ERROR_INVALID_TARGET_ID = 4 # QLTypes.h: 640
QL_ERROR_INVALID_PASSWORD = 5 # QLTypes.h: 640
QL_ERROR_INVALID_PATH = 6 # QLTypes.h: 640
QL_ERROR_INVALID_DURATION = 7 # QLTypes.h: 640
QL_ERROR_INVALID_POINTER = 8 # QLTypes.h: 640
QL_ERROR_TIMEOUT_ELAPSED = 9 # QLTypes.h: 640
QL_ERROR_INTERNAL_ERROR = 10 # QLTypes.h: 640
QL_ERROR_BUFFER_TOO_SMALL = 11 # QLTypes.h: 640
QL_ERROR_CALIBRAION_NOT_INITIALIZED = 12 # QLTypes.h: 640
QL_ERROR_DEVICE_NOT_STARTED = 13 # QLTypes.h: 640
QL_ERROR_NOT_SUPPORTED = 14 # QLTypes.h: 640
QL_ERROR_NOT_FOUND = 15 # QLTypes.h: 640
QL_ERROR_UNAUTHORIZED_APPLICATION_RUNNING = 16 # QLTypes.h: 640
QL_ERROR_INVALID_DEVICE_GROUP_ID = 17 # QLTypes.h: 640
QLError = enum_anon_9 # QLTypes.h: 640

def errorToString(qlerror):
    return {
        QL_ERROR_INVALID_DEVICE_ID: 'QL_ERROR_INVALID_DEVICE_ID',
        QL_ERROR_INVALID_SETTINGS_ID: 'QL_ERROR_INVALID_SETTINGS_ID',
        QL_ERROR_INVALID_CALIBRATION_ID: 'QL_ERROR_INVALID_CALIBRATION_ID',
        QL_ERROR_INVALID_TARGET_ID: 'QL_ERROR_INVALID_TARGET_ID',
        QL_ERROR_INVALID_PASSWORD: 'QL_ERROR_INVALID_PASSWORD',
        QL_ERROR_INVALID_PATH: 'QL_ERROR_INVALID_PATH',
        QL_ERROR_INVALID_DURATION: 'QL_ERROR_INVALID_DURATION',
        QL_ERROR_INVALID_POINTER: 'QL_ERROR_INVALID_POINTER',
        QL_ERROR_TIMEOUT_ELAPSED: 'QL_ERROR_TIMEOUT_ELAPSED',
        QL_ERROR_INTERNAL_ERROR: 'QL_ERROR_INTERNAL_ERROR',
        QL_ERROR_BUFFER_TOO_SMALL: 'QL_ERROR_BUFFER_TOO_SMALL',
        QL_ERROR_CALIBRAION_NOT_INITIALIZED: 'QL_ERROR_CALIBRAION_NOT_INITIALIZED',
        QL_ERROR_DEVICE_NOT_STARTED: 'QL_ERROR_DEVICE_NOT_STARTED',
        QL_ERROR_NOT_SUPPORTED: 'QL_ERROR_NOT_SUPPORTED',
        QL_ERROR_NOT_FOUND: 'QL_ERROR_NOT_FOUND',
        QL_ERROR_UNAUTHORIZED_APPLICATION_RUNNING: 'QL_ERROR_UNAUTHORIZED_APPLICATION_RUNNING',
        QL_ERROR_INVALID_DEVICE_GROUP_ID: 'QL_ERROR_INVALID_DEVICE_GROUP_ID',
    }[qlerror]

enum_anon_10 = c_int # QLTypes.h: 657
QL_EYE_TYPE_LEFT = 0 # QLTypes.h: 657
QL_EYE_TYPE_RIGHT = 1 # QLTypes.h: 657
QLEyeType = enum_anon_10 # QLTypes.h: 657

def eyeTypeToString(eyeType):
    return {
        QL_EYE_TYPE_LEFT: 'QL_EYE_TYPE_LEFT',
        QL_EYE_TYPE_RIGHT: 'QL_EYE_TYPE_RIGHT',
    }[eyeType]

enum_anon_11 = c_int # QLTypes.h: 688
QL_INDICATOR_MODE_OFF = 0 # QLTypes.h: 688
QL_INDICATOR_MODE_ON = 1 # QLTypes.h: 688
QL_INDICATOR_MODE_LEFT_EYE_STATUS = 2 # QLTypes.h: 688
QL_INDICATOR_MODE_RIGHT_EYE_STATUS = 3 # QLTypes.h: 688
QL_INDICATOR_MODE_LEFT_EYE_STATUS_FILTERED = 4 # QLTypes.h: 688
QL_INDICATOR_MODE_RIGHT_EYE_STATUS_FILTERED = 5 # QLTypes.h: 688
QLIndicatorMode = enum_anon_11 # QLTypes.h: 688

def indicatorModeToString(indicator_mode):
    return {
        QL_INDICATOR_MODE_OFF: 'QL_INDICATOR_MODE_OFF',
        QL_INDICATOR_MODE_ON: 'QL_INDICATOR_MODE_ON',
        QL_INDICATOR_MODE_LEFT_EYE_STATUS: 'QL_INDICATOR_MODE_LEFT_EYE_STATUS',
        QL_INDICATOR_MODE_RIGHT_EYE_STATUS: 'QL_INDICATOR_MODE_RIGHT_EYE_STATUS',
        QL_INDICATOR_MODE_LEFT_EYE_STATUS_FILTERED: 'QL_INDICATOR_MODE_LEFT_EYE_STATUS_FILTERED',
        QL_INDICATOR_MODE_RIGHT_EYE_STATUS_FILTERED: 'QL_INDICATOR_MODE_RIGHT_EYE_STATUS_FILTERED',
    }[indicator_mode]

enum_anon_12 = c_int # QLTypes.h: 705
QL_INDICATOR_TYPE_LEFT = 0 # QLTypes.h: 705
QL_INDICATOR_TYPE_RIGHT = 1 # QLTypes.h: 705
QLIndicatorType = enum_anon_12 # QLTypes.h: 705

def indicatorTypeToString(indicator_type):
    return {
        QL_INDICATOR_TYPE_LEFT: 'QL_INDICATOR_TYPE_LEFT',
        QL_INDICATOR_TYPE_RIGHT: 'QL_INDICATOR_TYPE_RIGHT',
    }[indicator_type]

enum_anon_13 = c_int # QLTypes.h: 761
QL_SETTING_TYPE_INT = 0 # QLTypes.h: 761
QL_SETTING_TYPE_INT8 = 1 # QLTypes.h: 761
QL_SETTING_TYPE_INT16 = 2 # QLTypes.h: 761
QL_SETTING_TYPE_INT32 = 3 # QLTypes.h: 761
QL_SETTING_TYPE_INT64 = 4 # QLTypes.h: 761
QL_SETTING_TYPE_UINT = 5 # QLTypes.h: 761
QL_SETTING_TYPE_UINT8 = 6 # QLTypes.h: 761
QL_SETTING_TYPE_UINT16 = 7 # QLTypes.h: 761
QL_SETTING_TYPE_UINT32 = 8 # QLTypes.h: 761
QL_SETTING_TYPE_UINT64 = 9 # QLTypes.h: 761
QL_SETTING_TYPE_FLOAT = 10 # QLTypes.h: 761
QL_SETTING_TYPE_DOUBLE = 11 # QLTypes.h: 761
QL_SETTING_TYPE_BOOL = 12 # QLTypes.h: 761
QL_SETTING_TYPE_STRING = 13 # QLTypes.h: 761
QL_SETTING_TYPE_VOID_POINTER = 14 # QLTypes.h: 761
QLSettingType = enum_anon_13 # QLTypes.h: 761

def settingTypeToString(setting_type):
    return {
        QL_SETTING_TYPE_INT: 'QL_SETTING_TYPE_INT',
        QL_SETTING_TYPE_INT8: 'QL_SETTING_TYPE_INT8',
        QL_SETTING_TYPE_INT16: 'QL_SETTING_TYPE_INT16',
        QL_SETTING_TYPE_INT32: 'QL_SETTING_TYPE_INT32',
        QL_SETTING_TYPE_INT64: 'QL_SETTING_TYPE_INT64',
        QL_SETTING_TYPE_UINT: 'QL_SETTING_TYPE_UINT',
        QL_SETTING_TYPE_UINT8: 'QL_SETTING_TYPE_UINT8',
        QL_SETTING_TYPE_UINT16: 'QL_SETTING_TYPE_UINT16',
        QL_SETTING_TYPE_UINT32: 'QL_SETTING_TYPE_UINT32',
        QL_SETTING_TYPE_UINT64: 'QL_SETTING_TYPE_UINT64',
        QL_SETTING_TYPE_FLOAT: 'QL_SETTING_TYPE_FLOAT',
        QL_SETTING_TYPE_DOUBLE: 'QL_SETTING_TYPE_DOUBLE',
        QL_SETTING_TYPE_BOOL: 'QL_SETTING_TYPE_BOOL',
        QL_SETTING_TYPE_STRING: 'QL_SETTING_TYPE_STRING',
        QL_SETTING_TYPE_VOID_POINTER: 'QL_SETTING_TYPE_VOID_POINTER',
    }[setting_type]

# QLTypes.h: 788
class struct_anon_14(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_14.__slots__ = [
    'targetId',
    'x',
    'y',
]
struct_anon_14._fields_ = [
    ('targetId', QLTargetId),
    ('x', c_float),
    ('y', c_float),
]

QLCalibrationTarget = struct_anon_14 # QLTypes.h: 788

# QLTypes.h: 812
class struct_anon_15(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_15.__slots__ = [
    'x',
    'y',
    'score',
]
struct_anon_15._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('score', c_float),
]

QLCalibrationScore = struct_anon_15 # QLTypes.h: 812

# QLTypes.h: 834
class struct_anon_16(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_16.__slots__ = [
    'sensorWidth',
    'sensorHeight',
    'serialNumber',
    'modelName',
]
struct_anon_16._fields_ = [
    ('sensorWidth', c_int),
    ('sensorHeight', c_int),
    ('serialNumber', c_char * 128),
    ('modelName', c_char * 128),
]
QLDeviceInfo = struct_anon_16 # QLTypes.h: 834

def infoToString(info):
    return "Model:\t" + info.modelName.decode("utf-8") \
        + "\nSN:\t" + info.serialNumber.decode("utf-8") \
        +"\nSensor:\t" + str(info.sensorWidth) + "x" + str(info.sensorHeight)

# QLTypes.h: 845
class struct_anon_17(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_17.__slots__ = [
    'x',
    'y',
]
struct_anon_17._fields_ = [
    ('x', c_double),
    ('y', c_double),
]

QLXYPairDouble = struct_anon_17 # QLTypes.h: 845

# QLTypes.h: 856
class struct_anon_18(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_18.__slots__ = [
    'x',
    'y',
]
struct_anon_18._fields_ = [
    ('x', c_float),
    ('y', c_float),
]

QLXYPairFloat = struct_anon_18 # QLTypes.h: 856

# QLTypes.h: 876
class struct_anon_19(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_19.__slots__ = [
    'x',
    'y',
    'width',
    'height',
]
struct_anon_19._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
]

QLRectInt = struct_anon_19 # QLTypes.h: 876

def rectToString(rect):
    return str(rect.x) + ',' + str(rect.y) + ' ' \
        + str(rect.width) + 'x' + str(rect.height)

# QLTypes.h: 920
class struct_anon_20(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'


struct_anon_20.__slots__ = [
    'PixelData',
    'Width',
    'Height',
    'Timestamp',
    'Gain',
    'FrameNumber',
    'ROI',
    'Reserved',
]

if(is_64bit()):
    struct_anon_20._fields_ = [
        ('PixelData', POINTER(c_ubyte)),
        ('Width', c_int),
        ('Height', c_int),
        ('Timestamp', c_double),
        ('Gain', c_int),
        ('FrameNumber', c_long),
        ('ROI', QLRectInt),
        #('Reserved', POINTER(None) * 12),#32 bit version # POINTER(None) = 4 bytes, 32 bits
        ('Reserved', POINTER(None) * 14),#64 bit version # POINTER(None) = 8 bytes, 64 bits
    ]
else:
    struct_anon_20._fields_ = [
        ('PixelData', POINTER(c_ubyte)),
        ('Width', c_int),
        ('Height', c_int),
        ('Timestamp', c_double),
        ('Gain', c_int),
        ('FrameNumber', c_long),
        ('ROI', QLRectInt),
        ('Reserved', POINTER(None) * 12),#32 bit version # POINTER(None) = 4 bytes, 32 bits
        #('Reserved', POINTER(None) * 14),#64 bit version # POINTER(None) = 8 bytes, 64 bits
    ]

QLImageData = struct_anon_20 # QLTypes.h: 920

def imageDataToString(img_data):
    return ' PixelData:\t' + str(img_data.PixelData) \
        + '\n Size:\t' + str(img_data.Width) + 'x' + str(img_data.Height) \
        + '\n Timestamp:\t' + "{0:.2f}".format(img_data.Timestamp) \
        + '\n Gain:\t' + str(img_data.Gain) \
        + '\n FrameNumber:\t' + str(img_data.FrameNumber) \
        + '\n ROI:\t' + rectToString(img_data.ROI)
        #+ '\n Reserved:\t' + str(img_data.Reserved)#img_data.Reserved.decode("utf-8")
        

# QLTypes.h: 959
class struct_anon_21(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_21.__slots__ = [
    'Found',
    'Calibrated',
    'PupilDiameter',
    'Pupil',
    'Glint0',
    'Glint1',
    'GazePoint',
    'Reserved',
]
struct_anon_21._fields_ = [
    ('Found', c_bool),
    ('Calibrated', c_bool),
    ('PupilDiameter', c_float),
    ('Pupil', QLXYPairFloat),
    ('Glint0', QLXYPairFloat),
    ('Glint1', QLXYPairFloat),
    ('GazePoint', QLXYPairFloat),
    ('Reserved', POINTER(None) * 16),
]

QLEyeData = struct_anon_21 # QLTypes.h: 959

def eyeDataToString(eye_data):
    return str(eye_data.Found) + " " \
        + "{0:.2f}".format(eye_data.Pupil.x) + "," \
        + "{0:.2f}".format(eye_data.Pupil.y)

# QLTypes.h: 988
class struct_anon_22(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + ','.join(res) + ')'

struct_anon_22.__slots__ = [
    'Valid',
    'x',
    'y',
    'LeftWeight',
    'RightWeight',
    'Reserved',
]
struct_anon_22._fields_ = [
    ('Valid', c_bool),
    ('x', c_float),
    ('y', c_float),
    ('LeftWeight', c_float),
    ('RightWeight', c_float),
    ('Reserved', POINTER(None) * 16),
]

QLWeightedGazePoint = struct_anon_22 # QLTypes.h: 988

def weightedGazePointToString(wgp):
    return ' Valid:\t' + str(wgp.Valid) \
        + '\n x:\t' + str(wgp.x) \
        + '\n y:\t' + str(wgp.y)

# QLTypes.h: 1033
class struct_anon_23(Structure):
    def __repr__(self):
        '''Print the fields'''
        res = []
        for field in self._fields_:
            res.append('%s=%s' % (field[0], repr(getattr(self, field[0]))))
        return self.__class__.__name__ + '(' + '\n'.join(res) + ')'

struct_anon_23.__slots__ = [
    'ImageData',
    'LeftEye',
    'RightEye',
    'WeightedGazePoint',
    'Focus',
    'Distance',
    'Bandwidth',
    'DeviceId',
    'Reserved',
]
struct_anon_23._fields_ = [
    ('ImageData', QLImageData), # works
    ('LeftEye', QLEyeData),
    ('RightEye', QLEyeData),
    ('WeightedGazePoint', QLWeightedGazePoint),
    ('Focus', c_float),
    ('Distance', c_float),
    ('Bandwidth', c_int),
    ('DeviceId', QLDeviceId),
    ('Reserved', POINTER(None) * 14),
]

QLFrameData = struct_anon_23 # QLTypes.h: 1033

def frameDataToString(frame):
    return 'ImageData:\t' + imageDataToString(frame.ImageData) \
        + '\nLeftEye:\t' + eyeDataToString(frame.LeftEye) \
        + '\nRightEye:\t' + eyeDataToString(frame.RightEye) \
        + '\nGazePoint:\t' + weightedGazePointToString(frame.WeightedGazePoint) \
        + '\nFocus:\t' + "{0:.2f}".format(frame.Focus) \
        + '\nDistance:\t' + "{0:.2f}".format(frame.Distance) \
        + '\nBandwidth:\t' + str(frame.Bandwidth) \
        + '\nDeviceId:\t' + str(frame.DeviceId)
        

__const = c_int # <command-line>: 5

# <command-line>: 8
try:
    CTYPESGEN = 1
except:
    pass

# QLTypes.h: 19
try:
    STRING_LENGTH_128 = 128
except:
    pass

# QLTypes.h: 58
try:
    QL_SETTING_DEVICE_BANDWIDTH_MODE = 'DeviceBandwidthMode'
except:
    pass

# QLTypes.h: 69
try:
    QL_SETTING_DEVICE_BANDWIDTH_PERCENT_FULL = 'DeviceBandwidthPercentFull'
except:
    pass

# QLTypes.h: 80
try:
    QL_SETTING_DEVICE_BANDWIDTH_PERCENT_TRACKING = 'DeviceBandwidthPercentTracking'
except:
    pass

# QLTypes.h: 92
try:
    QL_SETTING_DEVICE_BINNING = 'DeviceBinning'
except:
    pass

# QLTypes.h: 102
try:
    QL_SETTING_DEVICE_CALIBRATE_ENABLED = 'DeviceCalibrateEnabled'
except:
    pass

# QLTypes.h: 109
try:
    QL_SETTING_DEVICE_DISTANCE = 'DeviceDistance'
except:
    pass

# QLTypes.h: 116
try:
    QL_SETTING_DEVICE_EXPOSURE = 'DeviceExposure'
except:
    pass

# QLTypes.h: 127
try:
    QL_SETTING_DEVICE_FLIP_X = 'DeviceFlipX'
except:
    pass

# QLTypes.h: 138
try:
    QL_SETTING_DEVICE_FLIP_Y = 'DeviceFlipY'
except:
    pass

# QLTypes.h: 148
try:
    QL_SETTING_DEVICE_GAIN_MODE = 'DeviceGainMode'
except:
    pass

# QLTypes.h: 159
try:
    QL_SETTING_DEVICE_GAIN_VALUE = 'DeviceGainValue'
except:
    pass

# QLTypes.h: 169
try:
    QL_SETTING_DEVICE_GAZE_POINT_FILTER_MODE = 'DeviceGazePointFilterMode'
except:
    pass

# QLTypes.h: 179
try:
    QL_SETTING_DEVICE_GAZE_POINT_FILTER_VALUE = 'DeviceGazePointFilterValue'
except:
    pass

# QLTypes.h: 189
try:
    QL_SETTING_DEVICE_IMAGE_PROCESSING_ENABLED = 'DeviceImageProcessingEnabled'
except:
    pass

# QLTypes.h: 198
try:
    QL_SETTING_DEVICE_IMAGE_PROCESSING_EYES_TO_FIND = 'DeviceImageProcessingEyesToUse'
except:
    pass

# QLTypes.h: 211
try:
    QL_SETTING_DEVICE_IMAGE_PROCESSING_EYE_RADIUS_LEFT = 'DeviceImageProcessingEyeRadiusLeft'
except:
    pass

# QLTypes.h: 224
try:
    QL_SETTING_DEVICE_IMAGE_PROCESSING_EYE_RADIUS_RIGHT = 'DeviceImageProcessingEyeRadiusRight'
except:
    pass

# QLTypes.h: 234
try:
    QL_SETTING_DEVICE_INTERPOLATE_ENABLED = 'DeviceInterpolateEnabled'
except:
    pass

# QLTypes.h: 242
try:
    QL_SETTING_DEVICE_IR_LIGHT_MODE = 'DeviceIRLightMode'
except:
    pass

# QLTypes.h: 249
try:
    QL_SETTING_DEVICE_LENS_FOCAL_LENGTH = 'DeviceLensFocalLength'
except:
    pass

# QLTypes.h: 260
try:
    QL_SETTING_DEVICE_ROI_MOVE_THRESHOLD_PERCENT_X = 'DeviceRoiMoveThresholdPercentX'
except:
    pass

# QLTypes.h: 271
try:
    QL_SETTING_DEVICE_ROI_MOVE_THRESHOLD_PERCENT_Y = 'DeviceRoiMoveThresholdPercentY'
except:
    pass

# QLTypes.h: 281
try:
    QL_SETTING_DEVICE_ROI_SIZE_PERCENT_X = 'DeviceRoiSizePercentX'
except:
    pass

# QLTypes.h: 291
try:
    QL_SETTING_DEVICE_ROI_SIZE_PERCENT_Y = 'DeviceRoiSizePercentY'
except:
    pass

try:
    QL_SETTING_DEVICE_DOWNSAMPLE_SCALE_FACTOR = "DeviceDownsampleScaleFactor"
except: 
    pass
# No inserted files

# if __name__ == "__main__":
#     from quicklink2 import main
#     main()