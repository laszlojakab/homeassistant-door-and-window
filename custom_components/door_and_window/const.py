"""Define window and door device integration constants."""
DOMAIN = "door_and_window"

TYPE_DOOR = 'door'
TYPE_WINDOW = 'window'

HORIZON_PROFILE_TYPE_STATIC = 'static'
HORIZON_PROFILE_TYPE_DYNAMIC = 'dynamic'

CONF_TYPE = "type"
CONF_MANUFACTURER = "manufacturer"
CONF_MODEL = "model"

# dimensions
CONF_WIDTH = "width"
CONF_HEIGHT = "height"
CONF_INSIDE_DEPTH = "inside_depth"
CONF_OUTSIDE_DEPTH = "outside_depth"
CONF_FRAME_THICKNESS = "frame_thickness"
CONF_FRAME_FACE_THICKNESS = "frame_face_thickness"
CONF_PARAPET_WALL_HEIGHT = "parapet_wall_height"

# facing
CONF_TILT = "tilt"
CONF_AZIMUTH = "azimuth"

# horizon profile
CONF_HORIZON_PROFILE = "horizon_profile"
CONF_HORIZON_PROFILE_TYPE = "horizon_profile_type"
CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS = "horizon_profile_number_of_measurements"
CONF_HORIZON_PROFILE_ENTITY = "horizon_profile_entity"

# awning
CONF_HAS_AWNING = "has_awning"
CONF_AWNING_MIN_DEPTH = "awning_min_depth"
CONF_AWNING_MAX_DEPTH = "awning_max_depth"
CONF_AWNING_LEFT_DISTANCE = "awning_left_distance"
CONF_AWNING_RIGHT_DISTANCE = "awning_right_distance"
CONF_AWNING_CLOSEST_TOP = "awning_closest_top"
CONF_AWNING_FARTHEST_TOP = "awning_farthest_top"
CONF_AWNING_DISTANCE = "awning_distance"
CONF_AWNING_COVER_ENTITY = "awning_cover_entity"
