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


def list(api_ip, api_port):
    """
    列出所有flavor

    :api_ip:
    :api_port:
    :returns: (satatus, msg, result)

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


def get_flavor_by_id(api_ip, api_port, id):
    """
    根据id获取flavor

    :api_ip:
    :api_port:
    :id:
    :returns: (status, msg, result)

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/flavors/" + str(id)
    try:
        req = requests.get(url=url)
        result = req.json()
        status = req.status_code
        return (status, '', result)
    except Exception, e:
        return (-1, e, '')
