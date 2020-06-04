import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns

songs = pd.read_csv('G:/Projects/smart_shuffle/mlcode/dataset/Songs_data.csv')

song_features = (songs[['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']])

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()
song_features = min_max_scaler.fit_transform(song_features)

np.round(song_features,2)

from sklearn.neighbors import NearestNeighbors

nbrs = NearestNeighbors(n_neighbors=20, algorithm='kd_tree').fit(song_features)

distances, indices = nbrs.kneighbors(song_features)

def get_index_from_name(name):
    return songs[songs["track"]==name].index.tolist()[0]

def print_similar_songs(query=None,id=None):
    ss =[]
    if id:
        for id in indices[id][1:]:
            ss.append(songs.loc[id]["track"])
    if query:
        found_id = get_index_from_name(query)
        for id in indices[found_id][1:]:
            ss.append(songs.loc[id]["track"])
    return ss