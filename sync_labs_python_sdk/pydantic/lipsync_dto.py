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


class LipsyncDto(BaseModel):
    # A url to the audio file to be synchronized -- must be publicly accessible
    audio_url: str = Field(alias='audioUrl')

    # A url to the video file to be synchronized -- must be publicly accessible
    video_url: str = Field(alias='videoUrl')

    # A flag to enable / disable post-processing
    synergize: bool = Field(alias='synergize')

    # Maximum number of credits to use for video generation. If job exceeds this value, the job will be aborted
    max_credits: typing.Optional[typing.Union[int, float]] = Field(None, alias='maxCredits')

    # A url to send a notification to upon completion of video generation
    webhook_url: typing.Optional[str] = Field(None, alias='webhookUrl')

    # The model to use for video generation
    model: typing.Optional[str] = Field(None, alias='model')
    class Config:
        arbitrary_types_allowed = True
