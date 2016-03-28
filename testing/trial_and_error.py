# trial_and_error.py
import dataframe

from sklearn import svm
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = svm.SVC()

x = dataframe.df_data[:4000]
y = dataframe.df_target[:4000]

print 'Fitting the data'
clf.fit(x, y)
print 'Done with Fitting'

# testing_val = [0,203,304,411,829,327,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,8,113,0.88,0.25,0.12,0.02,0.00,0.00,0.00,0.00]
testing_val = [0, 203, 304, 411, 829, 327, 0, 0, 1, 1, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 8, 113, 0.88, 0.25,
               0.12, 0.02, 0.00, 0.00, 0.00, 0.00]
testing_val = [0, 201, 306, 411, 105, 146, 0, 1, 1, 0.00, 0, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 255, 253, 0.99, 0.01,
               0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
print 'Testing'
print clf.predict([testing_val])
