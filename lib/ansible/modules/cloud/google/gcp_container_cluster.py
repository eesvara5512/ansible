#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_container_cluster
description:
- A Google Container Engine cluster.
short_description: Creates a GCP Cluster
version_added: 2.6
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  name:
    description:
    - The name of this cluster. The name must be unique within this project and zone,
      and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens
      only. Must start with a letter. Must end with a number or a letter.
    required: false
  description:
    description:
    - An optional description of this cluster.
    required: false
  initial_node_count:
    description:
    - The number of nodes to create in this cluster. You must ensure that your Compute
      Engine resource quota is sufficient for this number of instances. You must also
      have available firewall and routes quota. For requests, this field should only
      be used in lieu of a "nodePool" object, since this configuration (along with
      the "nodeConfig") will be used to create a "NodePool" object with an auto-generated
      name. Do not use this and a nodePool at the same time.
    required: true
  node_config:
    description:
    - Parameters used in creating the cluster's nodes.
    - For requests, this field should only be used in lieu of a "nodePool" object,
      since this configuration (along with the "initialNodeCount") will be used to
      create a "NodePool" object with an auto-generated name. Do not use this and
      a nodePool at the same time. For responses, this field will be populated with
      the node configuration of the first node pool. If unspecified, the defaults
      are used.
    required: false
    suboptions:
      machine_type:
        description:
        - The name of a Google Compute Engine machine type (e.g.
        - n1-standard-1). If unspecified, the default machine type is n1-standard-1.
        required: false
      disk_size_gb:
        description:
        - Size of the disk attached to each node, specified in GB. The smallest allowed
          disk size is 10GB. If unspecified, the default disk size is 100GB.
        required: false
      oauth_scopes:
        description:
        - The set of Google API scopes to be made available on all of the node VMs
          under the "default" service account.
        - 'The following scopes are recommended, but not required, and by default
          are not included: U(https://www.googleapis.com/auth/compute) is required
          for mounting persistent storage on your nodes.'
        - U(https://www.googleapis.com/auth/devstorage.read_only) is required for
          communicating with gcr.io (the Google Container Registry).
        - If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring
          are enabled, in which case their required scopes will be added.
        required: false
      service_account:
        description:
        - The Google Cloud Platform Service Account to be used by the node VMs. If
          no Service Account is specified, the "default" service account is used.
        required: false
      metadata:
        description:
        - The metadata key/value pairs assigned to instances in the cluster.
        - 'Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes
          in length. These are reflected as part of a URL in the metadata server.
          Additionally, to avoid ambiguity, keys must not conflict with any other
          metadata keys for the project or be one of the four reserved keys: "instance-template",
          "kube-env", "startup-script", and "user-data" Values are free-form strings,
          and only have meaning as interpreted by the image running in the instance.
          The only restriction placed on them is that each value''s size must be less
          than or equal to 32 KB.'
        - The total size of all keys and values must be less than 512 KB.
        - 'An object containing a list of "key": value pairs.'
        - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
        required: false
      image_type:
        description:
        - The image type to use for this node. Note that for a given image type, the
          latest version of it will be used.
        required: false
      labels:
        description:
        - 'The map of Kubernetes labels (key/value pairs) to be applied to each node.
          These will added in addition to any default label(s) that Kubernetes may
          apply to the node. In case of conflict in label keys, the applied set may
          differ depending on the Kubernetes version -- it''s best to assume the behavior
          is undefined and conflicts should be avoided. For more information, including
          usage and the valid values, see: U(http://kubernetes.io/v1.1/docs/user-guide/labels.html)
          An object containing a list of "key": value pairs.'
        - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
        required: false
      local_ssd_count:
        description:
        - The number of local SSD disks to be attached to the node.
        - 'The limit for this value is dependant upon the maximum number of disks
          available on a machine per zone. See: U(https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits)
          for more information.'
        required: false
      tags:
        description:
        - The list of instance tags applied to all nodes. Tags are used to identify
          valid sources or targets for network firewalls and are specified by the
          client during cluster or node pool creation. Each tag within the list must
          comply with RFC1035.
        required: false
      preemptible:
        description:
        - 'Whether the nodes are created as preemptible VM instances. See: U(https://cloud.google.com/compute/docs/instances/preemptible)
          for more information about preemptible VM instances.'
        required: false
        type: bool
  master_auth:
    description:
    - The authentication information for accessing the master endpoint.
    required: false
    suboptions:
      username:
        description:
        - The username to use for HTTP basic authentication to the master endpoint.
        required: false
      password:
        description:
        - The password to use for HTTP basic authentication to the master endpoint.
          Because the master endpoint is open to the Internet, you should create a
          strong password.
        required: false
      cluster_ca_certificate:
        description:
        - Base64-encoded public certificate that is the root of trust for the cluster.
        required: false
      client_certificate:
        description:
        - Base64-encoded public certificate used by clients to authenticate to the
          cluster endpoint.
        required: false
      client_key:
        description:
        - Base64-encoded private key used by clients to authenticate to the cluster
          endpoint.
        required: false
  logging_service:
    description:
    - 'The logging service the cluster should use to write logs. Currently available
      options: logging.googleapis.com - the Google Cloud Logging service.'
    - none - no logs will be exported from the cluster.
    - if left as an empty string,logging.googleapis.com will be used.
    required: false
    choices:
    - logging.googleapis.com
    - none
  monitoring_service:
    description:
    - The monitoring service the cluster should use to write metrics.
    - 'Currently available options: monitoring.googleapis.com - the Google Cloud Monitoring
      service.'
    - none - no metrics will be exported from the cluster.
    - if left as an empty string, monitoring.googleapis.com will be used.
    required: false
    choices:
    - monitoring.googleapis.com
    - none
  network:
    description:
    - The name of the Google Compute Engine network to which the cluster is connected.
      If left unspecified, the default network will be used.
    required: false
  cluster_ipv4_cidr:
    description:
    - The IP address range of the container pods in this cluster, in CIDR notation
      (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify
      a /14 block in 10.0.0.0/8.
    required: false
  addons_config:
    description:
    - Configurations for the various addons available to run in the cluster.
    required: false
    suboptions:
      http_load_balancing:
        description:
        - Configuration for the HTTP (L7) load balancing controller addon, which makes
          it easy to set up HTTP load balancers for services in a cluster.
        required: false
        suboptions:
          disabled:
            description:
            - Whether the HTTP Load Balancing controller is enabled in the cluster.
              When enabled, it runs a small pod in the cluster that manages the load
              balancers.
            required: false
            type: bool
      horizontal_pod_autoscaling:
        description:
        - Configuration for the horizontal pod autoscaling feature, which increases
          or decreases the number of replica pods a replication controller has based
          on the resource usage of the existing pods.
        required: false
        suboptions:
          disabled:
            description:
            - Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.
              When enabled, it ensures that a Heapster pod is running in the cluster,
              which is also used by the Cloud Monitoring service.
            required: false
            type: bool
  subnetwork:
    description:
    - The name of the Google Compute Engine subnetwork to which the cluster is connected.
    required: false
  location:
    description:
    - The list of Google Compute Engine locations in which the cluster's nodes should
      be located.
    required: false
  zone:
    description:
    - The zone where the cluster is deployed.
    required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a cluster
  gcp_container_cluster:
      name: my-cluster
      initial_node_count: 2
      master_auth:
        username: cluster_admin
        password: my-secret-password
      node_config:
        machine_type: n1-standard-4
        disk_size_gb: 500
      zone: us-central1-a
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
name:
  description:
  - The name of this cluster. The name must be unique within this project and zone,
    and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens
    only. Must start with a letter. Must end with a number or a letter.
  returned: success
  type: str
description:
  description:
  - An optional description of this cluster.
  returned: success
  type: str
initialNodeCount:
  description:
  - The number of nodes to create in this cluster. You must ensure that your Compute
    Engine resource quota is sufficient for this number of instances. You must also
    have available firewall and routes quota. For requests, this field should only
    be used in lieu of a "nodePool" object, since this configuration (along with the
    "nodeConfig") will be used to create a "NodePool" object with an auto-generated
    name. Do not use this and a nodePool at the same time.
  returned: success
  type: int
nodeConfig:
  description:
  - Parameters used in creating the cluster's nodes.
  - For requests, this field should only be used in lieu of a "nodePool" object, since
    this configuration (along with the "initialNodeCount") will be used to create
    a "NodePool" object with an auto-generated name. Do not use this and a nodePool
    at the same time. For responses, this field will be populated with the node configuration
    of the first node pool. If unspecified, the defaults are used.
  returned: success
  type: complex
  contains:
    machineType:
      description:
      - The name of a Google Compute Engine machine type (e.g.
      - n1-standard-1). If unspecified, the default machine type is n1-standard-1.
      returned: success
      type: str
    diskSizeGb:
      description:
      - Size of the disk attached to each node, specified in GB. The smallest allowed
        disk size is 10GB. If unspecified, the default disk size is 100GB.
      returned: success
      type: int
    oauthScopes:
      description:
      - The set of Google API scopes to be made available on all of the node VMs under
        the "default" service account.
      - 'The following scopes are recommended, but not required, and by default are
        not included: U(https://www.googleapis.com/auth/compute) is required for mounting
        persistent storage on your nodes.'
      - U(https://www.googleapis.com/auth/devstorage.read_only) is required for communicating
        with gcr.io (the Google Container Registry).
      - If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring
        are enabled, in which case their required scopes will be added.
      returned: success
      type: list
    serviceAccount:
      description:
      - The Google Cloud Platform Service Account to be used by the node VMs. If no
        Service Account is specified, the "default" service account is used.
      returned: success
      type: str
    metadata:
      description:
      - The metadata key/value pairs assigned to instances in the cluster.
      - 'Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes
        in length. These are reflected as part of a URL in the metadata server. Additionally,
        to avoid ambiguity, keys must not conflict with any other metadata keys for
        the project or be one of the four reserved keys: "instance-template", "kube-env",
        "startup-script", and "user-data" Values are free-form strings, and only have
        meaning as interpreted by the image running in the instance. The only restriction
        placed on them is that each value''s size must be less than or equal to 32
        KB.'
      - The total size of all keys and values must be less than 512 KB.
      - 'An object containing a list of "key": value pairs.'
      - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
      returned: success
      type: dict
    imageType:
      description:
      - The image type to use for this node. Note that for a given image type, the
        latest version of it will be used.
      returned: success
      type: str
    labels:
      description:
      - 'The map of Kubernetes labels (key/value pairs) to be applied to each node.
        These will added in addition to any default label(s) that Kubernetes may apply
        to the node. In case of conflict in label keys, the applied set may differ
        depending on the Kubernetes version -- it''s best to assume the behavior is
        undefined and conflicts should be avoided. For more information, including
        usage and the valid values, see: U(http://kubernetes.io/v1.1/docs/user-guide/labels.html)
        An object containing a list of "key": value pairs.'
      - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
      returned: success
      type: dict
    localSsdCount:
      description:
      - The number of local SSD disks to be attached to the node.
      - 'The limit for this value is dependant upon the maximum number of disks available
        on a machine per zone. See: U(https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits)
        for more information.'
      returned: success
      type: int
    tags:
      description:
      - The list of instance tags applied to all nodes. Tags are used to identify
        valid sources or targets for network firewalls and are specified by the client
        during cluster or node pool creation. Each tag within the list must comply
        with RFC1035.
      returned: success
      type: list
    preemptible:
      description:
      - 'Whether the nodes are created as preemptible VM instances. See: U(https://cloud.google.com/compute/docs/instances/preemptible)
        for more information about preemptible VM instances.'
      returned: success
      type: bool
masterAuth:
  description:
  - The authentication information for accessing the master endpoint.
  returned: success
  type: complex
  contains:
    username:
      description:
      - The username to use for HTTP basic authentication to the master endpoint.
      returned: success
      type: str
    password:
      description:
      - The password to use for HTTP basic authentication to the master endpoint.
        Because the master endpoint is open to the Internet, you should create a strong
        password.
      returned: success
      type: str
    clusterCaCertificate:
      description:
      - Base64-encoded public certificate that is the root of trust for the cluster.
      returned: success
      type: str
    clientCertificate:
      description:
      - Base64-encoded public certificate used by clients to authenticate to the cluster
        endpoint.
      returned: success
      type: str
    clientKey:
      description:
      - Base64-encoded private key used by clients to authenticate to the cluster
        endpoint.
      returned: success
      type: str
loggingService:
  description:
  - 'The logging service the cluster should use to write logs. Currently available
    options: logging.googleapis.com - the Google Cloud Logging service.'
  - none - no logs will be exported from the cluster.
  - if left as an empty string,logging.googleapis.com will be used.
  returned: success
  type: str
monitoringService:
  description:
  - The monitoring service the cluster should use to write metrics.
  - 'Currently available options: monitoring.googleapis.com - the Google Cloud Monitoring
    service.'
  - none - no metrics will be exported from the cluster.
  - if left as an empty string, monitoring.googleapis.com will be used.
  returned: success
  type: str
network:
  description:
  - The name of the Google Compute Engine network to which the cluster is connected.
    If left unspecified, the default network will be used.
  returned: success
  type: str
clusterIpv4Cidr:
  description:
  - The IP address range of the container pods in this cluster, in CIDR notation (e.g.
    10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block
    in 10.0.0.0/8.
  returned: success
  type: str
addonsConfig:
  description:
  - Configurations for the various addons available to run in the cluster.
  returned: success
  type: complex
  contains:
    httpLoadBalancing:
      description:
      - Configuration for the HTTP (L7) load balancing controller addon, which makes
        it easy to set up HTTP load balancers for services in a cluster.
      returned: success
      type: complex
      contains:
        disabled:
          description:
          - Whether the HTTP Load Balancing controller is enabled in the cluster.
            When enabled, it runs a small pod in the cluster that manages the load
            balancers.
          returned: success
          type: bool
    horizontalPodAutoscaling:
      description:
      - Configuration for the horizontal pod autoscaling feature, which increases
        or decreases the number of replica pods a replication controller has based
        on the resource usage of the existing pods.
      returned: success
      type: complex
      contains:
        disabled:
          description:
          - Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.
            When enabled, it ensures that a Heapster pod is running in the cluster,
            which is also used by the Cloud Monitoring service.
          returned: success
          type: bool
subnetwork:
  description:
  - The name of the Google Compute Engine subnetwork to which the cluster is connected.
  returned: success
  type: str
location:
  description:
  - The list of Google Compute Engine locations in which the cluster's nodes should
    be located.
  returned: success
  type: list
endpoint:
  description:
  - The IP address of this cluster's master endpoint.
  - The endpoint can be accessed from the internet at https://username:password@endpoint/
    See the masterAuth property of this resource for username and password information.
  returned: success
  type: str
initialClusterVersion:
  description:
  - The software version of the master endpoint and kubelets used in the cluster when
    it was first created. The version can be upgraded over time.
  returned: success
  type: str
currentMasterVersion:
  description:
  - The current software version of the master endpoint.
  returned: success
  type: str
currentNodeVersion:
  description:
  - The current version of the node software components. If they are currently at
    multiple versions because they're in the process of being upgraded, this reflects
    the minimum version of all nodes.
  returned: success
  type: str
createTime:
  description:
  - The time the cluster was created, in RFC3339 text format.
  returned: success
  type: str
nodeIpv4CidrSize:
  description:
  - The size of the address space on each node for hosting containers.
  - This is provisioned from within the container_ipv4_cidr range.
  returned: success
  type: int
servicesIpv4Cidr:
  description:
  - The IP address range of the Kubernetes services in this cluster, in CIDR notation
    (e.g. 1.2.3.4/29). Service addresses are typically put in the last /16 from the
    container CIDR.
  returned: success
  type: str
currentNodeCount:
  description:
  - The number of nodes currently in the cluster.
  returned: success
  type: int
expireTime:
  description:
  - The time the cluster will be automatically deleted in RFC3339 text format.
  returned: success
  type: str
zone:
  description:
  - The zone where the cluster is deployed.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(type='str'),
            description=dict(type='str'),
            initial_node_count=dict(required=True, type='int'),
            node_config=dict(
                type='dict',
                options=dict(
                    machine_type=dict(type='str'),
                    disk_size_gb=dict(type='int'),
                    oauth_scopes=dict(type='list', elements='str'),
                    service_account=dict(type='str'),
                    metadata=dict(type='dict'),
                    image_type=dict(type='str'),
                    labels=dict(type='dict'),
                    local_ssd_count=dict(type='int'),
                    tags=dict(type='list', elements='str'),
                    preemptible=dict(type='bool'),
                ),
            ),
            master_auth=dict(
                type='dict',
                options=dict(
                    username=dict(type='str'),
                    password=dict(type='str'),
                    cluster_ca_certificate=dict(type='str'),
                    client_certificate=dict(type='str'),
                    client_key=dict(type='str'),
                ),
            ),
            logging_service=dict(type='str', choices=['logging.googleapis.com', 'none']),
            monitoring_service=dict(type='str', choices=['monitoring.googleapis.com', 'none']),
            network=dict(type='str'),
            cluster_ipv4_cidr=dict(type='str'),
            addons_config=dict(
                type='dict',
                options=dict(
                    http_load_balancing=dict(type='dict', options=dict(disabled=dict(type='bool'))),
                    horizontal_pod_autoscaling=dict(type='dict', options=dict(disabled=dict(type='bool'))),
                ),
            ),
            subnetwork=dict(type='str'),
            location=dict(type='list', elements='str'),
            zone=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'container')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    auth = GcpSession(module, 'container')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'container')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'initialNodeCount': module.params.get('initial_node_count'),
        u'nodeConfig': ClusterNodeconfig(module.params.get('node_config', {}), module).to_request(),
        u'masterAuth': ClusterMasterauth(module.params.get('master_auth', {}), module).to_request(),
        u'loggingService': module.params.get('logging_service'),
        u'monitoringService': module.params.get('monitoring_service'),
        u'network': module.params.get('network'),
        u'clusterIpv4Cidr': module.params.get('cluster_ipv4_cidr'),
        u'addonsConfig': ClusterAddonsconfig(module.params.get('addons_config', {}), module).to_request(),
        u'subnetwork': module.params.get('subnetwork'),
        u'location': module.params.get('location'),
    }
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'container')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://container.googleapis.com/v1/projects/{project}/zones/{zone}/clusters/{name}".format(**module.params)


def collection(module):
    return "https://container.googleapis.com/v1/projects/{project}/zones/{zone}/clusters".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': response.get(u'name'),
        u'description': response.get(u'description'),
        u'initialNodeCount': module.params.get('initial_node_count'),
        u'nodeConfig': ClusterNodeconfig(module.params.get('node_config', {}), module).to_request(),
        u'masterAuth': ClusterMasterauth(response.get(u'masterAuth', {}), module).from_response(),
        u'loggingService': response.get(u'loggingService'),
        u'monitoringService': response.get(u'monitoringService'),
        u'network': response.get(u'network'),
        u'clusterIpv4Cidr': response.get(u'clusterIpv4Cidr'),
        u'addonsConfig': ClusterAddonsconfig(response.get(u'addonsConfig', {}), module).from_response(),
        u'subnetwork': response.get(u'subnetwork'),
        u'location': response.get(u'location'),
        u'endpoint': response.get(u'endpoint'),
        u'initialClusterVersion': response.get(u'initialClusterVersion'),
        u'currentMasterVersion': response.get(u'currentMasterVersion'),
        u'currentNodeVersion': response.get(u'currentNodeVersion'),
        u'createTime': response.get(u'createTime'),
        u'nodeIpv4CidrSize': response.get(u'nodeIpv4CidrSize'),
        u'servicesIpv4Cidr': response.get(u'servicesIpv4Cidr'),
        u'currentNodeCount': response.get(u'currentNodeCount'),
        u'expireTime': response.get(u'expireTime'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://container.googleapis.com/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']))


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


# Google Container Engine API has its own layout for the create method,
# defined like this:
#
# {
#   'cluster': {
#     ... cluster data
#   }
# }
#
# Format the request to match the expected input by the API
def encode_request(resource_request, module):
    return {'cluster': resource_request}


class ClusterNodeconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'machineType': self.request.get('machine_type'),
                u'diskSizeGb': self.request.get('disk_size_gb'),
                u'oauthScopes': self.request.get('oauth_scopes'),
                u'serviceAccount': self.request.get('service_account'),
                u'metadata': self.request.get('metadata'),
                u'imageType': self.request.get('image_type'),
                u'labels': self.request.get('labels'),
                u'localSsdCount': self.request.get('local_ssd_count'),
                u'tags': self.request.get('tags'),
                u'preemptible': self.request.get('preemptible'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'machineType': self.request.get(u'machineType'),
                u'diskSizeGb': self.request.get(u'diskSizeGb'),
                u'oauthScopes': self.request.get(u'oauthScopes'),
                u'serviceAccount': self.request.get(u'serviceAccount'),
                u'metadata': self.request.get(u'metadata'),
                u'imageType': self.request.get(u'imageType'),
                u'labels': self.request.get(u'labels'),
                u'localSsdCount': self.request.get(u'localSsdCount'),
                u'tags': self.request.get(u'tags'),
                u'preemptible': self.request.get(u'preemptible'),
            }
        )


class ClusterMasterauth(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'username': self.request.get('username'),
                u'password': self.request.get('password'),
                u'clusterCaCertificate': self.request.get('cluster_ca_certificate'),
                u'clientCertificate': self.request.get('client_certificate'),
                u'clientKey': self.request.get('client_key'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'username': self.request.get(u'username'),
                u'password': self.request.get(u'password'),
                u'clusterCaCertificate': self.request.get(u'clusterCaCertificate'),
                u'clientCertificate': self.request.get(u'clientCertificate'),
                u'clientKey': self.request.get(u'clientKey'),
            }
        )


class ClusterAddonsconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'httpLoadBalancing': ClusterHttploadbalancing(self.request.get('http_load_balancing', {}), self.module).to_request(),
                u'horizontalPodAutoscaling': ClusterHorizontalpodautoscaling(self.request.get('horizontal_pod_autoscaling', {}), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'httpLoadBalancing': ClusterHttploadbalancing(self.request.get(u'httpLoadBalancing', {}), self.module).from_response(),
                u'horizontalPodAutoscaling': ClusterHorizontalpodautoscaling(self.request.get(u'horizontalPodAutoscaling', {}), self.module).from_response(),
            }
        )


class ClusterHttploadbalancing(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'disabled': self.request.get('disabled')})

    def from_response(self):
        return remove_nones_from_dict({u'disabled': self.request.get(u'disabled')})


class ClusterHorizontalpodautoscaling(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'disabled': self.request.get('disabled')})

    def from_response(self):
        return remove_nones_from_dict({u'disabled': self.request.get(u'disabled')})


if __name__ == '__main__':
    main()
