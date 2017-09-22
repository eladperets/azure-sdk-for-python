# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AppInsightsCredentials(Model):
    """AppInsights credentials.

    :param app_id: The AppInsights application ID.
    :type app_id: str
    :param instrumentation_key: The AppInsights instrumentation key. This is
     not returned in response of GET/PUT on the resource. To see this please
     call listKeys API.
    :type instrumentation_key: str
    """

    _attribute_map = {
        'app_id': {'key': 'appId', 'type': 'str'},
        'instrumentation_key': {'key': 'instrumentationKey', 'type': 'str'},
    }

    def __init__(self, app_id=None, instrumentation_key=None):
        self.app_id = app_id
        self.instrumentation_key = instrumentation_key
