#!/usr/bin/env python
# encoding: utf-8

"""
@Author: Frank
@Email: frank@thstack.com
@Date: 2014.11.19
"""

import requests
from exceptions import Exception

API_VERSION = 'v1'


def list(ip, port, **params):
    """
    列出images

    :params:可选参数
        all : 1/True/true or 0/False/false, default false
        filters : a json encoded value of the filters (a map[string][]string) \
            to process on the images list.
    :return:DICT
        {
            result:LIST,
            status:BOOL
        }
    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + "/images"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def create(ip, port, iid, tag, created, repository, virtual_size):
    """
    创建一个镜像

    :ip:
    :port:
    :iid:
    :tag:
    :created:
    :os_type:
    :os_version:
    :repository:
    :virtual_size:

    :returns:
    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + \
        "/images/create"
    try:
        load = {'iid': iid,
                'created': created,
                'tag': tag,
                'repository': repository,
                'virtual_size': virtual_size
                }
        req = requests.post(url=url, data=load)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_image_by_pk(ip, port, pk):
    """
    通过pk值获取images

    :ip: TODO
    :port: TODO
    :pk: TODO
    :returns: TODO

    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + "/images/" \
        + str(pk)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def delete(ip, port, pk):
    """
    删除指定pk值的image

    :ip: TODO
    :port: TODO
    :pk: TODO
    :returns: TODO

    """

    url = "http://" + ip + str(port) + "/" + API_VERSION + "/images/" + \
        str(pk) + "/delete"
    try:
        req = requests.put(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
