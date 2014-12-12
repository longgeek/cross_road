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


def containers(api_ip, api_port, **params):
    """
    list containers filtered by parameters

    :api_ip: STRING
    :api_port: INT/STRING
    :**params: optional parameters
        cid: STRING
        name: STRING
        host: STRING
        size: INT       # GB
        ports: INT/STRING
        image: STRING
        status: STRING
        user_id: STRING
        command: STRING
        created: STRING
        hostname: STRING
        flavor_id: STRING
        json_extra: STRING
    :returns: (
        status: INT,            # -1: exception; other: status code
        msg: STRING,            # '': success; other: exception message
        result: LIST or DICT    # success:return LIST;failure: return DICT
    )

    Example result format:
        Success:
            [
                {
                    "id": 14,
                    "cid": "390e90e34656806578a5a86bd12d5f1abc59b58b8be2b65bc
                        f48a410e5536b9b",
                    "size": "0",
                    "host": 1,
                    "name": "/determined_lalande",
                    "image": 1,
                    "ports": "",
                    "status": "Up 36 minutes",
                    "user_id": "2",
                    "command": "/bin/bash",
                    "created": "1417874473",
                    "hostname": "bda51967884c",
                    "flavor_id": "1",
                    "json_extra": ""
                }
            ]
        Failure:
            {"detail": STRING}
    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/"
    try:
        req = requests.get(url=url, params=params)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def create(api_ip, api_port, cid='', name='',
           host='', size='', ports='',
           image='', status='', user_id='',
           command='', created='',
           hostname='', flavor_id='', json_extra=''):
    """
    create a container

    :api_ip: STRING
    :api_port: INT/STRING
    :cid: STRING
    :name: STRING
    :host: STRING
    :size: STRING
    :ports: STRING
    :image: STRING
    :status: STRING
    :user_id: STRING
    :command: STRING
    :created: STRING
    :hostname: STRING
    :flavor_id: STRING 1/2/3
    :json_extra: STRING
    :returns: (
        status: INT    # -1: exception, other: status code
        msg: STRING    # '': success, other: exception message
        result: DICT
    )
    Example result format:
        Success:
            {
                "id": 14,
                "cid": "bda51967884c70b578a5a86bd12d5f1abc59b5
                        8b8be2b65bcf48a410e5536b9b",
                "size": "0",
                "host": 1,
                "name": "/determined_lalande",
                "image": 1,
                "ports": "",
                "status": "Up 41 minutes",
                "user_id": "2",
                "command": "/bin/bash",
                "created": "1417874473",
                "hostname": "bda51967884c",
                "flavor_id": "1",
                "json_extra": "",
            }

        Failure:
            {"detail": STRING}
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
        'flavor_id': flavor_id,
        'json_extra': json_extra}
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(load))
        result = req.json()
        status = req.status_code
        if status == 201:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def get_container_by_id(api_ip, api_port, db_id):
    """
    get container information by container id

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT    #-1 : exception, other : status code
        msg: STRING    #'' : success, other : exception message
        result: DICT
    )
    Example result format:
        Success:
            {
                "id": 14,
                "cid": "bda51967884c70b578a5a86bd12d5f1abc59b
                        58b8be2b65bcf48a410e5536b9b",
                "size": "0",
                "host": 1,
                "name": "/determined_lalande",
                "image": 1,
                "ports": "",
                "status": "Up 6 minutes",
                "user_id": "2",
                "command": "/bin/bash",
                "created": "1417874473",
                "hostname": "bda51967884c",
                "flavor_id": "1",
                "json_extra": ""
            }
        Failure:
            {"detail": STRING}
    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/"
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def delete(api_ip, api_port, db_id):
    """
    delete a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/delete"
    try:
        req = requests.delete(url=url)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def stop(api_ip, api_port, db_id, t=''):
    """
    stop a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :params: optional parameters
        t: INT-number of seconds to wait before killing the container
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/stop"
    headers = {'content-type': 'application/json'}
    load = {'t': t}
    try:
        req = requests.post(url=url, data=json.dumps(load), headers=headers)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def start(api_ip, api_port, db_id):
    """
    start a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/start"
    headers = {'content-type': 'application/json'}
    try:
        req = requests.post(url=url, headers=headers)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def restart(api_ip, api_port, db_id):
    """
    restart a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/restart"
    headers = {'content-type': 'application/json'}
    try:
        req = requests.post(url=url, headers=headers)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def excute(api_ip, api_port, db_id='', command=''):
    """
    excute a command inside a running container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :command: STRING
    :returns: (
        status: INT,    # -1: exception, other: status code
        msg: STRING,    # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/exec"
    headers = {'content-type': 'application/json'}
    load = {'command': command}
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(load))
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def pause(api_ip, api_port, db_id):
    """
    pause a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """
    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/pause"
    try:
        req = requests.post(url=url)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def unpause(api_ip, api_port, db_id):
    """
    unpause a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {"detail": STRING}
        Failure:
            {"detail": STRING}

    """
    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/unpause"
    try:
        req = requests.post(url=url)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def top(api_ip, api_port, db_id):
    """
    list all processes inside a container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :returns: (
        status: INT,            # -1: exception, other: status code
        msg: STRING,            # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
        {
            "cid": "bda51967884c70b578a5a86bd12d5f1abc59b58b
                    8be2b65bcf48a410e5536b9b",
            "titles":[
                    "USER",
                    "PID",
                    "%CPU",
                    "%MEM",
                    "VSZ",
                    "RSS",
                    "TTY",
                    "STAT",
                    "START",
                    "TIME",
                    "COMMAND"
                    ],
            "processes":[
                    ["root","20147","0.0","0.1","18060",
                    "1864","pts/4","S","10:06","0:00","bash"],
                    ["root","20271","0.0","0.0","4312",
                    "352","pts/4","S+","10:07","0:00","sleep","10"]
            ]
        }
        Failure:
            {"detail": STRING}

    """
    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/top"
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')


def console(api_ip, api_port, db_id='', command='', username=''):
    """
    console container

    :api_ip: STRING
    :api_port: INT/STRING
    :db_id: STRING
    :command: STRING
    :username: STRING
    :returns: (
        status: INT,    # -1: exception, other: status code
        msg: STRING,    # '': success, other: exception message
        result: DICT
    )

    Example result format:
        Success:
            {
                "id": "10",
                "cid": "779bfb2bebb079ae80f7686c642cb83df9ae
                        b51b3cd139fc050860f362def2ed",
                "host": "192.168.8.8",
                "username": "longgeek",
                "console": {
                    "/bin/bash": {
                        "private_port": 4301,
                        "public_port": 49187
                    }
                },
            }

        Failure:
            {"detail": STRING}

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/containers/" + str(db_id) + "/console"
    headers = {'content-type': 'application/json'}
    load = {'command': command, 'username': username}
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(load))
        result = req.json()
        status = req.status_code
        if status == 200:
            return (0, '', result)
        else:
            return (status, result, '')
    except Exception, e:
        return (-1, e, '')
