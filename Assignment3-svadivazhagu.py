#A3 by svadivazhagu for CS-534 Fall'2018

#Problem 1, Implementing K-Means on cluster_data.txt
import numpy as np
import random as random
from matplotlib import pyplot as plt
import math

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
plt.scatter(xCoords, yCoords)
#plt.show()


#Class Point that is a data point (x,y)
zippedPoints = []



# class Cluster:
#     def __init__(self, id, dataPoints ):
#         self.id = id
#         self.dataPoints = []






#Clusters list that holds each cluster.
eachCluster = [zippedPoints]
allClusters = []
#Clustering function that implements k-means on user-specified integer k clusters
def clusterSet(k):
    #list distances contains the values of each data point being compared to the clusters.
    #to find the shortest distance (clustering) from point to centroid, Euclid. dist. and store value in array
    #iteratively. Then, take min(distances[]) and then fetch the indice via .index(shortestDistance), then
    #add


    distances = []
    if (isinstance(k, int)):
        #make point list that is k lists long where each list is 2 elements (x,y)
        #initialize k number of clusters, each cluster = (x,y) where f(-10)<=x,y<=f(10)
        for i in range(k):
            allClusters.append([[random.uniform(-5, 5), random.uniform(-5, 5)]])
        print(allClusters)


#If wanna modify cluster size change this value here (Default 3):
clusterSet(3)
zippedPoints  = list(zip(xCoords, yCoords))


xyZip = []
def shortestDistance():
    distanceList = []
    shortestCluster = 0
    for i in range(len(allClusters)):
        # allXClusters.append(allClusters[i][0][0])
        # allYClusters.append(allClusters[i][0][1])
        #xyZip.append(list(zip(allXClusters[i][0][0], allYClusters[i][0][1])))
        clusterX = [(allClusters[i][0][0])]
        clusterY = [(allClusters[i][0][1])]
        xyZip.append(list(zip(clusterX, clusterY)))
    print(xyZip[0][0][0])
   # print(xyZip[0])
  #  print(xyZip[0], zippedPoints[0])
    for point in range(len(zippedPoints)):
        for i in range(len(allClusters)):
            distance = math.sqrt(((xyZip[i][0][0] - zippedPoints[point][0]) ** 2)  + ((xyZip[i][0][1] - zippedPoints[point][1]) ** 2))
            distanceList.append(distance)
            shortestCluster = distanceList.index(min(distanceList))
        print(distanceList, point, shortestCluster)
        distanceList.clear()
        xyZip[shortestCluster].append(zippedPoints[point])
    print(xyZip)
    print(len(xyZip[0]))
   # xyZip.insert(shortestCluster, point)



shortestDistance()


