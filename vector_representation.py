import pandas as pd

def get_vectors():
    df = pd.read_csv('data_small.csv')

    thresh = 0.8
    movies = []

    for i in range(len(df)):
        row = df.iloc[i]
        # id = i + 1
        # title = row['movieId'] # the title of the movie is under 'movieId' in the csv

        vector = row.to_numpy()[22:] # exclude title and genres
        vector[vector < thresh] = 0

        # movies.append((id, title, vector))
        movies.append(vector)

    return movies