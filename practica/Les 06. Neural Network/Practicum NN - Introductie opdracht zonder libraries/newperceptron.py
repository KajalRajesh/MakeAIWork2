import random
import logging
import numpy as np


class Perceptron1:

    """
    Perceptron class to simulate a Neuron
    """

    # Constructor
    # 'dunder init'
    def __init__(self):
        self.weightVector = None
        self.bias = 0
        
    
    
    def initialize(self):
        """Initialize w and b as zero"""

        # Create initial weight vector for each feature
        
        # return self.weightMatrix
        # Initialize bias
        self.bias = 0
        
    
    def flatten(self,matrix):
        transposedMatrix =list(map(list, zip(*matrix)))
        flatMatrix = [[item for sub_list in transposedMatrix for item in sub_list]]
        return flatMatrix
    
    
    def predict(self, inputVector):
        """
        Determin outputvalue by multiplying
        inputvector with weightvector
        """
        
        self.weightMatrix = [[round(random.uniform(0, 1), 2) for _ in range(1)] for _ in range(9)]
        outputMatrix = [[round(sum(a*b for a,b in zip(A_row, B_col)), 2) for B_col in zip(*self.weightMatrix)] 
             for A_row in inputVector] 
        logging.debug(f"activation : {outputMatrix}")

        return 1 if outputMatrix > 0 else 0

    def train(self, flatMatrix, outputMatrix, epochs=100, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels
        """
        # Initialize weights and bias
        
        # rows = 9
        # self.initialize(rows)
        self.weightMatrix = [[round(random.uniform(0, 1), 2) for _ in range(1)] for _ in range(9)]
        
        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            logging.info(f"epoch : {epoch}")

            # For each inputVector
            for inputVector, label in zip(flatMatrix, outputMatrix):
                logging.debug(f"inputVector : {inputVector}")

                # Labeled output
                logging.debug(f"label : {label}")

                # Predict output
                prediction = self.predict(inputVector)
                logging.debug(f"prediction : {prediction}")

                # Determine error
                error = label - outputMatrix
                logging.debug(f"error : {error}")

                # update weight and b
                deltaWeight = learningRate*error*inputVector
                self.weightMatrix = self.weightMatrix + deltaWeight
                
                logging.debug(f"deltaWeight : {deltaWeight}")
                
                logging.debug(f"learningRate : {learningRate}")
                
                deltaBias = learningRate*error
                self.bias = self.bias + deltaBias
                
                logging.debug(f"deltaBias : {deltaBias}")

                print()

    def predict(self, inputVector):
        """
        Determin outputvalue by multiplying
        inputvector with weightvector
        """
        outputMatrix = [[round(sum(a*b for a,b in zip(A_row, B_col)), 2) for B_col in zip(*self.weightMatrix)] 
             for A_row in inputVector] 
        logging.debug(f"activation : {outputMatrix}")

        return 1 if outputMatrix > 0 else 0
    