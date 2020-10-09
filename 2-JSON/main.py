#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import configparser

#config variables definition
config = configparser.ConfigParser()
config.read('config.ini')
input_file = config['FILES']['source']
output_file = config['FILES']['destination']

#reading an input json file
with open(input_file, encoding='utf-8') as openfile:
    data = json.load(openfile)

dataArray = data['exchangeRate']

res = list()
test = {}

#write required key & fields in an output json file
for obj in dataArray:
    if 'saleRate' in obj:
        test[obj.get('currency')] = obj['saleRate'] - obj['saleRateNB']
res.append(test)
with open(output_file, 'w') as jsonFile:
    json.dump(res, jsonFile, indent=4)
