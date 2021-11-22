import os
from PIL import Image
import numpy as np
import tensorflow as tf
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from keras.layers import BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing import image

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # or any {'0', '1', '2'}


class model(object):
    """main class for model training and prediction"""

    _model_path = "/app/project/data/model"
    """model.h5 folder"""

    _traindata_path = "/app/project/data/train"
    """raining data folder"""

    _validationdata_path = "/app/project/data/validation"
    """validation data folder"""

    _testdata_path = "/app/project/data/test"
    """test data folder. """

    _model = None
    """trained model"""

    _class_labels = []

    def __init__(self):
        """suppress tf2.0 warning messages"""
        tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

        """get class labels"""
        dataset = tf.keras.preprocessing.image_dataset_from_directory(
            self._traindata_path, seed=40, image_size=(224, 224), batch_size=32
        )
        self._class_labels = dataset.class_names

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def train(self):
        """train model from data folders"""
        dataset = tf.keras.preprocessing.image_dataset_from_directory(
            self._traindata_path, seed=40, image_size=(224, 224), batch_size=32
        )
        dataset2 = tf.keras.preprocessing.image_dataset_from_directory(
            self._validationdata_path,
            seed=40,
            image_size=(224, 224),
            shuffle=False,
            batch_size=32,
        )
        self._model = Sequential()
        self._model.add(
            Conv2D(32,
                   kernel_size=(3, 3),
                   activation="relu",
                   input_shape=(224, 224, 3))
        )
        self._model.add(MaxPooling2D(pool_size=(2, 2)))
        self._model.add(BatchNormalization())
        self._model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
        self._model.add(MaxPooling2D(pool_size=(2, 2)))
        self._model.add(BatchNormalization())
        self._model.add(Dropout(0.2))
        self._model.add(Flatten())
        self._model.add(Dense(128, activation="relu"))
        self._model.add(Dense(len(self._class_labels), activation="softmax"))

        self._model.compile(
            loss=tf.keras.losses.SparseCategoricalCrossentropy(),
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            metrics=["accuracy"],
        )
        self._model.summary()

        history = self._model.fit(x=dataset,
                                  epochs=20,
                                  validation_data=dataset2)
        self._model.save(self._model_path + "/model.h5")
        message = "model trained. model is saved to " + \
            self._model_path + \
            "/model.h5"
        return message

    def predict(self, image_path):
        """predict from existing model"""
        self._model = keras.models.load_model(self._model_path + "/model.h5")
        if self._model is None:
            return "model error"
        targetImage = image.load_img(image_path, target_size=(224, 224, 3))
        imageArray = image.img_to_array(targetImage)
        x = np.expand_dims(imageArray, axis=0)
        images = np.vstack([x])
        pred = self._model.predict(images, batch_size=32)
        return {
            "image": image_path,
            "result": self._class_labels[np.argmax(pred)]
            }
        """return "actural object: " + image_path.split("/")[-2]
        + '   predicted object:' + self._class_labels[np.argmax(pred)]
        """
