import csv
import random
import math
import operator


'''
In this Function there a similarity to K-Nearest Neighbour is created in Python only.
This function is to classify a signal of a potential Trend. This trend excists of similar values.
The objects seen in this example are different Integer. These integers stand for different Interests scores:

These scores contain the following values--

Fashion Interests
Technichal Interests
Cultural Interests
Economical Interests
Political Interests

The Signal will be classified on this different values to a certain color.
This color stands for a profile how a user interacts with a Trend.

RED: Vitality Users
Blue: Controlling Users
YELLOW: Harmony Users
GREEN: Secure Users.

A Dutch explanation of this BSR (Brand Strategy Research) Model can be found on:
https://www.samr.nl
'''


#Main function to load in our CSV set with values
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	       if random.random() < split:
	           trainingSet.append(dataset[x])
	       else:
	            testSet.append(dataset[x])

#make an empty array for the trainingset.
trainingSet = []
#make an empty array for the test set.
testSet = []
#split the CSV file in 66% to train, use the other 33 %for test set.
loadDataset('values-with-color.csv', 0.66, trainingSet, testSet)

#print the values of the training and test set
print ('Train ' + repr(len(trainingSet)))
print ('Train ' + repr(len(testSet)))

#function to calculate the distance between the similar neighbours.
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance +=pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance);


#test values of a signal
data1 = [44, 2, 3, 4, 1, 2, "a"]
data2 = [44, 5, 2, 1, 4, 2, "b"]

#test the distance between the test arrays data1 and data2
distance = euclideanDistance(data1, data2, 3)
print ('Distance ' + repr(distance))

#function to get the nearest neighbours.
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

#create a train set with the early mentioned data 1 and data 2.
trainSet = [[44, 2, 3, 4, 1, 2, "red"], [25, 5, 2, 1, 4, 2, "blue"]]
#classify if a signal with different data is a RED or Blue Signal.
testInstance = [44, 5, 2, 1, 1]
#calculate the simmularities on ONE neighbour.
neighbors = getNeighbors(trainSet, testInstance, 1)
#return the neighbour to the user.
print(neighbors)
