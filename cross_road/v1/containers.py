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
    列出所有containers

    params:可选参数
        all   :1/True/true or 0/False/false, Show all containers. Only running
               containers are shown by default (i.e., this defaults to false)
        limit :Show limit last created containers, include non-running ones.
        since :Show only containers created since Id, include non-running ones.
        before:Show only containers created before Id,include non-running ones.
        size  :1/True/true or 0/False/false, Show the containers sizes
    return:DICT
        {
            result:LIST,
            status:BOOL
        }
    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + "/containers"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = str(req.status_code)
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_info_by_cid(ip, port, cid):
    """TODO: Docstring for get_info_by_cid.

    :ip: TODO
    :port: TODO
    :cid: TODO
    :returns: TODO

    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + \
        "/containers/" + str(cid)
    load = {'cid': cid}
    try:
        req = requests.get(url=url, data=load)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def create(ip, port, image, user_id, flavor_id):
    """TODO: Docstring for create.

    :ip: TODO
    :port: TODO
    :image: TODO
    :user_id: TODO
    :flavor_id: TODO
    :returns: TODO

    """

    url = "http://" + ip + ":" + str(port) + "/" + API_VERSION + \
        "/containers" + "/create"
    load = {'image': image, 'user_id': user_id, 'flavor_id': flavor_id}
    try:
        req = requests.post(url=url, data=load)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def delete(ip, port, cid):
    """TODO: Docstring for delete.

    :ip: TODO
    :port: TODO
    :cid: TODO
    :returns: TODO

    """

    url = "http://" + ip + str(port) + "/" + API_VERSION + str(cid) + "/delete"
    load = {'cid': cid}
    try:
        req = requests.delete(url=url, data=load)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
