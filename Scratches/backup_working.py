# main_code.py
# This is the entry point of the program.
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import dataframe
import VarianceThresholdTest

x, y = dataframe.get_dataset_from_file('nsl.train')
test_x, test_y = dataframe.get_dataset_from_file('nsl.test')

v_threshold = 0.15

new_x = VarianceThresholdTest.get_transformed_matrix_with_threshold(x, y, v_threshold)

print 'After VarianceThreshold data contains %d features' % (len(new_x[0]))

split_ratio = 0.1

while split_ratio < 1.0:
    X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=split_ratio, random_state=0)

    print 'Calling StandardScalar with split_ratio = %f' % split_ratio

    sc = StandardScaler()
    sc.fit(X_train)

    print 'Done with StandardScalar fit'

    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    print 'Calling SVC'
    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm.fit(X_train_std, y_train)

    print 'Done with svm fit'

    print 'Beginning Predict...'
    y_pred = svm.predict(X_test_std)
    print 'Done with predict.'

    print ('Misclassified samples: %d' % (y_test != y_pred).sum())

    print ('Accuracy: %.2f' % (accuracy_score(y_test, y_pred) * 100))
    print '-' * 80

    split_ratio += 0.1
