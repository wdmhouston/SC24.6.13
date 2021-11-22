import os
from flask_restful import Resource, fields, request
from modules.model import model
from utils.restful import *


class api_model_predict(Resource):

    def get(self, image_path=''):
        """Prediction
        ---
        schemes:
          - http
        parameters:
          - name: image_path
            in: path
            type: string
            required: true
            default: ''
            description: image path for prediction

        responses:
          200:
            description: return prediction results
            examples:
                {
                    "image_path":"/app/project/data/upload/xx.jpg"
                }
        """
        image_path = os.path.basename(image_path)
        if image_path == '':
            return fail('image path is empty')

        if not os.path.isfile('/app/project/upload/' + image_path):
            return fail('fail to read image')

        image_path = '/app/project/upload/' + image_path

        model1 = model()
        result = model1.predict(image_path)
        return success("ok", result)
