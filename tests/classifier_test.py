import json

from unittest import TestCase

from xray_classifier_api import flask_api


class FlaskAPItests(TestCase):
    def setUp(self):
        self.client = flask_api.app.test_client()

    def test_view_position_classification(self):
        with open('tests/TestData/request.json', 'r') as _file:
            request = json.load(_file)
        response = self.client.post(
            '/predict',
            data=json.dumps(request)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.data)['message'],
            'This is an X-ray with Lateral (L) view position.'
        )
