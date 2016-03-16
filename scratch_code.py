from sklearn.feature_selection import RFE
from sklearn.svm import SVR

import dataframe

x, y = dataframe.df_data[:30], dataframe.df_target[:30]

estimator = SVR(kernel='linear')
selector = RFE(estimator, 10, step=10)

print 'Fitting selector'

selector = selector.fit(x, y)

print selector.support_
print selector._get_param_names()