#!/usr/bin/env python
# encoding: utf-8

"""
@Author: Frank
@Email: frank@thstack.com
@Date: 2014.11.25
"""

import simplejson as json
import requests
from exceptions import Exception

API_VERSION = 'v1'


def hosts(api_ip, api_port, **params):
    """
    list hosts filtered by parameters

    :ip: STRING
    :port: STRING
    :params: 可选查询参数
        ip: STRING
        port: STRING
        image: STRING
        status: BOOL
        total_cpu: INT          # Cores
        total_mem: INT          # GB
        total_sys_disk: INT     # GB
        total_volume: INT       # GB
        total_bandwidth: INT    # MB
    :returns: (
        status: INT  -1 : exception; other : status code
        msg: STRING  '' : success; other : exception message
        result: TODO
    )

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/hosts/"
    headers = {'content-type': 'application/json'}
    try:
        req = requests.get(url=url, params=params, headers=headers)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def create(api_ip, api_port, ip='', port='', image='', status='',
           total_cpu='', total_mem='', total_sys_disk='',
           total_volume='', total_bandwidth=''):
    """
    create a host

    :api_ip: STRING
    :api_port: STRING
    :image: STRING
    :status: BOOL
    :total_cpu: INT          # Cores
    :total_mem: INT          # GB
    :total_sys_disk: INT     # GB
    :total_volume: INT       # GB
    :total_bandwidth: INT    # MB
    :returns: (
        status: INT  -1 : exception; other : status code
        msg: STRING  '' : success; other : exception message
        result: TODO
    )

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/host/create"
    headers = {'content-type': 'application/json'}
    load = {
        'ip': ip,
        'port': port,
        'image': image,
        'status': status,
        'total_cpu': total_cpu,
        'total_mem': total_mem,
        'total_sys_disk': total_sys_disk,
        'total_volume': total_volume,
        'total_bandwidth': total_bandwidth}
    try:
        req = requests.post(url=url, data=json.dumps(load), headers=headers)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_host_by_pk(api_ip, api_port, pk):
    """
    get host information by host pk

    :ip: STRING
    :port: STRING
    :pk: STRING
    :returns: (
        status: INT  -1 : exception; other : status code
        msg: STRING  '' : success; other : exception message
        result: TODO
    )

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/hosts/" + str(pk)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
