from flask import jsonify, request


def response(status, message):
    errorObject = {
        'status': status,
        'message': message,
        'endpoint': request.url
    }
    errorResponse = jsonify(errorObject)
    errorResponse.status_code = status
    return errorResponse
