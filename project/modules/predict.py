import os
#from PIL import Image
import numpy as np
import tensorflow as tf
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout
from tensorflow.keras.callbacks import EarlyStopping
#from keras.layers.normalization import BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from keras_preprocessing import image

def run_predict_test(model, image_path):
    img = image.load_img(image_path, target_size=(224,224,3))
    #plt.imshow(img)
    #plt.show()
    x = image.img_to_array(img)
    #print(x.shape)
    x = np.expand_dims(x, axis=0)
    #print(x.shape)
    #print(x)
    images = np.vstack([x])
    pred = model.predict(images, batch_size=32)
    print(pred)
    #label = np.argmax(pred, axis=1)
    print("Actual: "+image_path.split("/")[-2])
    print("Predicted: "+class_names[np.argmax(pred)])


path = "/data/SC24.6.12/project/data/data"
dataset = tf.keras.preprocessing.image_dataset_from_directory(path,
                                                               seed=2509,
                                                               image_size=(224, 224),
                                                              batch_size=32)
class_names = dataset.class_names

reconstructed_model = keras.models.load_model("/data/SC24.6.12/project/data/model/model.h5")
path3 = "/data/SC24.6.12/project/data/data3"
image_path=path3 + "/apple/Image_1.jpg"
run_predict_test(reconstructed_model, image_path)
