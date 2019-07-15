from sklearn import datasets
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy

iris = datasets.load_iris()
x = iris.data
y = iris.target
# print(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2003)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train, y_train)

# correct = numpy.count_nonzero((clf.predict(x_test) == y_test) == True)

print(accuracy_score(y_test, clf.predict(x_test)))

# print(correct/len(x_test))

# def euc_dis(instance1, instance2):
#     return numpy.sqrt(sum((instance1 - instance2) ** 2))
