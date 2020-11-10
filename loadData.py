#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:48:41 2020

@author: thiha
"""

from csv import reader
# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename,'r') as f:
        csvfile = reader(f)
        for row in csvfile:
            if not row:
                continue
            dataset.append(row)
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup
    
def main():
    file = input("Enter file name :")
    dataset = load_csv(file)
    print( ' Loaded data file {0} with {1} rows and {2} columns ' .format(file, len(dataset),
    len(dataset[0])))
    print(dataset[0])
    # convert string columns to float
    for i in range(4):
        str_column_to_float(dataset, i)
    # convert class column to int
    lookup = str_column_to_int(dataset, 4)
    print(dataset[:4])
    print(lookup)
        
if __name__ == "__main__":
    main()
    