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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operationalization_clusters_operations import OperationalizationClustersOperations
from .operations.machine_learning_compute_operations import MachineLearningComputeOperations
from . import models


class MachineLearningComputeManagementClientConfiguration(AzureConfiguration):
    """Configuration for MachineLearningComputeManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(MachineLearningComputeManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('machinelearningcomputemanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class MachineLearningComputeManagementClient(object):
    """These APIs allow end users to operate on Azure Machine Learning Compute resources. They support the following operations:&lt;ul&gt;&lt;li&gt;Create or update a cluster&lt;/li&gt;&lt;li&gt;Get a cluster&lt;/li&gt;&lt;li&gt;Patch a cluster&lt;/li&gt;&lt;li&gt;Delete a cluster&lt;/li&gt;&lt;li&gt;Get keys for a cluster&lt;/li&gt;&lt;li&gt;Check if updates are available for system services in a cluster&lt;/li&gt;&lt;li&gt;Update system services in a cluster&lt;/li&gt;&lt;li&gt;Get all clusters in a resource group&lt;/li&gt;&lt;li&gt;Get all clusters in a subscription&lt;/li&gt;&lt;/ul&gt;

    :ivar config: Configuration for client.
    :vartype config: MachineLearningComputeManagementClientConfiguration

    :ivar operationalization_clusters: OperationalizationClusters operations
    :vartype operationalization_clusters: azure.mgmt.machinelearningcompute.operations.OperationalizationClustersOperations
    :ivar machine_learning_compute: MachineLearningCompute operations
    :vartype machine_learning_compute: azure.mgmt.machinelearningcompute.operations.MachineLearningComputeOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MachineLearningComputeManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-08-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operationalization_clusters = OperationalizationClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self.config, self._serialize, self._deserialize)
