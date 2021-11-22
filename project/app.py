from flask import Flask
from flask_restful import Api
from flasgger import Swagger
import config
from utils.restful import *
from modules.api_model_predict import api_model_predict

"""Flask app"""
app = Flask(__name__)
api = Api(app)
api.add_resource(api_model_predict,
                 '/api/predict',
                 '/api/predict/',
                 '/api/predict/<string:image_path>'
                 )

"""Swagger API Document"""
swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = config.SWAGGER_TITLE
swagger_config['description'] = config.SWAGGER_DESC
swagger_config['host'] = config.SWAGGER_HOST
swagger = Swagger(app, config=swagger_config)

"""404 error"""
@app.errorhandler(404)
def page_not_found(e):
    return restful_result(404, 'page does not exist')

"""run app"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
