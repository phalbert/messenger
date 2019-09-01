import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class BaseController(object):

    def __init__(self, app, env_vars):
        self.app = app
        self.user = False
        self.request = app.current_request
        self.json_params = self.request.json_body
        self.resource_path = self.request.context['resourcePath']
        self.method = self.request.method
        self.current_path = self.request.to_dict()
        self.config = env_vars
        self.logger = logger
