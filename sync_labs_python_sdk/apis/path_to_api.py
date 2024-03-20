import typing_extensions

from sync_labs_python_sdk.paths import PathValues
from sync_labs_python_sdk.apis.paths.video_cost import VideoCost
from sync_labs_python_sdk.apis.paths.video import Video
from sync_labs_python_sdk.apis.paths.video_id import VideoId
from sync_labs_python_sdk.apis.paths.lipsync_cost import LipsyncCost
from sync_labs_python_sdk.apis.paths.lipsync import Lipsync
from sync_labs_python_sdk.apis.paths.lipsync_id import LipsyncId
from sync_labs_python_sdk.apis.paths.voices import Voices
from sync_labs_python_sdk.apis.paths.translate_cost import TranslateCost
from sync_labs_python_sdk.apis.paths.translate import Translate
from sync_labs_python_sdk.apis.paths.translate_id import TranslateId
from sync_labs_python_sdk.apis.paths.speak_cost import SpeakCost
from sync_labs_python_sdk.apis.paths.speak import Speak
from sync_labs_python_sdk.apis.paths.speak_id import SpeakId
from sync_labs_python_sdk.apis.paths.animate_cost import AnimateCost
from sync_labs_python_sdk.apis.paths.animate import Animate
from sync_labs_python_sdk.apis.paths.animate_id import AnimateId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VIDEO_COST: VideoCost,
        PathValues.VIDEO: Video,
        PathValues.VIDEO_ID: VideoId,
        PathValues.LIPSYNC_COST: LipsyncCost,
        PathValues.LIPSYNC: Lipsync,
        PathValues.LIPSYNC_ID: LipsyncId,
        PathValues.VOICES: Voices,
        PathValues.TRANSLATE_COST: TranslateCost,
        PathValues.TRANSLATE: Translate,
        PathValues.TRANSLATE_ID: TranslateId,
        PathValues.SPEAK_COST: SpeakCost,
        PathValues.SPEAK: Speak,
        PathValues.SPEAK_ID: SpeakId,
        PathValues.ANIMATE_COST: AnimateCost,
        PathValues.ANIMATE: Animate,
        PathValues.ANIMATE_ID: AnimateId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VIDEO_COST: VideoCost,
        PathValues.VIDEO: Video,
        PathValues.VIDEO_ID: VideoId,
        PathValues.LIPSYNC_COST: LipsyncCost,
        PathValues.LIPSYNC: Lipsync,
        PathValues.LIPSYNC_ID: LipsyncId,
        PathValues.VOICES: Voices,
        PathValues.TRANSLATE_COST: TranslateCost,
        PathValues.TRANSLATE: Translate,
        PathValues.TRANSLATE_ID: TranslateId,
        PathValues.SPEAK_COST: SpeakCost,
        PathValues.SPEAK: Speak,
        PathValues.SPEAK_ID: SpeakId,
        PathValues.ANIMATE_COST: AnimateCost,
        PathValues.ANIMATE: Animate,
        PathValues.ANIMATE_ID: AnimateId,
    }
)
