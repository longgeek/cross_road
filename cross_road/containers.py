#!/usr/bin/env python
# encoding: utf-8

"""
@Author: Frank
@Email: frank@thstack.com
@Date: 2014.11.19
"""

import json
import requests
from exceptions import Exception


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

    url = "http://" + ip + ":" + str(port) + "/containers/json"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = str(req.status_code)
        return dict(result=result, status=status)
    except Exception, e:
        return e


def create(ip, port, image, cmd, **params):
    """
    创建新的containers
    """

    url = "http://" + ip + ":" + str(port) + "/containers/create"
    data = dict(Image=image, Cmd=cmd)
    headers = {'content-type': 'application/json'}
    try:
        req = requests.post(url=url, data=json.dumps(data), headers=headers,
                            params=params)
        container_id = req.json()['Id']
        status = str(req.status_code)
        status_dict = {
            '201': 'status code 201: no error',
            '404': 'status code 404: no such container',
            '406': 'status code 406: impossible to attach(container not \
                    running',
            '500': 'status code 500: server error'
        }
        return dict(container_id=container_id, status=status_dict[status])
    except Exception, e:
        return e


def inspect(ip, port, id_or_cname, **params):
    """返回指定container的基本信息"""

    url = "http://" + ip + ":" + str(port) + "/containers/" + id_or_cname + \
        "/json"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = str(req.status_code)
        status_dict = {
            '200': 'status code 200: no error',
            '404': 'status code 404: no such container',
            '500': 'status code 500: server error'
        }
        return dict(result=result, status=status_dict[status])
    except Exception, e:
        return e


def list_process_inside_a_container(ip, port, id_or_cname, **params):
    url = "http://" + ip + ":" + str(port) + "/containers/" + id_or_cname + \
        "/top"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = str(req.status_code)
        status_code = {
            '200': 'status code 200: no error',
            '404': 'status code 404: no such containers',
            '500': 'status code 500: server error'
        }
        return dict(result=result, status=status_code[status])
    except Exception, e:
        return e
