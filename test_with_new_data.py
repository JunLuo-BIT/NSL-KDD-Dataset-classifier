# test_with_new_data.py
# This python script will first train the svm with training data set
# then test it against the training data set provided
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import VarianceThresholdTest
import dataframe

train_x, train_y = dataframe.get_dataset_from_file('corrected')
test_x = dataframe.get_test_data_from_file('kddcup.testdata.unlabeled_10_percent')

v_threshold = 0.15

selector = VarianceThreshold(v_threshold)
x_train = selector.fit_transform(train_x, train_y)

selector = VarianceThreshold(v_threshold)
x_test = selector.fit_transform(test_x)

print len(x_train), len(x_test)