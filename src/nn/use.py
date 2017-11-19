import json
import numpy as np
from keras.models import load_model
f = open('data_for_everything')
j = json.load(f)
model = load_model('trained.dat')
all = 0.0
for i in range(1000,1200):
    prediction =  model.predict(np.matrix(j[i]['in'],))
    total = 0.0
    for k in range(0,len(j[i]['out'])):
        total += abs(prediction[0][k]-j[i]['out'][k])
    all += total/len(j[i]['out'])

print 1-(all/200)
