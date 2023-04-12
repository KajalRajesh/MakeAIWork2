from newperceptron import Perceptron1
import itertools
import logging
import numpy as np


xTrain =  [[1,1,1],
    [1,0,1],
    [1,1,1]]


logging.debug(f"xTrain : {xTrain}")

# Waarheidstabel output
yTrain = [[ 1]]

# Maak een object perceptron aan
andPerceptron = Perceptron1()
# Train de perceptron met een AND functie
# andPerceptron.train(xTrain, yTrain, epochs=10, learningRate=0.1)

testInput = [[1,0,1],
    [1,0,1],
    [1,1,1]]
prediction = andPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")

