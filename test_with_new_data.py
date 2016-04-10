# test_with_new_data.py
# This python script will first train the svm with training data set
# then test it against the training data set provided
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import VarianceThresholdTest
import dataframe

train_x, train_y = dataframe.get_dataset_from_file('proper.train.data')
test_x, test_y = dataframe.get_dataset_from_file('corrected')

v_threshold = 0.15
debug = True

selector = VarianceThreshold(v_threshold)
new_test_x = selector.fit(train_x)

new_test_y = selector.transform(test_x)

if debug:
    print 'After fit'
    print 'Train contains %d features' % len(new_test_x[0])
    print 'Test contains %d features' % len(new_test_y[0])
