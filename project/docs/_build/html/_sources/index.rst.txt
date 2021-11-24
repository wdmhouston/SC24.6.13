.. Fruit Prediction Web Api documentation master file, created by
   sphinx-quickstart on Tue Sep 21 14:40:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fruit Prediction Web Api's documentation!
========================================================
Fruit Prediction Web Api is a tool for predicting fruit type from image using deep learning(TensorFlow and Keras).
|
This tool provdes a standard restful api for prediction. It can also be used to train with new images.
|
This web api is called by blogapp (https://github.com/wdmhouston/capstone_project_blogapp) to predict any image uploaded through blogapp.
Check blogapp for more details.
|
The following picture shows how this web api(in red box) works with blogapp to privide Fruit Prediction service to end user.

.. image:: container.jpg
	:align: center

This web api includes a trained model(Please refer to "Train model" for more details) with multiple layers setup shown in the following picture: 

.. image:: model.jpg
	:align: center

|

The following picture shows the accuracy and loss plot from one training:

.. image:: performance.jpg
	:align: center

|
	
A live demo is available in showcase section of my personal website: http://www.wdmhouston.com

The following screenshots show how to predict fruit in blogapp and display the returned json data from this web api.

.. image:: demo1.jpg
	:align: center

.. image:: demo2.jpg
	:align: center

|

The source code of this web api is available in github https://github.com/wdmhouston/capstone_project_fruit_prediction

Please refer the following guide to deploy, train and test this web api service. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   deployment
   accessapi
   trainmodel
   unittest
   


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
