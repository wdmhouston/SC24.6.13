from flask_restful import Resource, fields, request
import modules.model

class apiModelTrain(Resource):
     def get(self):
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
        return success("ApiModelTrain.get success")
