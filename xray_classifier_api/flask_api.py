import json

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

from classifier import classify

app = Flask(__name__)
api = Api(app, doc=False)

expected_request = api.model('X-ray Image from URL', {'url_image': fields.String('The image URL goes here.')})


@api.route('/helloworld')
class HelloWorld(Resource):
    def get(self):
        return jsonify(message='Hello world!')


@api.route('/predict')
class XrayViewPositionClassifier(Resource):
    @api.expect(expected_request)
    def post(self):
        request_dict = json.loads(request.data)
        view_predicted = classify(request_dict)

        return jsonify(message=f'This is an X-ray with {view_predicted} view position.')


def create_app():
    return app.run(host='0.0.0.0', port=5005)
