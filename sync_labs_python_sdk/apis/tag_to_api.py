import typing_extensions

from sync_labs_python_sdk.apis.tags import TagValues
from sync_labs_python_sdk.apis.tags.video_api import VideoApi
from sync_labs_python_sdk.apis.tags.lipsync_api import LipsyncApi
from sync_labs_python_sdk.apis.tags.translate_api import TranslateApi
from sync_labs_python_sdk.apis.tags.speak_api import SpeakApi
from sync_labs_python_sdk.apis.tags.animate_api import AnimateApi
from sync_labs_python_sdk.apis.tags.voices_api import VoicesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VIDEO: VideoApi,
        TagValues.LIPSYNC: LipsyncApi,
        TagValues.TRANSLATE: TranslateApi,
        TagValues.SPEAK: SpeakApi,
        TagValues.ANIMATE: AnimateApi,
        TagValues.VOICES: VoicesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VIDEO: VideoApi,
        TagValues.LIPSYNC: LipsyncApi,
        TagValues.TRANSLATE: TranslateApi,
        TagValues.SPEAK: SpeakApi,
        TagValues.ANIMATE: AnimateApi,
        TagValues.VOICES: VoicesApi,
    }
)
