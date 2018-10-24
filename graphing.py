# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing libraries
from sklearn.preprocessing import Imputer
from sklearn.metrics import accuracy_score
from flatten_json import flatten
#import ijson
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.ensemble import RandomForestRegressor 
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
#import jsonlines
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.json import json_normalize
#json extraction
filename = "train_features_0.jsonl"
data = []
new_data = []
#new_data = []
with open(filename) as f:
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
flattened_json = (flatten(d) for d in data)# denesting json
#for i in range(len(data[0]['section']['sections'])):
#new_data[0]['section']['sections']['name1'].append(data[0]['section']['sections'][0]['name'])
#new_data.append(data[i]['section'])
#for i in range(len(data)):
#    for p in range(10):
#        new_data.append(data[i]['section']['sections'][p])

#df = json_normalize(data)
#df2 = json_normalize(df, record_path = 'section.sections',errors='ignore')
df1 = pd.DataFrame(flattened_json)#initial dataframe
#imp = Imputer(missing_values = 'NaN', strategy = '0', axis = '0')
#imp.fit(df1)
#df1 = imp.trandorm(df1)
df1.fillna(0, inplace=True)# filling NaN values with 0
#df2 = json_normalize(data,'sections',['data'],errors='ignore')
dummy = pd.get_dummies(df1) #dealing with categorical values
df2 = pd.DataFrame(dummy) #final dataframe
labels = np.array(df2['label'])
#df2 = df2.drop('label',axis = 1)
feature_list = list(df2.columns)
benign = df2['label'].groupby('0').count()
df2 = np.array(df2)
train_features, test_features, train_labels, test_labels = train_test_split(df2, labels, test_size = 0.25, random_state = 42)
model = XGBClassifier()
#rf = RandomForestClassifier(oob_score=True, n_estimators=1000)
model.fit(train_features,train_labels)
#predicted = model.predict(test_labels)
#print(model)
y_pred = model.predict(test_features)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(test_labels,predictions)
#print("Accuracy: %.2f%%" %(accuracy * 100.0))
#np.array(rf.feature_importances_))
#print(sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), feature_list), reverse=True))
#predicts = rf.predict(test_features)
#accuracy = accuracy_score(test_labels,predicts)
#print(accuracy)
#rf.score(test_features,test_labels)
#df1 = pd.concat([df1,dummy],axis=1)
#df1 = np.array(df1)
#df1 = pd.DataFrame(df)
#print(data[1])
#df_2 = pd.DataFrame(data='df' , columns = 'True')
#optional_subsystem
#header.machine
#print(df[1])
#with open(filename) as f:
#    dict_train = json.loads(f)
#train = pd.dataFrame.from_dict(dict_train, orient = 'index')
#train.reset_index(level = 0,implace = 'True')
#data[1]['section']['entry'] #entrypoint
#data[19999]['section']['sections'][0]['name']
#data[19999]['section']['sections'][0]['entropy']
#data[19999]['section']['sections'][1]['name']
#data[19999]['section']['sections'][1]['entropy']
#data[19999]['section']['sections'][2]['name']
#data[19999]['section']['sections'][2]['entropy']
#data[19999]['label']#VERIFIES IF SAMPLE IS BENIGN OR MALICIOUS OR UNLABELLED
#pq = json.dumps(data[1])

print(benign)
#get graphs for dates
#samples
#entry points
#labels
#objects = ('Labelled', 'Unlabelled', 'Neutral')
#y_pos = np.arange(len(objects))
#labelled_count = pd.value_counts(df2['label'].values(0), sort=False)
#unlabelled_count = pd.value_counts(df2['label'].values(1), sort=False)
#neutral = pd.value_counts(df2.label.values(-1), sort=False)
#performance = [labelled_count, unlabelled_count, neutral]
#plt.xticks(y_pos,objects)
#plt.ylabel('No Of Instance')
#plt.title('Distribution of Malware')
#plt.show()