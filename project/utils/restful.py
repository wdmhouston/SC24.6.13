from flask import jsonify

class apiServiceCode(object):
    ok = 0
    fail = 1

def restful_result(code, message, data={}):
    return jsonify({"code": code, "message": message, "data": data or {}})

def success(message="", data=None):
    """
    正确返回
    :return:
    """
    return restful_result(code=apiServiceCode.ok, message=message, data=data)

def fail(message="", data=None):
    """
    正确返回
    :return:
    """
    return restful_result(code=apiServiceCode.fail, message=message, data=data)

