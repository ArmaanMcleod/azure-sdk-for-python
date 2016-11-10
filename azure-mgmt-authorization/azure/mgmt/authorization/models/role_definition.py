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


class RoleDefinition(Model):
    """Role definition.

    :param id: The role definition ID.
    :type id: str
    :param name: The role definition name.
    :type name: str
    :param type: The role definition type.
    :type type: str
    :param properties: Role definition properties.
    :type properties: :class:`RoleDefinitionProperties
     <azure.mgmt.authorization.models.RoleDefinitionProperties>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'RoleDefinitionProperties'},
    }

    def __init__(self, id=None, name=None, type=None, properties=None):
        self.id = id
        self.name = name
        self.type = type
        self.properties = properties
