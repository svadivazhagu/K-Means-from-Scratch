#Problem 3
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering, AffinityPropagation

#KMeans
#Agglomerative
def agglomerative():
    from sklearn.datasets import load_digits
    digits = load_digits()
    data, target = load_digits(return_X_y=True)

    clustering = AgglomerativeClustering(n_clusters=10, linkage="ward").fit(data)

    results = [[0 for _ in range(10)] for __ in range(10)]

    for i, val in enumerate(clustering.labels_):
        results[val-1][target[i]] += 1

    print('Agglomerative Clustering Confusion Matrix \n Cluster X axis, Label Y axis', end='\n    ')
    [print("{:3d}".format(i), end=' ') for i in range(10)]
    print('', end='\n    ')
    [print("----", end='') for i in range(10)]

    print('')
    for x in range(10):
        print(x, end=' | ')
        for y in range(10):
            print("{:3d}".format(results[x][y]), end=' ')
        print('')
    # Calculating the  Fowlkes-Mallows scores for Agglomerative
    print('For Agglomerative, Fowlkes-Mallows Score is: '+str(metrics.fowlkes_mallows_score(target[:500],
    clustering.labels_[:500]))+'\n'+'\n')


#Affinity Propagation
def affinityProp():
    from sklearn.datasets import load_digits
    digits = load_digits()
    data, target = load_digits(return_X_y=True)
    aff = AffinityPropagation(preference=-50000)
    clustering = aff.fit(data)

    count = {}

    for label in clustering.labels_:
        if label not in count:
            count[label] = 1
        else:
            count[label] += 1

    results = [[0 for _ in range(10)] for __ in range(10)]

    for i, val in enumerate(clustering.labels_):
        results[target[i]][val] += 1

    conversion = {}
    for t_i, targ in enumerate(results):
        max_cluster = None
        for c_i, cluster in enumerate(targ):
            if max_cluster is None or cluster > targ[max_cluster]:
                max_cluster = c_i

            conversion[t_i] = max_cluster

    labels = [conversion[l] for l in clustering.labels_]

    print("Affinity Propagation Confusion Matrix \n Cluster X axis, Label Y axis")
    [print("{:3d}".format(i), end=' ') for i in range(10)]
    print('', end='\n    ')
    [print("----", end='') for i in range(10)]

    print('')
    for x in range(10):
        print(x, end=' | ')
        for y in range(10):
            print("{:3d}".format(results[x][y]), end=' ')
        print('')
    print("For Affinity Propagation Fowlkes-Mallows Score is: ", metrics.fowlkes_mallows_score(target[:500], labels[:500]))

agglomerative()
affinityProp()