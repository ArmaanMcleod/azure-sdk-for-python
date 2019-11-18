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


class DeliveryRuleCondition(Model):
    """A condition for the delivery rule.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DeliveryRuleUrlPathCondition,
    DeliveryRuleUrlFileExtensionCondition

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Constant filled by server.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    _subtype_map = {
        'name': {'UrlPath': 'DeliveryRuleUrlPathCondition', 'UrlFileExtension': 'DeliveryRuleUrlFileExtensionCondition'}
    }

    def __init__(self, **kwargs):
        super(DeliveryRuleCondition, self).__init__(**kwargs)
        self.name = None