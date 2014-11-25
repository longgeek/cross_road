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
    列出所有容器

    :api_ip:
    :api_port:
    :**params: 可选参数
        cid, name, host_size, ports,
        image, status, user_id, command,
        created, hostname, flavor_id
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def create(api_ip, api_port, cid='', name='',
           host='', size='', ports='',
           image='', status='', user_id='',
           command='', created='',
           hostname='', flavor_id=''):
    """
    创建容器

    :api_ip:
    :api_port:
    :cid:
    :name:
    :host:
    :size:
    :ports:
    :image:
    :status:
    :user_id:
    :command:
    :created:
    :hostname:
    :flavor_id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/create"
    headers = {'content-type': 'application/json'}
    load = {
        'cid': cid,
        'name': name,
        'host': host,
        'size': size,
        'ports': ports,
        'image': image,
        'status': status,
        'user_id': user_id,
        'command': command,
        'created': created,
        'hostname': hostname,
        'flavor_id': flavor_id}
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(load))
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_container_by_id(api_ip, api_port, id):
    """
    根据容器id获取数据库中容器信息

    :api_ip:
    :api_port:
    :id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(id)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def delete(api_ip, api_port, id):
    """
    删除一个容器

    :api_ip:
    :api_port:
    :id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(id) + "/delete"
    try:
        req = requests.delete(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def stop(api_ip, api_port, id, t=''):
    """
    停止一个容器

    :api_ip:
    :api_port:
    :id:
    :params: 可选查询参数
        t – number of seconds to wait before killing the container
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(id) + "/stop"
    headers = {'content-type': 'application/json'}
    load = {'t': t}
    try:
        req = requests.post(url=url, data=json.dumps(load), headers=headers)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def start(api_ip, api_port, id):
    """
    启动一个容器

    :api_ip:
    :api_port:
    :id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(id) + "/start"
    headers = {'content-type': 'application/json'}
    try:
        req = requests.post(url=url, headers=headers)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def restart(api_ip, api_port, id):
    """
    重启一个容器

    :api_ip:
    :api_port:
    :id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(id) + "/restart"
    headers = {'content-type': 'application/json'}
    try:
        req = requests.post(url=url, headers=headers)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
