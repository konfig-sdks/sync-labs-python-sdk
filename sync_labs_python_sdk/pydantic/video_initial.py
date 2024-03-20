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
from pydantic import BaseModel, Field, RootModel


class VideoInitial(BaseModel):
    # A unique identifier for the video.
    id: str = Field(alias='id')

    # The original URL of the video that was submitted.
    original_video_url: str = Field(alias='original_video_url')

    # The original URL of the audio that was submitted.
    original_audio_url: str = Field(alias='original_audio_url')

    # The status of the video.
    status: str = Field(alias='status')

    # A flag to enable / disable post-processing
    synergize: bool = Field(alias='synergize')

    # A URL which can be used to download the video.
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
