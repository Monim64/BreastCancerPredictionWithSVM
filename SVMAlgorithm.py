"""    Created by Monim on 9/14/2018.    """
# Importing the libraries
import numpy as numpy
import pandas as pandas
from sklearn.svm import SVC

classifier = SVC()


class SVMAlgorithm:
    # Importing the dataset
    dataset = pandas.read_csv('breast_cancer_data.csv')
    dataset.replace('?', 0, inplace=True)
    dataset.drop(['Id'], 1, inplace=True)

    X = numpy.array(dataset.drop(['Class'], 1))
    y = numpy.array(dataset['Class'])

    classifier.fit(X, y)

    def get_result(self, input_array):
        result = classifier.predict(input_array)
        return result[0]
