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


def images(api_ip, api_port, **params):
    """
    list images filtered by parameters

    :api_ip: STRING
    :api_port: INT/STRING
    :**params: optional parameters
        iid: STRING
        tag: STRING
        created: STRING
        repository: STRING
        virtual_size: STRING
        os_type: STRING
        os_version: STRING
    :returns: (
        status: INT    # -1: exception, other: status code
        msg: STRING    # '': success, other: exception message
        result: LIST
    )
    Example result format:
        [
            {u'created': u'222',
              u'id': 1,
              u'iid': u'86ce37374f40',
              u'os_type': None,
              u'os_version': None,
              u'repository': u'ubuntu',
              u'tag': u'latest',
              u'virtual_size': u'192'}
        ]

    """

    url = "http://" + api_ip + ":" + str(api_port) + "/" + API_VERSION + \
        "/images/"
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


def create(api_ip, api_port, iid='', tag='', created='', repository='',
           virtual_size='', os_type='', os_version=''):
    """
    create an image

    :api_ip: STRING
    :api_port: INT/STRING
    :iid: STRING
    :tag: STRING
    :created: STRING
    :repository: STRING
    :virtual_size: STRING
    :os_type: STRING
    :os_version: STRING
    :returns:(
        status: INT    # -1 : exception; other : status code
        msg: STRING    # '' : success; other : exception message
        result: DICT
    )

    Example result format:
        {
            'repository': 'test',
            'os_version': '',
            'created': 'now',
            'iid': '1',
            'tag': 'test',
            'os_type': None,
            'virtual_size': '200',
            'id': 5
        }
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
    get image information by image pk

    :ip: STRING
    :port: STRING
    :pk: STRING
    :returns: (
        status: INT   # -1 : exception; other : status code
        msg: STRING   # '' : success; other : exception message
        result: DICT
    )

    Example result format:
        {
            "id": 1,
            "iid": "5506de2b643b",
            "tag": "14.04.1",
            "created": "3",
            "os_type": null,
            "os_version": null,
            "repository": "ubuntu",
            "virtual_size": "199"
        }

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
