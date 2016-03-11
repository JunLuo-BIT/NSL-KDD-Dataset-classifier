# test_1.py

import dataframe

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.feature_selection import RFE
from sklearn.svm import SVR

from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import GaussianNB

# print dataframe.target

x = dataframe.df_data
y = dataframe.df_target

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)

# standardize data for classifier

print 'Calling the StandardScaler'

# --------------------------------------------------------The originals
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

print 'Calling the SVM classifier'

# call SVM classifier and train it using fit()
# svm = SVC(kernel='linear', C=1.0, random_state=0)
# svm.fit(X_train_std, y_train)

# --------------------------------------------------------The originals

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train_std, y_train)
print 'Done with svm fitting'

print 'Predicting the error rate with K neighbors'
y_pred = neigh.predict(X_test_std)

# predicted labels and accuracy
#y_pred = svm.predict(X_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())

print('Accuracy: %.2f %%' % (accuracy_score(y_test, y_pred) * 100))

print 'Coming to Naive Bayes'
gnb = GaussianNB()

y_pred = gnb.fit(x, y).predict(x)
print("Number of mislabeled points out of a total %d points : %d" % (len(x),(y != y_pred).sum()))
#print('Misclassified samples: %d' % (y_test != y_pred).sum())

# print('Accuracy: %.2f %%' % (accuracy_score(y_test, y_pred) * 100))
print 'Accuracy is %.2f' % (100 - 100 * (y != y_pred).sum() // len(x))