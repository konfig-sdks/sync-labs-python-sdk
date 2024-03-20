# coding: utf-8

"""
    Synchronize API

    Synchronize API allows you to lipsync a video to any audio in any language.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import sync_labs_python_sdk
from sync_labs_python_sdk.paths.translate_cost import get
from sync_labs_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTranslateCost(ApiTestMixin, unittest.TestCase):
    """
    TranslateCost unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
