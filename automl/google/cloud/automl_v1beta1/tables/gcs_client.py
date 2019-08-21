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

"""Wraps the Google Cloud Storage client library for use in tables helper."""

import pandas
import time

from google.cloud import storage

class GcsClient(object):
    """Uploads Pandas DataFrame to a bucket in Google Cloud Storage."""

    def __init__(self, **kwargs):
        """Constructor.
        
        Args:
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
        """
        self.client = storage.Client()


    def create_bucket(bucket_name=None):
        """Creates a new bucket and returns the created bucket's name.
        
        Args:
            bucket_name (Optional[string]): The name of the bucket to create.
                If no `bucket_name` was provided, we will set it to
                'automl-tables-bucket-${timestamp}'. The value of ${timestamp}
                is an integer UNIX timestamp of when this bucket is created.
                An example `bucket_name` is 'automl-tables-bucket-1234567890'.
        """
        if bucket_name is None:
            bucket_name = "automl-tables-bucket-{}".format(int(time.time()))
        bucket = self.client.create_bucket(bucket_name)
        return bucket_name


    def upload_pandas_dataframe(bucket_name, dataframe, uploaded_csv_name):
        """Converts a Pandas DataFrame to CSV and uploads the CSV to the bucket.

        Args:
            bucket_name (string): The bucket name to upload the CSV to.
            dataframe (pandas.DataFrame): The Pandas Dataframe to be uploaded.
            uploaded_csv_name (string): The name for the uploaded CSV file.
        """
        if not isinstance(dataframe, pandas.DataFrame):
            raise ValueError("'dataframe' must be a pandas.DataFrame instance.")

        source_csv_name = "autml-table-dataframe-{}.csv".format(int(time.time()))
        dataframe.to_csv(source_csv_name)
        
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(uploaded_csv_name)
        blob.upload_from_filename(source_csv_name)
