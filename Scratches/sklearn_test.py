from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.svm import SVC

from sklearn import datasets

# iris = datasets.load_iris()
# x, y = iris.data, iris.target
#
# print 'X.size = '
#
# estimator = SVR(kernel='linear')
# selector = RFE(estimator, 2, step=3)
#
# print 'Fitting selector'
#
# selector = selector.fit(x, y)
#
# print selector.support_
# print selector._get_param_names()
#
# print selector.predict([4.6, 3.1, 1.5, 0.2])
#
# clf = SVC()
# clf.fit(x, y)
#
# print clf.predict([4.6, 3.1, 1.5, 0.2])

from sklearn.feature_selection import VarianceThreshold

v = VarianceThreshold(0.6)

a = []

a = [[1, 2, 3], [1, 3, 4], [1, 3, 5], [1, 6, 5]]

r = v.fit_transform(a)

print r
