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


class OptionalClaims(Model):
    """Specifying the claims to be included in the token.

    :param id_token: Optional claims requested to be included in the id token.
    :type id_token: list[~azure.graphrbac.models.OptionalClaim]
    :param access_token: Optional claims requested to be included in the
     access token.
    :type access_token: list[~azure.graphrbac.models.OptionalClaim]
    :param saml_token: Optional claims requested to be included in the saml
     token.
    :type saml_token: list[~azure.graphrbac.models.OptionalClaim]
    """

    _attribute_map = {
        'id_token': {'key': 'idToken', 'type': '[OptionalClaim]'},
        'access_token': {'key': 'accessToken', 'type': '[OptionalClaim]'},
        'saml_token': {'key': 'samlToken', 'type': '[OptionalClaim]'},
    }

    def __init__(self, *, id_token=None, access_token=None, saml_token=None, **kwargs) -> None:
        super(OptionalClaims, self).__init__(**kwargs)
        self.id_token = id_token
        self.access_token = access_token
        self.saml_token = saml_token