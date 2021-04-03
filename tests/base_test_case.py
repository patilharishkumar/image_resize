from flask import current_app
from flask_testing import TestCase

from app import create_app


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app('app.config.TestingConfig')

    def setUp(self):
        self.logger = current_app.logger
        self.logger.info('Test execution started')

    def tearDown(self):
        self.logger.info('Test execution finished')
