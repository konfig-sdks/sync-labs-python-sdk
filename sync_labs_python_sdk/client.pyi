# coding: utf-8
"""
    Synchronize API

    Synchronize API allows you to lipsync a video to any audio in any language.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from sync_labs_python_sdk.client_custom import ClientCustom
from sync_labs_python_sdk.configuration import Configuration
from sync_labs_python_sdk.api_client import ApiClient
from sync_labs_python_sdk.type_util import copy_signature
from sync_labs_python_sdk.apis.tags.animate_api import AnimateApi
from sync_labs_python_sdk.apis.tags.lipsync_api import LipsyncApi
from sync_labs_python_sdk.apis.tags.speak_api import SpeakApi
from sync_labs_python_sdk.apis.tags.translate_api import TranslateApi
from sync_labs_python_sdk.apis.tags.video_api import VideoApi
from sync_labs_python_sdk.apis.tags.voices_api import VoicesApi



class SyncLabs(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.animate: AnimateApi = AnimateApi(api_client)
        self.lipsync: LipsyncApi = LipsyncApi(api_client)
        self.speak: SpeakApi = SpeakApi(api_client)
        self.translate: TranslateApi = TranslateApi(api_client)
        self.video: VideoApi = VideoApi(api_client)
        self.voices: VoicesApi = VoicesApi(api_client)
