#!/usr/bin/env python

from perceptron import Perceptron
import itertools
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)


# Waarheidstabel invoerwaarden
possibleOutcomes = [0, 1]
xTrain = np.array(
    [element for element in itertools.product(possibleOutcomes, possibleOutcomes)]
)

logging.debug(f"xTrain : {xTrain}")

# Waarheidstabel output
yTrain = np.array([0, 1, 1, 1])


# Maak een object perceptron or

orPerceptron = Perceptron()

# Train de perceptron met een OR functie
orPerceptron.train(xTrain, yTrain, epochs=100, learningRate=0.1)

# Test de perceptron
testInput = np.array([0, 0])
prediction = orPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")

# Test de perceptron

testInput = np.array([0, 1])
prediction = orPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")

# Test de perceptron
testInput = np.array([1, 0])
prediction = orPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")

# Test de perceptron
testInput = np.array([1, 1])
prediction = orPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")
