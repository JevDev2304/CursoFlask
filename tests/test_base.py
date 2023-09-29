from flask_testing import TestCase
from main import app
from flask import current_app, url_for

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED']= False
        return app
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        expected_location = '/hello'
        self.assertRedirects(response,expected_location)