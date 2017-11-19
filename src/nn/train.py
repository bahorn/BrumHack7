
# based on the keras documentation
# 
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv1D,Activation
from keras import losses, optimizers
import keras.utils as keras_utils
import json

f = open('data_for_everything')
j = json.load(f)

# our parameters
nn_input_size = len(j[0]['in'])
nn_hidden_layer_size = 20
nn_hidden_layers_n = 1
nn_output_layer_size = len(j[0]['out'])

epochs_count = 2000
batch_size = 100

# define the model.
model = Sequential()
model.add(Dense(nn_hidden_layer_size, activation='relu',
    input_shape=(nn_input_size,)))
# hidden layers. we went for three. seems decent.
for i in range(0, nn_hidden_layers_n):
    model.add(Dense(nn_hidden_layer_size, activation='relu',
            input_shape=(nn_hidden_layer_size,)))
# output layer.
model.add(Dense(nn_output_layer_size, activation='relu',
    input_shape=(nn_hidden_layer_size,)))
# compile it.
model.compile(optimizer=optimizers.Adam(),
              loss=losses.binary_crossentropy,
              metrics=['accuracy'])

######
###### LOAD DATA HERE
######
#data = np.empty(shape=(len(j),196))
#labels = np.empty(shape=(len(j),664))
t_data = []
t_label = []
for i in j:
    t_data += [i['in']]
    t_label += [i['out']]

amount_for_training = 1000
data = np.array(t_data[:amount_for_training])
labels = np.array(t_label[:amount_for_training])
test_data = np.array(t_data[amount_for_training:])
test_labels = np.array(t_label[amount_for_training:])

print data
model.fit(data, labels, epochs=epochs_count, batch_size=batch_size)
score = model.evaluate(test_data, test_labels, batch_size=batch_size)
print score
#print j[1001]['bill']
#print t_label[100]
#print model.predict(np.matrix(t_data[1001],))

model.save('trained.dat')
