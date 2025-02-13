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


class AnimateInitial(BaseModel):
    # A unique identifier for the video.
    id: str = Field(alias='id')

    # A URL to a file containing the input transcript.
    transcript_url: str = Field(alias='transcript_url')

    # The status of the audio.
    status: str = Field(alias='status')

    # A URL which can be used to download the audio.
    video_url: typing.Optional[str] = Field(None, alias='video_url')

    # A URL which can be used to download the audio.
    audio_url: typing.Optional[str] = Field(None, alias='audio_url')
    class Config:
        arbitrary_types_allowed = True
