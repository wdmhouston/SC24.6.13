.. _TrainModel:

###############################
Train model
###############################

The out-of-box container has already included a trained model for immediate use. When more images are added to training/validation data folder, the model can be retrained.

Train model
==============================

To train model, first, launch a new train container or using existing container with /bin/bash command, for example,

.. code-block:: sh

	$docker run --rm -i -t -v /data/SC24.6.13/project:/app/project wdmhouston/sc24.6.13:0.1 /bin/bash
	

second, run the train unit test,

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

.. note::
   Train model only when needed.
   
   It is recommended to run in a seperated container to train model. The trained model file "model.h5" can be shared with different containers.
