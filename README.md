![index](https://user-images.githubusercontent.com/19333848/143232194-2de2b373-d257-4680-b226-d281abe6f179.jpg)
# Fruit Prediction with Deep Learning
Springboard Machine Learning Career Track (May 2020, Deming Wang) - Capstone Project

Fruit Prediction Web Api is a tool for predicting fruit type from images with deep learning(TensorFlow and Keras). 

This tool provdes a standard restful api for prediction. It can also be used to train with new images. 
This web api is called by blogapp (https://github.com/wdmhouston/capstone_project_blogapp) to predict any image uploaded through blogapp. The following picture shows how this web api(in red box) works with blogapp to privide Fruit Prediction service to end user.

![container](https://user-images.githubusercontent.com/19333848/143234426-59a050f4-13a3-4a9b-86cf-d57c06b098d6.jpg)

This web api includes a pre-trained model(Please refer to “Train model” for more details) with multiple layers setup shown in the following picture:
![model](https://user-images.githubusercontent.com/19333848/143234443-c936edfc-a17c-4b32-afab-dd9042e09e43.jpg)

The following picture shows the accuracy and loss plot from one training:
![performance](https://user-images.githubusercontent.com/19333848/143234450-8ad7b1b4-44ec-486a-b318-211ed1570172.jpg)

A live demo is available in showcase section of my personal website: http://www.wdmhouston.com

The following screenshots show how to predict fruit in blogapp and display the returned json data from this web api.
![demo1](https://user-images.githubusercontent.com/19333848/143234432-6ba1c085-da82-4a17-8504-a5936f4fefc2.jpg)
![demo2](https://user-images.githubusercontent.com/19333848/143234438-2cf35f26-c4f2-4009-9903-50217d109272.jpg)

## Links:
1. Project presentation slides:
https://github.com/wdmhouston/capstone_project_fruit_prediction/blob/main/Capstone_Project_Fruit_Prediction.pptx

2. Fruit Prediction with Deep Learning source code:
https://github.com/wdmhouston/capstone_project_fruit_prediction

3. Demon App source code:
https://github.com/wdmhouston/capstone_project_blogapp

4. Online Documentations for deployment, train, test, unit test 
https://sc24613.readthedocs.io/en/main/

## Note:

The dataset used in this demo is downloaded from https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a This dataset contains most popular fruits.

In future, more and more fruit images will be added for more acccurate prediction, for example, Asian pear/European pear, li jujupe/lang jujupe.

