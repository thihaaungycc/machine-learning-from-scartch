#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:44:08 2020

@author: thiha
"""
from math import sqrt

def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

def normalize_dataset(dataset, minmax):
    for row in dataset:
        for col in range(len(row)):
            row[col] = (row[col] - minmax[col][0])/(minmax[col][1]-minmax[col][0])

def col_means(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for col in range(len(dataset[0])):
        col_values = [row[col] for row in dataset]
        means[col] = sum(col_values) / len(col_values)
    return means    

def column_stdevs(dataset, means):
    stdevs = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i]-means[i], 2) for row in dataset]
        stdevs[i] = sum(variance)
    stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
        return stdevs

def standardize_dataset(dataset, means, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]

def main():
    test_list = ([1,11,10],[5,46,5],[3,4,9],[5,6,7])
    '''list_minmax = dataset_minmax(test_list)
    normalize_dataset(test_list, list_minmax)
    print(test_list)'''
    means = col_means(test_list)
    print(means)
    
if __name__ == '__main__':
    main()