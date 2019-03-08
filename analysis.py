
#from sklearn.preprocessing import Imputer
from flatten_json import flatten
#import ijson
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.metrics import accuracy_score
import sklearn.metrics
from matplotlib import pyplot as py
from sklearn.model_selection import train_test_split
import sklearn
import os
#from sklearn.ensemble import RandomForestRegressor 
#from sklearn.naive_bayes import GaussianNB
#from sklearn.ensemble import RandomForestClassifier
#import jsonlines
import json
#import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from pandas.io.json import json_normalize
data = []
new_data = []
count_0 = 0
count_1 = 0
with open("data") as f:
   for line in f:
       data.append(json.loads(line))
for i in range(len(data)):
   del data[i]['sha256']
   del data[i]['histogram'] 
   del data[i]['byteentropy']
   del data[i]['strings']['printabledist']
   del data[i]['exports']
   del data[i]['header']['coff']['characteristics']
   del data[i]['header']['optional']['dll_characteristics']
   del data[i]['imports']
   del data[i]['appeared']
   for j in range(len(data[i]['section']['sections'])):
      del data[i]['section']['sections'][j]['props']   
for i in range(70000):
    if(data[i]['label'] != -1):
      new_data.append(data[i])
    if(data[i]['label'] == 0):
      count_0 += 1
    if(data[i]['label'] == 1):
      count_1 += 1
    
    
