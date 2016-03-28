from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.svm import SVC

from sklearn import datasets

iris = datasets.load_iris()
x, y = iris.data, iris.target

print 'X.size = '

estimator = SVR(kernel='linear')
selector = RFE(estimator, 3, step=1)

print 'Fitting selector'

selector = selector.fit(x, y)

print selector.support_
print selector._get_param_names()

print selector.predict([4.6, 3.1, 1.5, 0.2])

clf = SVC()
clf.fit(x, y)

print clf.predict([4.6, 3.1, 1.5, 0.2])
