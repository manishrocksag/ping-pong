"""
A set of common function which can be used across the application.
"""


from __future__ import absolute_import, print_function, unicode_literals
import json
from collections import namedtuple
import settings

Error = namedtuple('Error', 'status code description')
Response = namedtuple('Response', 'data status')


def date_handler(obj):
    """
        @function: date_handler
        @createdBy: Manish Agarwal
        @createdDate: 7/22/2015
        @lastModifiedBy: Manish Agarwal
        @lastModifiedDate: 08/12/2015
        @type: function
        @param: date
        @purpose - Parse the date object to isoformat so that it
                    can be handled by json
    """
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    else:
        return obj


def create_response(data, additional_info=None):
    if additional_info:
        response = {"data": data, "status": "success"}
        response.update(additional_info)
        return json.dumps(response, default=date_handler, indent=4)
    return json.dumps({"data": data, "status": "success"}, default=date_handler, indent=4)


def error(code, *args):
    desc = ''
    for args in args:
        desc += str(args)
    return json.dumps({"code": code, "description": desc, "status": "failure"})


def load_data():
    with open(settings.DATA_FILE, 'r') as _file:
        return json.loads(_file.read())


def write_data(data):
    with open(settings.DATA_FILE, 'w') as _file:
            _file.write(json.dumps(data))


def load_report_data():
    with open(settings.REPORT_FILE, 'r') as _file:
        return json.loads(_file.read())


def write_report_data(data):
    with open(settings.REPORT_FILE, 'r') as _file:
        loaded_data = json.loads(_file.read())
    _id = len(loaded_data) + 1
    data["tournamnet"] = _id
    loaded_data.append(data)
    with open(settings.REPORT_FILE, 'w') as _file:
            _file.write(json.dumps(loaded_data, indent=4))
