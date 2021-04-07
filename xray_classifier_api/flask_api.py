import os
import json
import logging

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

from xray_classifier_api.classifier import classify

app = Flask(__name__)
api = Api(app, doc=False)


@api.route('')
class HealthCheck(Resource):
    def get(self):
        logging.info('Health checking...')
        return jsonify(message='Status ok')


expected_request = api.model('X-ray Image from URL', {'url_image': fields.String('The image URL goes here.')})


@api.route('/predict')
class XrayViewPositionClassifier(Resource):
    @api.expect(expected_request)
    def post(self):
        request_dict = json.loads(request.data)
        view_predicted = classify(request_dict)

        return jsonify(message=f'This is an X-ray with {view_predicted} view position.')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
