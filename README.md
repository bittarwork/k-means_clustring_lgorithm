# k-means_clustring_lgorithm
A side project 
It is an algorithm that clusters a set of points that can be considered close into a known number of clusters called K. 

The algorithm works iteratively (epochs or iterations) by rebuilding the clusters and recalculating their centers during each epoch. 

The algorithm stops when a maximum number of epochs, totalIterations, is reached, or when a stopping condition is met (no new changes in the clusters occur). 

The algorithm is initialized by selecting a number of points as the initial centroids for the clusters. 

The number of initial centroids is equal to the number of clusters, for example, if K = 6, then there will be 6 initial centroids.

During each epoch, the K-Means algorithm performs the following steps:

- Initialize the clusters with no points.

- For each point:

1. Calculate the distance between the point and each of the cluster centroids.

2. Add the point to the cluster with the nearest centroid.

- Recalculate the new centroids for each cluster using the mean values.

- Calculate the loss value, which is the sum of the distances between the new centroids and their corresponding old centroids.

- Stopping condition: the algorithm stops if the loss function value is less than 0.0001 (meaning no new changes in the cluster centroids).

The file containing the points is in the following format:

It is an xls file where each row contains the coordinates of a point (x,y). 

An example of the coordinates of a point is: 3.310639, 0.281214. 

The ultimate goal of this project is to obtain the final clusters of the points in the file.

A value of k=6 has been given,

and the algorithm will be run accordingly. 

Python has been used in this project, with plt.scatter being used as the method to display the points.

and view the results in the attached images.

" #python #project "
