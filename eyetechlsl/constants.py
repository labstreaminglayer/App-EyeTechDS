QUICKLINK_POLL_TIME_MS = 500
DEFAULT_CONFIG_FILENAME = 'config'
EXAMPLE_CONFIG_FILENAME = 'config.example'
SDK_URL = "https://eyetechds.com/developer-corner/software-downloads/quicklink2-sdk-download/"

# Based on http://answers.eyetechds.com/questions/520/quick-capture-data-format
CHANNEL_METADATA = [
    {'label': 'LeftEye_Found',                  'eye': 'left', 'type':  'Confidence',  'unit': 'normalized'},
    {'label': 'LeftEye_Calibrated',             'eye': 'left', 'type':  'Confidence',  'unit': 'normalized'},
    {'label': 'LeftEye_PupilDiameter',          'eye': 'left', 'type':  'Diameter',    'unit': 'mm'},
    {'label': 'LeftEye_Pupil_X',                'eye': 'left', 'type':  'PupilX',      'unit': 'pixels'},
    {'label': 'LeftEye_Pupil_Y',                'eye': 'left', 'type':  'PupilY',      'unit': 'pixels'},
    {'label': 'LeftEye_Glint0_X',               'eye': 'left', 'type':  'ReflexX',     'unit': 'pixels'},
    {'label': 'LeftEye_Glint0_Y',               'eye': 'left', 'type':  'ReflexY',     'unit': 'pixels'},
    {'label': 'LeftEye_Glint1_X',               'eye': 'left', 'type':  'ReflexX',     'unit': 'pixels'},
    {'label': 'LeftEye_Glint1_Y',               'eye': 'left', 'type':  'ReflexY',     'unit': 'pixels'},
    {'label': 'LeftEye_GazePoint_X',            'eye': 'left', 'type':  'ScreenX',     'unit': 'percent'},
    {'label': 'LeftEye_GazePoint_Y',            'eye': 'left', 'type':  'ScreenY',     'unit': 'percent'},

    {'label': 'RightEye_Found',                 'eye': 'right', 'type': 'Confidence',  'unit': 'normalized'},
    {'label': 'RightEye_Calibrated',            'eye': 'right', 'type': 'Confidence',  'unit': 'normalized'},
    {'label': 'RightEye_PupilDiameter',         'eye': 'right', 'type': 'Diameter',    'unit': 'mm'},
    {'label': 'RightEye_Pupil_X',               'eye': 'right', 'type': 'PupilX',      'unit': 'pixels'},
    {'label': 'RightEye_Pupil_Y',               'eye': 'right', 'type': 'PupilY',      'unit': 'pixels'},
    {'label': 'RightEye_Glint0_X',              'eye': 'right', 'type': 'ReflexX',     'unit': 'pixels'},
    {'label': 'RightEye_Glint0_Y',              'eye': 'right', 'type': 'ReflexY',     'unit': 'pixels'},
    {'label': 'RightEye_Glint1_X',              'eye': 'right', 'type': 'ReflexX',     'unit': 'pixels'},
    {'label': 'RightEye_Glint1_Y',              'eye': 'right', 'type': 'ReflexY',     'unit': 'pixels'},
    {'label': 'RightEye_GazePoint_X',           'eye': 'right', 'type': 'ScreenY',     'unit': 'percent'},
    {'label': 'RightEye_GazePoint_Y',           'eye': 'right', 'type': 'ScreenY',     'unit': 'percent'},

    {'label': 'WeightedGazePoint_Valid',        'eye': 'both', 'type':  'Confidence',  'unit': 'normalized'},
    {'label': 'WeightedGazePoint_X',            'eye': 'both', 'type':  'ScreenX',     'unit': 'percent'},
    {'label': 'WeightedGazePoint_Y',            'eye': 'both', 'type':  'ScreenY',     'unit': 'percent'},
    {'label': 'WeightedGazePoint_LeftWeight',   'eye': 'both', 'type':  'Other',       'unit': 'normalized' },
    {'label': 'WeightedGazePoint_RightWeight',  'eye': 'both', 'type':  'Other',       'unit': 'normalized' },
    {'label': 'Focus',                          'eye': 'both', 'type':  'Other',       'unit': 'unspecified'},
    {'label': 'Distance',                       'eye': 'both', 'type':  'Distance',    'unit': 'mm'},
]

CHANNEL_NAMES = [ch['label'] for ch in CHANNEL_METADATA]
