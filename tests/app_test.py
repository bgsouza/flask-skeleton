import unittest
import json

from app import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app #create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    # def tearDown(self):
    #     pass

    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_not_found_404_code(self):
        response = self.client.get('/wrong/url',
                                   headers=self.get_api_headers())

        self.assertEqual(response.status_code, 404)