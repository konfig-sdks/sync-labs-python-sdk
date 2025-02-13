# coding: utf-8

"""
    Synchronize API

    Synchronize API allows you to lipsync a video to any audio in any language.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredVideoExtended(TypedDict):
    # A unique identifier for the video.
    id: str

    # The original URL of the video that was submitted.
    original_video_url: str

    # The original URL of the audio that was submitted.
    original_audio_url: str

    # The status of the video.
    status: str

    # A flag to enable / disable post-processing
    synergize: bool

    # The number of credits deducted for the video.
    credits_deducted: typing.Union[int, float]

class OptionalVideoExtended(TypedDict, total=False):
    # A URL which can be used to download the video.
    url: str

class VideoExtended(RequiredVideoExtended, OptionalVideoExtended):
    pass
