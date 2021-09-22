# SC24.6.13
Springboard Machine Learning Training Project Unit 24.6.13

Build docker images + Flask WebApi + TensorFlow model

Build docker container:
   docker build -t wdmhouston/sc24.6.13:0.1 .

Run docker container:
   sudo docker run --rm -i -t -v /data/SC24.6.13/project:/app/project wdmhouston/sc24.6.13:0.1


Web API test:
   curl http://172.17.0.2:5000/api/train
   curl http://172.17.0.2:5000/api/predict

Unit Tests:
   ca /app/project
   python -m unittest tests/train.py
   python -m unittest tests/predict.py

Docs are generated using Sphinx, and are available in /app/project/docs/_build folder
