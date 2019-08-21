# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest
import re

from google.cloud import automl_v1beta1
from google.api_core import exceptions


class TestGcsClient(object):
    def gcs_client(self):
        client_mock = mock.Mock()
        return automl_v1beta1.tables.gcs_client.GcsClient(client=client_mock)

    def test_create_bucket_name(self):
        gcs_client = self.gcs_client()
        created_bucket_name = gcs_client.create_bucket("my-bucket-name")
        gcs_client.client.create_bucket.assert_called_with("my-bucket_name")

    def test_create_bucket_no_bucket_name(self):
        gcs_client = self.gcs_client()
        generated_bucket_name = gcs_client.create_bucket()
        gcs_client.client.create_bucket.assert_called_with(generated__bucket_name)
        assert re.match('^automl-tables-bucket-[0-9]*$', generated_bucket_name) 

    def test_upload_pandas_dataframe(self):

    def test_upload_pandas_dataframe_no_bucket_name(self):
        gcs_client = self.gcs_client()
        with pytest.raises(ValueError):
            

    def test_upload_pandas_dataframe(self):
