# coding: utf-8

"""
    Synchronize API

    Synchronize API allows you to lipsync a video to any audio in any language.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sync_labs_python_sdk import schemas  # noqa: F401


class TranslationJobExtended(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "original_video_url",
            "source_language",
            "audio_url",
            "step",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            audio_url = schemas.StrSchema
            original_video_url = schemas.StrSchema
            source_language = schemas.StrSchema
            status = schemas.StrSchema
            step = schemas.StrSchema
            video_url = schemas.StrSchema
            transcript_url = schemas.StrSchema
            target_language = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "audio_url": audio_url,
                "original_video_url": original_video_url,
                "source_language": source_language,
                "status": status,
                "step": step,
                "video_url": video_url,
                "transcript_url": transcript_url,
                "target_language": target_language,
            }
    
    original_video_url: MetaOapg.properties.original_video_url
    source_language: MetaOapg.properties.source_language
    audio_url: MetaOapg.properties.audio_url
    step: MetaOapg.properties.step
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_url"]) -> MetaOapg.properties.audio_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_video_url"]) -> MetaOapg.properties.original_video_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_language"]) -> MetaOapg.properties.source_language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["step"]) -> MetaOapg.properties.step: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["video_url"]) -> MetaOapg.properties.video_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transcript_url"]) -> MetaOapg.properties.transcript_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_language"]) -> MetaOapg.properties.target_language: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "audio_url", "original_video_url", "source_language", "status", "step", "video_url", "transcript_url", "target_language", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_url"]) -> MetaOapg.properties.audio_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_video_url"]) -> MetaOapg.properties.original_video_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_language"]) -> MetaOapg.properties.source_language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["step"]) -> MetaOapg.properties.step: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["video_url"]) -> typing.Union[MetaOapg.properties.video_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transcript_url"]) -> typing.Union[MetaOapg.properties.transcript_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_language"]) -> typing.Union[MetaOapg.properties.target_language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "audio_url", "original_video_url", "source_language", "status", "step", "video_url", "transcript_url", "target_language", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        original_video_url: typing.Union[MetaOapg.properties.original_video_url, str, ],
        source_language: typing.Union[MetaOapg.properties.source_language, str, ],
        audio_url: typing.Union[MetaOapg.properties.audio_url, str, ],
        step: typing.Union[MetaOapg.properties.step, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        video_url: typing.Union[MetaOapg.properties.video_url, str, schemas.Unset] = schemas.unset,
        transcript_url: typing.Union[MetaOapg.properties.transcript_url, str, schemas.Unset] = schemas.unset,
        target_language: typing.Union[MetaOapg.properties.target_language, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TranslationJobExtended':
        return super().__new__(
            cls,
            *args,
            original_video_url=original_video_url,
            source_language=source_language,
            audio_url=audio_url,
            step=step,
            id=id,
            status=status,
            video_url=video_url,
            transcript_url=transcript_url,
            target_language=target_language,
            _configuration=_configuration,
            **kwargs,
        )
