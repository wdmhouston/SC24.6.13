.. _Depolyment:

###############################
Deployment Guide
###############################

The goal of this page is to help you deploy this tool
We will walk you through downloading the source, compiling the code, and testing the installation.

Repository
==============================

The source for this Fruit Identification Web Api and related tools are hosted on `Github <https://github.com>`_.
https://github.com/wdmhouston/capstone_project_fruit_prediction

Download
======================

It is possible to directly download the source code as a zip file.
We strongly suggest, however, that users don't rely on this option.
Instead, most users should use Git to either *clone* or *fork* the repository.
This makes it much easier to stay up to date with the latest releases and bug fixes.
If you are not familiar with the basics of Git, `here is a helpful resource <https://git-scm.com>`_ to get you started.

The tutorial here assumes you will use a https clone with no specific credentials.

If you do not already have Git installed on your system, you will need to install it.
We recommend using a relatively recent version of Git, as there have been some notable improvements over the past few years.
You can check if Git is already available by opening a terminal and typing

.. code-block:: sh

  git --version

To download, run the following git clone command:

git clone with https:

.. code-block:: sh

  git colone https://github.com/wdmhouston/capstone_project_fruit_prediction.git
  

git clone with ssh:

.. code-block:: sh

  git clone git@github.com:wdmhouston/capstone_project_fruit_prediction.git


git clone with GitHub CLI:

.. code-block:: sh

   gh repo clone wdmhouston/capstone_project_fruit_prediction
   

In this example,  we run the git clone command in folder /data, and we should get the following structure: 
  
.. code-block:: sh

  capstone_project_fruit_prediction/
  ├── README.md/
  ├── requirements.txt/
  ├─┬─  project/
  │ ├── __init__.py
  │ ├── _app.py
  │ ├── __init__.py
  │ ├── config.py
  │ ├── modules
  │ ├── utils
  │ ├── data
  │ │   ├──model  
  │ │   ├──train 
  │ │   ├──validation 
  │ │   └──test   
  │ ├── upload
  │ ├── docs
  │ └── tests/
  └── Dockerfile/
  
where the Dockerfile and requirements.txt are provided to build a docker container with all components configured.

Build
======================

First, using a terminal, build the downloaded docker container. 

.. code-block:: sh

  cd capstone_project_fruit_prediction
  deming@ml-instance:/data/capstone_project_fruit_prediction$ docker build -t wdmhouston/capstone_project_fruit_prediction:0.1 .
  Sending build context to Docker daemon  242.9MB
  Step 1/6 : FROM tensorflow/tensorflow:2.6.0
   ---> 94fc08a3795e
  Step 2/6 : COPY ./requirements.txt /app/requirements.txt
   ---> Using cache
   ---> 5a50c951040e
  Step 3/6 : WORKDIR /app
   ---> Using cache
   ---> f4f64125c894
  Step 4/6 : RUN pip install -r requirements.txt
   ---> Using cache
   ---> 7faffa6d685e
  Step 5/6 : EXPOSE 5000
   ---> Using cache
   ---> cb9b49b580a2
  Step 6/6 : CMD python /app/project/app.py
   ---> Using cache
   ---> 2a120c3ab376
  Successfully built 2a120c3ab376
  Successfully tagged wdmhouston/sc24.6.13:0.1

  
where wdmhouston/capstone_project_fruit_prediction:0.1 can be modified as your own name and version.

Train
======================
Second, train model to generate /app/project/data/model/model.h5 file. This file is needed for prediction. Please refer "unit test" chapter to train model.

Run
======================

Third, run the docker container:

.. code-block:: sh

    deming@ml-instance:/data/capstone_project_fruit_prediction$ sudo docker run --rm -i -t -v /data/capstone_project_fruit_prediction/project:/app/project -v /apps/blog/web/image/upload:/app/project/upload -p 5000:5000 wdmhouston/capstone_project_fruit_prediction:0.1
    * Serving Flask app 'app' (lazy loading)
    * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
    * Debug mode: on
    * Running on all addresses.
      WARNING: This is a development server. Do not use it in a production deployment.
    * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 108-387-964

where wdmhouston/capstone_project_fruit_prediction:0.1 can be replaced with your own name and version.

If all goes well, you should have a complete copy of the this Fruit Idntification Web api and the api service is running.

.. note::
	This train model is only needed once to generate model.h5 file. After that, trained model will be used for prediction.
	
	If deployment fails, there is likely something wrong with your installation.
   
	If you find something is wrong, please consider posting an issue to our issue tracker (https://github.com/wdmhouston/capstone_project_fruit_prediction/issues) .
