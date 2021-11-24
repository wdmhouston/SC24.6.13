![index](https://user-images.githubusercontent.com/19333848/143232194-2de2b373-d257-4680-b226-d281abe6f179.jpg)
# Fruit Prediction Using Deep Learning
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

Online docs are available online: https://sc24613.readthedocs.io/en/main/

Try this prediction online: http://35.202.95.240/

Note: 
1. Currently, model is trained with 36 fruits data and more data will be added and trained in future.    
2. When a high probablity(for example, 0.90) is returned, mostlikely, it means the predict result is correct. When trying to predict a untrained fruit type, it's expected to have low probablity.  This probablity critia value can be adjusted to decide the prediction is acceptable or not.
