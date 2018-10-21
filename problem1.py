#A3 by svadivazhagu for CS-534 Fall'2018

#Problem 1, Implementing K-Means on cluster_data.txt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.cluster import AgglomerativeClustering
#%matplotlib inline NEED FOR JUPYTER


xCoords = []
yCoords = []
zippedList = []

#Prep the dataset to be accessed. Removes the line # and splits x and y coordinates
#into their own arrays. Dataset -> 2d[] -> 2 1d[]'s
def prepData():
    with open("cluster_data.txt") as textFile:
        lines = [line.split() for line in textFile]

    for i in range(len(lines)):
        lines[i].pop(0)
    for i in range (len(lines)):
        xCoords.append(float(lines[i][0]))
        yCoords.append(float(lines[i][1]))

prepData()

zippedPoints  = list(zip(xCoords, yCoords))
#plt.scatter(xCoords, yCoords)
#plt.show()


df = pd.DataFrame({
    'x': xCoords,
    'y': yCoords
})

np.random.seed(200)
k = 6
# centroids[i] = [x, y]
centroids = {
    i + 1: [random.randint(1, 2), random.uniform(-0.005, 0.005 )]
    for i in range(k)
}

colmap = {1: 'red', 2: 'green', 3: 'blue', 4:'yellow', 5:'purple', 6:'black'}

#Assigning points to dataset based on Euclidean Distance

def assignment(df, centroids):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)


#Update the centroids based on cluster's points.
import copy

old_centroids = copy.deepcopy(centroids)


def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k


centroids = update(centroids)


#Assignment again.
df = assignment(df, centroids)


# Stop only when the change from cluster to cluster is negligible.
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure(figsize=(8, 8))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=1, edgecolor='k', label = "Data Point")
for i in centroids.keys():
    plt.scatter(*centroids[i], color='black', alpha = 1, s = 100, edgecolor = 'white', marker="X", label = "Centroid "+str(i))
fig.suptitle('After K=' + str(k) + ' Clustering', fontsize=14)
plt.xlabel('Length', fontsize=12)
plt.ylabel('Width', fontsize=12)
plt.legend(loc='lower left')
plt.show()

print("Note that sometimes, the random initial clustering can lead to having a"
      " blank centroid in the legend. Just run the program again and it should update within 1 or 2 instances."
      " Each centroid is marked by an X. It may"
      "be difficult to see all the centroids.")



