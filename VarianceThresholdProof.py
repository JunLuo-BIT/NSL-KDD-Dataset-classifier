# This python script provides a proof that variance threshold removes
# feature at an early stage.

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import dataframe
import VarianceThresholdTest

x = dataframe.df_data
y = dataframe.df_target

v_threshold = 0.0
while v_threshold <= 1.0:
    new_x = VarianceThresholdTest.get_transformed_matrix_with_threshold(x, y, v_threshold)
    features = len(new_x[0])

    print 'Threshold %f, Features %d' % (v_threshold, features)

    v_threshold += 0.01
