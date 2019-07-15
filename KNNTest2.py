from sklearn import datasets
from collections import Counter
from sklearn.model_selection import train_test_split
import numpy

iris = datasets.load_iris()
x = iris.data
y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(x, y, random_state=2003)


def euc_dis(instance1, instance2):
    return numpy.sqrt(sum((instance1 - instance2) ** 2))


def knn_classify(X, y, testInstance, k):
    distances = [euc_dis(x, testInstance) for x in X]
    kneighbors = numpy.argsort(distances)[:k]
    count = Counter(y[kneighbors])
    return count.most_common()[0][0]


predictions = [knn_classify(X_train, Y_train, data, 3) for data in X_test]
correct = numpy.count_nonzero((predictions == Y_test) == True)
print(correct / len(X_test))
