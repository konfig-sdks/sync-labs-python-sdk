# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from sync_labs_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from sync_labs_python_sdk.model.animate_dto import AnimateDto
from sync_labs_python_sdk.model.animate_extended import AnimateExtended
from sync_labs_python_sdk.model.animate_initial import AnimateInitial
from sync_labs_python_sdk.model.create_video_dto import CreateVideoDto
from sync_labs_python_sdk.model.lip_sync_extended import LipSyncExtended
from sync_labs_python_sdk.model.lip_sync_initial import LipSyncInitial
from sync_labs_python_sdk.model.lipsync_dto import LipsyncDto
from sync_labs_python_sdk.model.speak_dto import SpeakDto
from sync_labs_python_sdk.model.speak_extended import SpeakExtended
from sync_labs_python_sdk.model.speak_initial import SpeakInitial
from sync_labs_python_sdk.model.translate_dto import TranslateDto
from sync_labs_python_sdk.model.translation_job_extended import TranslationJobExtended
from sync_labs_python_sdk.model.translation_job_initial import TranslationJobInitial
from sync_labs_python_sdk.model.video_extended import VideoExtended
from sync_labs_python_sdk.model.video_initial import VideoInitial
