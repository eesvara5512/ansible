#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: mso_schema_template_vrf
short_description: Manage VRFs in schema templates
description:
- Manage VRFs in schema templates on Cisco ACI Multi-Site.
author:
- Dag Wieers (@dagwieers)
version_added: '2.8'
options:
  schema:
    description:
    - The name of the schema.
    type: str
    required: yes
  template:
    description:
    - The name of the template.
    type: list
  vrf:
    description:
    - The name of the VRF to manage.
    type: str
    aliases: [ name ]
  display_name:
    description:
    - The name as displayed on the MSO web interface.
    type: str
  layer3_multicast:
    description:
    - Whether to enable L3 multicast.
    type: bool
  state:
    description:
    - Use C(present) or C(absent) for adding or removing.
    - Use C(query) for listing an object or multiple objects.
    type: str
    choices: [ absent, present, query ]
    default: present
extends_documentation_fragment: mso
'''

EXAMPLES = r'''
- name: Add a new VRF
  mso_schema_template_vrf:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    vrf: VRF 1
    state: present
  delegate_to: localhost

- name: Remove an VRF
  mso_schema_template_vrf:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    vrf: VRF1
    state: absent
  delegate_to: localhost

- name: Query a specific VRFs
  mso_schema_template_vrf:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    vrf: VRF1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all VRFs
  mso_schema_template_vrf:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    state: query
  delegate_to: localhost
  register: query_result
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.aci.mso import MSOModule, mso_argument_spec, mso_reference_spec, issubset


def main():
    argument_spec = mso_argument_spec()
    argument_spec.update(
        schema=dict(type='str', required=True),
        template=dict(type='str', required=True),
        vrf=dict(type='str', required=False, aliases=['name']),  # This parameter is not required for querying all objects
        display_name=dict(type='str'),
        layer3_multicast=dict(type='bool'),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'absent', ['vrf']],
            ['state', 'present', ['vrf']],
        ],
    )

    schema = module.params['schema']
    template = module.params['template']
    vrf = module.params['vrf']
    display_name = module.params['display_name']
    layer3_multicast = module.params['layer3_multicast']
    state = module.params['state']

    mso = MSOModule(module)

    # Get schema_id
    schema_obj = mso.get_obj('schemas', displayName=schema)
    if schema_obj:
        schema_id = schema_obj['id']
    else:
        mso.fail_json(msg="Provided schema '{0}' does not exist".format(schema))

    path = 'schemas/{id}'.format(id=schema_id)

    # Get template
    templates = [t['name'] for t in schema_obj['templates']]
    if template not in templates:
        mso.fail_json(msg="Provided template '{0}' does not exist. Existing templates: {1}".format(template, ', '.join(templates)))
    template_idx = templates.index(template)

    # Get ANP
    vrfs = [v['name'] for v in schema_obj['templates'][template_idx]['vrfs']]

    if vrf is not None and vrf in vrfs:
        vrf_idx = vrfs.index(vrf)
        mso.existing = schema_obj['templates'][template_idx]['vrfs'][vrf_idx]

    if state == 'query':
        if vrf is None:
            mso.existing = schema_obj['templates'][template_idx]['vrfs']
        elif not mso.existing:
            mso.fail_json(msg="VRF '{vrf}' not found".format(vrf=vrf))
        mso.exit_json()

    mso.previous = mso.existing
    if state == 'absent':
        if mso.existing:
            mso.sent = mso.existing = {}
            operation = [dict(
                op='remove',
                path='/templates/{template}/vrfs/{vrf}'.format(template=template, vrf=vrf),
            )]
            if not module.check_mode:
                mso.request(path, method='PATCH', data=operation)

    elif state == 'present':
        if display_name is None and not mso.existing:
            display_name = vrf

        payload = dict(
            name=vrf,
            displayName=display_name,
            l3MCast=layer3_multicast,
            # FIXME
            regions=[],
        )

        mso.sanitize(payload, collate=True)

        if mso.existing:
            operation = [dict(
                op='replace',
                path='/templates/{template}/vrfs/{vrf}'.format(template=template, vrf=vrf),
                value=mso.sent,
            )]

        else:
            operation = [dict(
                op='add',
                path='/templates/{template}/vrfs/-'.format(template=template),
                value=mso.sent,
            )]

        mso.existing = mso.proposed
        if not module.check_mode:
            mso.request(path, method='PATCH', data=operation)

    mso.exit_json()


if __name__ == "__main__":
    main()
