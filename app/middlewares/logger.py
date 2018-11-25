from flask import Request


class LoggingMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        print('Request! Path: %s, Url: %s' % (request.path, request.url))
        return self.app(environ, start_response)
