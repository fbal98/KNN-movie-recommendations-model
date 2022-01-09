import sys

import sklearn
from sklearn.neighbors import KNeighborsClassifier
import sklearn.neighbors
import pandas as pd
import numpy as np
import pickle
from fuzzywuzzy import fuzz

class Recommendation:


    def __init__(self):
        # importing data and model
        self.encodedData = pickle.load(open('assets/encodedData', 'rb'))
        self.data = pickle.load(open('assets/data', 'rb'))
        self.model = pickle.load(open('assets/model', 'rb'))

    def findMatching(self, query):
        matchingList = []

        i = 0

        for row in self.data.itertuples():
            title = row[2]
            tag = row[6]
            index = row.Index

            if fuzz.partial_ratio(title, query) > 40:
                matchingList.append(self.encodedData[index])

            if fuzz.partial_ratio(tag, query) > 40:
                matchingList.append(self.encodedData[index])

            i += 1

            if i > 30000:
                break

        return matchingList

    def make_recommendation(self,favoriteMovies):
        PredictionList = []

        for i in range(len(favoriteMovies)):
            PredictionList.extend(self.findMatching(favoriteMovies[i]))

        _, predicted = self.model.kneighbors(PredictionList, n_neighbors=30)

        return self.data.iloc[predicted[0]]








##how to use it
#
#predictedMoviesList = r.make_recommendation(["shawshank redemption", 'the matrix', 'inception', 'dark Knight'])

#print(predictedMoviesList.values.tolist()[0][1])



