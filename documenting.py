# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:57:09 2018

@author: Mani
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing libraries
#import ijson
#import jsonlines
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#json extraction
filename = "train_features_0.jsonl"
data = []
with open(filename) as f:
    for line in f:
       data.append(json.loads(line))
for i in range(len(data)):
  data[i]['histogram'] = None
  data[i]['byteentropy'] = None
  data[i]['strings'] = None
#print(data[100])
#with open('train_features_0.jsonl','rb') as f:
 #   data = pd.read_json('train_features_0.jsonl', lines ='True')
 #  X = data.iloc[:,:-1].values
#print(len(data))
#with open("train_features_0.jsonl") as f:
#    for line in f:
#        data.append(json.dumps(line))
#print(data)
#jsonlines.Reader('train_features_0.jsonl',loads=None)
#contents = open(filename, "r").read() 
#data = [json.loads(str(item)) for item in contents.strip().split('\n')]
#print(data[1])
#print(data[2])
#temp = data['histogram']
#csv_data = open('csvdata.csv','w')
#csvwriter = csv.writer(csv_data)
#count = 0
#for i in range(len(temp)):
 #   if count == 0:
  #      header = i.keys()
   #     csvwriter.writerow(header)
    #    count+=1
    #csv.writerow(i.values())
#csv_data.close()
#the dataset
#test 2 
#def jsonextract(file):
 #   for i in range(100):
  ###            yield line
     #   i+=1
#jsonextract(filename)#

dataset = np.array(data)

