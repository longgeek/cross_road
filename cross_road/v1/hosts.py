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


def list(api_ip, api_port, **params):
    """
    列出所有主机

    :ip:
    :port:
    :params: 可选查询参数
        ip, port, image, status,
        total_cpu, total_mem,
        total_sys_disk, total_volume,
        total_bandwidth
    :returns: (status, msg, result)

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
    创建一个主机

    :api_ip:
    :api_port:
    :image:
    :status:
    :total_cpu:
    :total_mem:
    :total_sys_disk:
    :total_volume:
    :total_bandwidth:
    :returns: (status, msg, result)

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
    根据pk获取主机信息

    :ip:
    :port:
    :pk:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/hosts/" + str(pk) + "/"
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
