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


class RequiredAnimateInitial(TypedDict):
    # A unique identifier for the video.
    id: str

    # A URL to a file containing the input transcript.
    transcript_url: str

    # The status of the audio.
    status: str

class OptionalAnimateInitial(TypedDict, total=False):
    # A URL which can be used to download the audio.
    video_url: str

    # A URL which can be used to download the audio.
    audio_url: str

class AnimateInitial(RequiredAnimateInitial, OptionalAnimateInitial):
    pass
