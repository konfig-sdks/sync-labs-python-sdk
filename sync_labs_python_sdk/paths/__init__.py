# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sync_labs_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    VIDEO_COST = "/video/cost"
    VIDEO = "/video"
    VIDEO_ID = "/video/{id}"
    LIPSYNC_COST = "/lipsync/cost"
    LIPSYNC = "/lipsync"
    LIPSYNC_ID = "/lipsync/{id}"
    VOICES = "/voices"
    TRANSLATE_COST = "/translate/cost"
    TRANSLATE = "/translate"
    TRANSLATE_ID = "/translate/{id}"
    SPEAK_COST = "/speak/cost"
    SPEAK = "/speak"
    SPEAK_ID = "/speak/{id}"
    ANIMATE_COST = "/animate/cost"
    ANIMATE = "/animate"
    ANIMATE_ID = "/animate/{id}"
