import json
import numpy as np
import sys
from keras.models import load_model
f = open('data_for_everything')
j = json.load(f)
model = load_model('trained.dat')
all = 0.0
for i in range(1000,1200):
    prediction =  model.predict(np.matrix(j[i]['in'],))
    total = 0.0
    k = int(sys.argv[1])
    res = False
    if prediction[0][k] > 0.5 and j[i]['out'][k] > 0.5:
        res = True
    elif prediction[0][k] <= 0.5 and j[i]['out'][k] <= 0.5:
        res = True
    print res,prediction[0][k],j[i]['out'][k],j[i]['bill']
    total += abs(prediction[0][k]-j[i]['out'][k])
    all += total/len(j[i]['out'])

print 1-(all/200)
