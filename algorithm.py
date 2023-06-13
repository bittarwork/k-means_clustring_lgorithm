
import matplotlib.pyplot as plt

# 1
def Average(lst): 
    n = len ( lst) 
    sum = 0
    count = 0 
    for i in range ( 0,n ): 
        sum = sum + lst[i]
        count = count +1 
    avr = sum / count 
    return avr  
# 2
def Distance(point1X, point2X, point1Y, point2Y):
    return ((point2X - point1X)**2 + (point2Y - point1Y ) **2)**0.5
# 3
def readPoints():
    f = open("data.csv", "r")
    handel = f.readlines()
    listofx = []
    listofy = []
    pointCount = 0 
    for i in handel :  
        if "X" in i : 
            continue
        else : 
            line = i.strip()
            numbers = line.split(',')
            listofx.append(float(numbers[0]))
            listofy.append(float (numbers[1]))
            pointCount=pointCount+1
    return listofx , listofy , pointCount 
# # 4
def initCentroids(listofx, listofy, K):
    centroids = []
    for i in range (K) :
        l = [] 
        l.append(listofx[i])
        l.append(listofy[i])
        centroids.append(l)
    return centroids
# 5
def initClusters(K):
    lis = [[[ [] for _ in range(0)] for _ in range(2)] for _ in range(K)]
    return lis
# 6 
def rebuildClusters(pointCount, Centroids, listofx, listofy, K):
    clusters = initClusters(K) 
    for i in range (0, pointCount) : 
        dic = []
        for j in range (0, K) : 
            dictanc = Distance(Centroids[j][0], listofx[i], Centroids[j][1], listofy[i])
            dic.append(dictanc)
        min = dic[0]
        for x  in range (1, len (dic)) : 
            if (dic[x] < min ) :
                min = dic[x]
        index = dic.index(min)
        clusters[index][0].append(listofx[i])
        clusters[index][1].append(listofy[i])
    return clusters

def reCalclculateCentroids(clusters, K):
    NewCentroids = initClusters(K)
    for i in range ( K) : 
        if (len (clusters[i][0]) > 0):
            NewCentroids[i][0]= (Average(clusters[i][0]))
            NewCentroids[i][1]= (Average(clusters[i][1]))
    return NewCentroids

def calculateLossValue(NewCentroids, Centroids,K):
    sum = 0
    for i in range (K) : 
        x = Centroids[i][0]
        y = Centroids[i][1]
        x2 = NewCentroids[i][0]
        y2 = NewCentroids[i][1]
        sum =sum + Distance(x2, x, y2, y)
    return sum
        

def K_Means_iteration(pointCount,listofx, listofy, Centroids, K ):
    clusters = rebuildClusters(pointCount, Centroids, listofx, listofy, K)
    newCentroids =  reCalclculateCentroids(clusters, K)
    loos = calculateLossValue(newCentroids, Centroids,K)
    return clusters , loos , newCentroids

def showClusters(clusters, K):
        for i in range ( 0 , K) : 
            listofx = clusters[i][0]
            listofy = clusters[i][1]
            plt.scatter(listofx, listofy)
        plt.show()
       


# Please do not change after this point

listofx, listofy, pointCount = readPoints()
Xlabel = "X"
Ylabel = "Y"

plt.scatter(listofx, listofy)
plt.xlabel(Xlabel)
plt.ylabel(Ylabel)
plt.show()


totalIterations = 50
iterations = totalIterations
K = 6
Minimumloss = 0.0001

Centroids = initCentroids(listofx, listofy,K)
while iterations >= 0:
    clusters, loss, Centroids = K_Means_iteration(pointCount,listofx, listofy, Centroids, K )
    print("Epoch = %d"%(totalIterations - iterations+1 ))
    print("Loss Function = %0.4f"%(loss))
    if(loss <Minimumloss):
        break
    iterations -= 1


print ( clusters)
Colors = ["red", "blue", "green", "black", "yellow", "purple","magenta"]
showClusters(clusters, K)