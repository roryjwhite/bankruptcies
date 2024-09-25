# clustering model to group EU countries by correlation patterns, to provide insights into shared economic characteristics

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler # import scaler
scaler = RobustScaler() # initiate

df_read = pd.read_csv("/content/python EU debt correlations - Sheet1.csv")
df_read
# link to csv - https://docs.google.com/spreadsheets/d/1eQu0-k23V5k40-tj3W0ZL80YbHMmNH6Y10r363Tocmk/edit?gid=0#gid=0

df_read.set_index("joiner").corr()

df_read.set_index(["joiner"], inplace=True)  # set joiner column as index since not numerical

df_no_interest = df_read.pop('avg_interest_rate')   # take out interest rate since similar for all countries

df_read_scaled = pd.DataFrame(scaler.fit_transform(df_read), columns=df_read.columns, index=df_read.index)  # scale data

df_read_scaled = df_read_scaled.dropna()  # drop nulls

# Working out inertias for different number of clusters
nb_clusters_to_try = range(1, 20)
inertias3 = []

for k in nb_clusters_to_try:
    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(df_read_scaled)
    inertias3.append(kmeans.inertia_)

inertias3


import plotly.express as px

fig3 = px.line(y=inertias3,
              x=range(1, len(inertias3) + 1),
              labels={'x': 'nb centroids', 'y':'Inertia'},
              title="Elbow method")
fig3.show()


# Choosing the number of clusters and fitting the model
new_new_clusters = 5
kmeans = KMeans(n_clusters=new_new_clusters, n_init='auto', max_iter=300)
kmeans.fit(df_read_scaled)

# Extract the labels
labelling3 = kmeans.labels_

df_read = df_read.dropna()   # dropping nulls so that indexes match


df_read['labels'] = labelling3   # Add the labels to the original dataframe

fig2_clustered = px.scatter_3d(df_read_scaled,
                           x='avg_bankruptcy_index',
                           y='avg_registration_index',    # graph to visualize
                           z='debt_value_from_profits',
                           color=labelling3,
                           width=500,
                           height=500)
fig2_clustered.show()
