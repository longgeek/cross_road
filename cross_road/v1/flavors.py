#!/usr/bin/env python
# encoding: utf-8

"""
@Author: Frank
@Email: frank@thstack.com
@Date: 2014.11.25
"""


import requests
from exceptions import Exception


API_VERSION = 'v1'


def flavors(api_ip, api_port):
    """
    list all flavors

    :api_ip: STRING
    :api_port: INT/STRING
    :returns: (
        status: INT   # -1 : exception; other : status code
        msg: STRING   # '' : success; other : exception message
        result: DICT
    )

    Example result format:
        {
            '1': {
                     'bandwidth': 512,
                     'cpu': 1,
                     'mem': 128,
                     'name': u'tiny',
                     'sys_disk': 5120,
                     'volume': 0},
            '2': {
                     'bandwidth': 1024,
                     'cpu': 1,
                     'mem': 256,
                     'name': u'small',
                     'sys_disk': 10240,
                     'volume': 0},
            '3': {
                     'bandwidth': 1024,
                     'cpu': 1,
                     'mem': 512,
                     'name': u'standard',
                     'sys_disk': 10240,
                     'volume': 0}
        }
    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/flavors/"
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')


def get_flavor_by_id(api_ip, api_port, db_id):
    """
    get flavor information filtered by flavor_id

    :api_ip: STRING
    :api_port: STRING
    :db_id: STRING
    :returns: (
        status: INT   # -1 : exception; other : status code
        msg: STRING   # '' : success; other : exception message
        result: DICT
    )

    Example result format:
        {
            'bandwidth': 512,
            'cpu': 1,
            'mem': 128,
            'name': u'tiny',
            'sys_disk': 5120,
            'volume': 0
        }

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/flavors/" + str(db_id)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
