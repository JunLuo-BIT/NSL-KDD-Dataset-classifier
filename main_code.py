# main_code.py
# This is the entry point of the program.
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import dataframe
import VarianceThresholdTest

x = dataframe.df_data
y = dataframe.df_target

v_threshold = 0.15

new_x = VarianceThresholdTest.get_transformed_matrix_with_threshold(x, y, v_threshold)

print 'After VarianceThreshold data contains %d features' % (len(new_x[0]))

X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=0.3, random_state=0)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

svm = SVC(kernel='linear', C=1.0, random_state=0)
svm.fit(X_train_std, y_train)

y_pred = svm.predict(X_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())

print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
