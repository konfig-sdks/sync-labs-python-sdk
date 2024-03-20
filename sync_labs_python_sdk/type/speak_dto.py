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


class RequiredSpeakDto(TypedDict):
    # A string of text to be spoken by the AI
    transcript: str

    # The voice to use for audio generation
    voiceId: str

class OptionalSpeakDto(TypedDict, total=False):
    # Maximum number of credits to use for audio generation. If job exceeds this value, the job will be aborted
    maxCredits: typing.Union[int, float]

    # A url to send a notification to upon completion of audio generation
    webhookUrl: str

class SpeakDto(RequiredSpeakDto, OptionalSpeakDto):
    pass
