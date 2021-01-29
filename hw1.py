"""
Author: Joey Hejna
Institution: UC Berkeley
Date: Spring 2021
Course: CS189/289A

A Template file for CS 189 Homework 1.

Feel free to use this if you like, but you are not required to!
"""

# Imports. Feel free to add / remove
import numpy as np
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.metrics import accuracy_score # This is the only function you are allowed to use.
from scipy import io
import csv
import os
import argparse

#################################
# Suggested Utility Functions   #
#################################

def load_data(name):
    # Return the specified dataset
    return NotImplemented

#################################
# Question 1: Data Partitioning #
#################################

def partition(data, labels, validation_size):
    return NotImplemented

#################################
# Question 2: SVMs              #
#################################

def train(X, Y, other_args="insert your args here"):
    # create, train, and return and SVM Model
    return NotImplemented

def num_examples_experiment(X_train, Y_train, X_val, Y_val, num_examples_arr):
    # train an svm for each number of examples.
    # Evaluate the training and validation performance
    # plot the results.
    return NotImplemented

def main_q2():
    # Run all of the code for question 3.
    MNIST_NUM_EXAMPLES_ARR = [100, 200, 500, 1000, 2000, 5000, 10000]
    SPAM_NUM_EXAMPLES_ARR = [100, 200, 500, 1000, 2000, "ALL"] # Figure out the number of examples in the dataset or handle this case.
    CIFAR_NUM_EXAMPLES_ARR = [100, 200, 500, 1000, 2000, 5000]

    # YOUR CODE HERE
    return NotImplemented

#################################
# Question 3: Hyperparameters   #
#################################

def hyperparameter_search(X_train, Y_train, X_val, Y_val, parameter_values):
    return NotImplemented

def main_q3():
    return NotImplemented

#################################
# Question 4: KFold CrossValid  #
#################################

def k_fold_cross_validation(X_train, Y_train, k):
    return NotImplemented

def main_q4():
    return NotImplemented

#################################
# Question 5: Kaggle            #
#################################

# For kaggle, do whatever you like!

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", "-q", type=int, default=1, help="Specify which question to run")
    args = parser.parse_args()

    if args.question == 2:
        main_q2()
    elif args.question == 3:
        main_q3()
    elif args.question == 4:
        main_q4()
    elif args.question == 5:
        pass # TODO: Insert your calls for running the kaggle code.
    else:
        raise ValueError("Cannot find specified question number")
