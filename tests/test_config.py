import unittest

from flask import current_app
from flask_testing import TestCase

from server import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/google_drive'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/google_drive_test'
        )