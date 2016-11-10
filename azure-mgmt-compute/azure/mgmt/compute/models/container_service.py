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

from .resource import Resource


class ContainerService(Resource):
    """Container service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response.
    :vartype provisioning_state: str
    :param orchestrator_profile: Properties of the orchestrator.
    :type orchestrator_profile: :class:`ContainerServiceOrchestratorProfile
     <azure.mgmt.compute.models.ContainerServiceOrchestratorProfile>`
    :param custom_profile: Properties for custom clusters.
    :type custom_profile: :class:`ContainerServiceCustomProfile
     <azure.mgmt.compute.models.ContainerServiceCustomProfile>`
    :param service_principal_profile: Properties for cluster service
     principals.
    :type service_principal_profile:
     :class:`ContainerServiceServicePrincipalProfile
     <azure.mgmt.compute.models.ContainerServiceServicePrincipalProfile>`
    :param master_profile: Properties of master agents.
    :type master_profile: :class:`ContainerServiceMasterProfile
     <azure.mgmt.compute.models.ContainerServiceMasterProfile>`
    :param agent_pool_profiles: Properties of the agent pool.
    :type agent_pool_profiles: list of
     :class:`ContainerServiceAgentPoolProfile
     <azure.mgmt.compute.models.ContainerServiceAgentPoolProfile>`
    :param windows_profile: Properties of Windows VMs.
    :type windows_profile: :class:`ContainerServiceWindowsProfile
     <azure.mgmt.compute.models.ContainerServiceWindowsProfile>`
    :param linux_profile: Properties of Linux VMs.
    :type linux_profile: :class:`ContainerServiceLinuxProfile
     <azure.mgmt.compute.models.ContainerServiceLinuxProfile>`
    :param diagnostics_profile: Properties of the diagnostic agent.
    :type diagnostics_profile: :class:`ContainerServiceDiagnosticsProfile
     <azure.mgmt.compute.models.ContainerServiceDiagnosticsProfile>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'master_profile': {'required': True},
        'agent_pool_profiles': {'required': True},
        'linux_profile': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'orchestrator_profile': {'key': 'properties.orchestratorProfile', 'type': 'ContainerServiceOrchestratorProfile'},
        'custom_profile': {'key': 'properties.customProfile', 'type': 'ContainerServiceCustomProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ContainerServiceServicePrincipalProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'ContainerServiceMasterProfile'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ContainerServiceAgentPoolProfile]'},
        'windows_profile': {'key': 'properties.windowsProfile', 'type': 'ContainerServiceWindowsProfile'},
        'linux_profile': {'key': 'properties.linuxProfile', 'type': 'ContainerServiceLinuxProfile'},
        'diagnostics_profile': {'key': 'properties.diagnosticsProfile', 'type': 'ContainerServiceDiagnosticsProfile'},
    }

    def __init__(self, location, master_profile, agent_pool_profiles, linux_profile, tags=None, orchestrator_profile=None, custom_profile=None, service_principal_profile=None, windows_profile=None, diagnostics_profile=None):
        super(ContainerService, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.orchestrator_profile = orchestrator_profile
        self.custom_profile = custom_profile
        self.service_principal_profile = service_principal_profile
        self.master_profile = master_profile
        self.agent_pool_profiles = agent_pool_profiles
        self.windows_profile = windows_profile
        self.linux_profile = linux_profile
        self.diagnostics_profile = diagnostics_profile
