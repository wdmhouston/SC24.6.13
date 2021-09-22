.. _UnitTest:

###############################
Unit Test
###############################

Two unit test scripts has already been included: train.py and predict.py. These two scripts are used to train model and run prediction.

To run unit tests, run container with /bin/bash command,

.. code-block:: sh

	$docker run --rm -i -t -v /data/SC24.6.13/project:/app/project wdmhouston/sc24.6.13:0.1 /bin/bash


Train model
==============================

Go to /app/project folder and run unit test for train model,

.. code-block:: sh

	python -m unittest tests/train.py
	

for example,

.. code-block:: sh

	root@8cab2c621396:/app:cd /app/project/
	root@8cab2c621396:/app/project# python -m unittest tests/train.py
	Found 180 files belonging to 3 classes.
	Found 180 files belonging to 3 classes.
	Found 29 files belonging to 3 classes.
	Model: "sequential"
	_________________________________________________________________
	Layer (type)                 Output Shape              Param #
	=================================================================
	conv2d (Conv2D)              (None, 222, 222, 32)      896
	_________________________________________________________________
	max_pooling2d (MaxPooling2D) (None, 111, 111, 32)      0
	_________________________________________________________________
	batch_normalization (BatchNo (None, 111, 111, 32)      128
	_________________________________________________________________
	...
	...
	Epoch 16/20
	6/6 [==============================] - 9s 1s/step - loss: 0.0135 - accuracy: 0.9944 - val_loss: 25.0667 - val_accuracy: 0.6207
	Epoch 17/20
	6/6 [==============================] - 9s 1s/step - loss: 0.0618 - accuracy: 0.9944 - val_loss: 21.6596 - val_accuracy: 0.7241
	Epoch 18/20
	6/6 [==============================] - 9s 1s/step - loss: 0.0192 - accuracy: 0.9889 - val_loss: 21.9505 - val_accuracy: 0.7241
	Epoch 19/20
	6/6 [==============================] - 9s 1s/step - loss: 0.2131 - accuracy: 0.9889 - val_loss: 17.6200 - val_accuracy: 0.7241
	Epoch 20/20
	6/6 [==============================] - 9s 1s/step - loss: 0.0293 - accuracy: 0.9889 - val_loss: 11.5269 - val_accuracy: 0.7931
	model trained. model is saved to /app/project/data/model/model.h5
	
	----------------------------------------------------------------------
	Ran 0 tests in 0.000s
	
	OK


Predict
==============================

Go to /app/project folder and run unit test for prediction,

.. code-block:: sh

	python -m unittest tests/predict.py
	

for example,
	
.. code-block:: sh

	root@8cab2c621396:/app# cd /app/project
	root@8cab2c621396:/app/project# python -m unittest tests/predict.py
	Found 180 files belonging to 3 classes.
	{'image': '/app/project/data/data3/apple/Image_1.jpg', 'result': 'apple'}
	
	----------------------------------------------------------------------
	Ran 0 tests in 0.000s
	
	OK
	
.. note::
   Train model only when needed.
   
   After training model, model file "model.h5" will be created in /app/project/data/model folder. 
   
   The trained model file "model.h5" can be shared with different containers.
