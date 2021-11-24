![index](https://user-images.githubusercontent.com/19333848/143232194-2de2b373-d257-4680-b226-d281abe6f179.jpg)
# Fruit Prediction with Deep Learning
Springboard Machine Learning Career Track (May 2020, Deming Wang) - Capstone Project

Fruit Prediction Web Api is a tool for predicting fruit type from images with deep learning(TensorFlow and Keras). 

This tool provdes a standard restful api for prediction. It can also be used to train with new images. 
This web api is called by blogapp (https://github.com/wdmhouston/capstone_project_blogapp) to predict any image uploaded through blogapp. Check blogapp for more details. | The following picture shows how this web api(in red box) works with blogapp to privide Fruit Prediction service to end user.

![container](https://user-images.githubusercontent.com/19333848/143234426-59a050f4-13a3-4a9b-86cf-d57c06b098d6.jpg)

This web api includes a trained model(Please refer to “Train model” for more details) with multiple layers setup shown in the following picture:
![model](https://user-images.githubusercontent.com/19333848/143234443-c936edfc-a17c-4b32-afab-dd9042e09e43.jpg)

The following picture shows the accuracy and loss plot from one training:
![performance](https://user-images.githubusercontent.com/19333848/143234450-8ad7b1b4-44ec-486a-b318-211ed1570172.jpg)

A live demo is available in showcase section of my personal website: http://www.wdmhouston.com

The following screenshots show how to predict fruit in blogapp and display the returned json data from this web api.
![demo1](https://user-images.githubusercontent.com/19333848/143234432-6ba1c085-da82-4a17-8504-a5936f4fefc2.jpg)
![demo2](https://user-images.githubusercontent.com/19333848/143234438-2cf35f26-c4f2-4009-9903-50217d109272.jpg)


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

