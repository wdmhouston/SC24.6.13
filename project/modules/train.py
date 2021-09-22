import os
from PIL import Image
import numpy as np
import tensorflow as tf
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout
from keras_preprocessing import image
from tensorflow.keras.callbacks import EarlyStopping
#import matplotlib.pyplot as plt
#from keras.layers.normalization import BatchNormalization
from keras.layers import BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator

path = "/data/SC24.6.12/project/data/data"
path2 = "/data/SC24.6.12/project/data/data2"
dataset = tf.keras.preprocessing.image_dataset_from_directory(path,
                                                               seed=2509,
                                                               image_size=(224, 224),
                                                              batch_size=32)
dataset2 = tf.keras.preprocessing.image_dataset_from_directory(path2,
                                                              seed=2509,
                                                              image_size=(224, 224),
                                                              shuffle=False,
                                                              batch_size=32)

class_names = dataset.class_names
print(len(class_names))

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(224,224,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
#model.add(Dropout(0.3))
model.add(Dense(len(class_names),activation='softmax'))

model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics = ["accuracy"])
model.summary()

history = model.fit(x=dataset,
                    epochs= 20,
                    validation_data=dataset2)

model.save('newmodel.h5')

def run_test(image_path):
    img = image.load_img(image_path, target_size=(224,224,3))
    #plt.imshow(img)
    #lt.show()
    x = image.img_to_array(img)
    #print(x.shape)
    x = np.expand_dims(x, axis=0)
    #print(x.shape)
    #print(x)
    images = np.vstack([x])
    pred = model.predict(images, batch_size=32)
    #label = np.argmax(pred, axis=1)
    print("Actual: "+image_path.split("/")[-2])
    print("Predicted: "+class_names[np.argmax(pred)])

path3 = "/data/SC24.6.12/project/data/data3"
image_path=path3 + "/apple/Image_1.jpg"
run_test(image_path)
