.. Fruit Identification Web Api documentation master file, created by
   sphinx-quickstart on Tue Sep 21 14:40:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fruit Prediction Web Api's documentation!
========================================================
Fruit Prediction Web Api is a tool for predicting fruit type from image using deep learning(TensorFlow and Keras).

This tool provdes a standard restful api for prediction. It can also be used to train with new images.

This web api is called by blogapp (https://github.com/wdmhouston/capstone_project_blogapp) to predict any image uploaded through blogapp.
Check blogapp for more details.

.. image:: container.jpg
	:align: center


Please refer the following guide to deploy, test and train the model included in this tool. 

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
