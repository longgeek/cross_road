#!/usr/bin/env python
# encoding: utf-8

"""
@Author: Frank
@Email: frank@thstack.com
@Date: 2014.11.19
"""

import simplejson as json
import requests
from exceptions import Exception

API_VERSION = 'v1'


def list(api_ip, api_port, **params):
    """
    列出所有镜像

    :api_ip:
    :api_port:
    :**params: 可选查询参数
        iid, tag, created, repository,
        virtual_size, os_type,os_version
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/images/"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def create(api_ip, api_port, iid='', tag='', created='', repository='',
           virtual_size='', os_type='', os_version=''):
    """
    创建一个镜像

    :api_ip:
    :api_port:
    :iid:
    :tag:
    :created:
    :repository:
    :virtual_size:
    :os_type:
    :os_version:
    :returns:(status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/images/create"
    headers = {'content-type': 'application/json'}
    load = {
        'iid': iid,
        'tag': tag,
        'created': created,
        'repository': repository,
        'virtual_size': virtual_size,
        'os_type': os_type,
        'os_version': os_version}
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(load))
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_image_by_pk(api_ip, api_port, pk):
    """
    通过pk值获取images

    :ip: TODO
    :port: TODO
    :pk: TODO
    :returns: TODO

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + "/images/" \
        + str(pk)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
