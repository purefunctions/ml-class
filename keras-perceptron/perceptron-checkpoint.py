import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.callbacks import ModelCheckpoint
from keras.layers import Dropout
from keras.utils import np_utils
from keras.optimizers import SGD
# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
img_width = X_train.shape[1]
img_height = X_train.shape[2]

X_train = X_train.astype('float32')
X_train /= 255.
X_test = X_test.astype('float32')
X_test /= 255.

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
num_classes = y_train.shape[1]

y_test = np_utils.to_categorical(y_test)

# create model
model=Sequential()
model.add(Flatten(input_shape=(img_width,img_height)))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

checkpoint = ModelCheckpoint('model', monitor='val_acc', verbose=1, save_best_only=True, mode='max')

# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), callbacks=[checkpoint])
