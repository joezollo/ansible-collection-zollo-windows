#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-only
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = r'''
---
module: win_dhcp_scope
short_description: Manages Windows DHCP Server Scopes
author: Joe Zollo (@joezollo)
requirements:
  - This module requires Windows Server 2012 or Newer
description:
  - Manage Windows DHCP Server Scopes
  - Task should be delegated to a Windows DHCP Server
options:
  type:
    description:
      - The type of DHCP address.
      - Leases expire as defined by l(duration).
      - When l(duration) is not specified, the server default is used.
      - Reservations are permanent.
    type: str
    default: reservation
    choices: [ reservation, lease ]
  state:
    description:
      - Specifies the desired state of the DHCP lease or reservation.
    type: str
    default: present
    choices: [ present, absent ]
  ip:
    description:
      - The IPv4 address of the client server/computer.
      - This is a required parameter, if l(mac) is not set.
      - Can be used to identify an existing lease/reservation, instead of l(mac).
    type: str
    required: no
  scope_id:
    description:
      - Specifies the scope identifier as defined by the DHCP server.
      - This is a required parameter, if l(state=present) and the reservation or lease
        doesn't already exist. Not required if updating an existing lease or reservation.
    type: str
  mac:
    description:
      - Specifies the client identifier to be set on the IPv4 address.
      - This is a required parameter, if l(ip) is not set.
      - Windows clients use the MAC address as the client ID.
      - Linux and other operating systems can use other types of identifiers.
      - Can be used to identify an existing lease/reservation, instead of l(ip).
    type: str
  duration:
    description:
      - Specifies the duration of the DHCP lease in days.
      - The duration value only applies to l(type=lease).
      - Defaults to the duration specified by the DHCP server
        configuration.
      - Only applicable to l(type=lease).
    type: int
  dns_hostname:
    description:
      - Specifies the DNS hostname of the client for which the IP address
        lease is to be added.
    type: str
  dns_regtype:
    description:
      - Indicates the type of DNS record to be registered by the DHCP.
        server service for this lease.
      - l(a) results in an A record being registered.
      - l(aptr) results in both A and PTR records to be registered.
      - l(noreg) results in no DNS records being registered.
    type: str
    default: aptr
    choices: [ aptr, a, noreg ]
  reservation_name:
    description:
      - Specifies the name of the reservation being created.
      - Only applicable to l(type=reservation).
    type: str
  description:
    description:
      - Specifies the description for reservation being created.
      - Only applicable to l(type=reservation).
    type: str

author:
- Joseph Zollo (@joezollo)
'''

EXAMPLES = r'''
- name: Ensure DHCP scope is present
  win_dhcp_scope:
    state: present
    name: ZolloVLAN10
    active: true
    description: DHCP Server for VLAN 10
    pool_start: 192.168.100.10
    pool_end: 192.168.100.254
    subnet_mask: 255.255.255.0
    subnet_length: 24
    exclusion_list:
    subnet_delay:
    lease_duration:
    scope_options:
    - router: 192.168.100.1
      parent_domain: home.zollo.net
      dns_servers:
      - 8.8.8.8
      - 8.8.4.4

- name: 
  win_dhcp_scope:

- name: 
  win_dhcp_scope:
'''

RETURN = r'''
scope:
  description: DHCP Scope
  returned: 
  type: dict
  sample: 
    name: 10.0.1.0-vlan1
    scope_id: 10.0.1.0
    subnet_mask: 255.255.255.0
    state: Active
    start_range: 10.0.1.100
    end_range: 10.0.1.199
    lease_duration:
      days: 2
      hours: 48
'''