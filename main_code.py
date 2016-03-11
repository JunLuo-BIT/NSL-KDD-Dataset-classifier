# main_code.py
# This is the entry point of the project

import dataframe

from sklearn.feature_selection import RFE
from sklearn.svm import SVR

# The data
x = dataframe.df_data
y = dataframe.df_target

estimator = SVR(kernel="linear")
selector = RFE(estimator,5,step=1)

print 'Fitting selector'
selector = selector.fit(x,y)

print "support", selector.support_
print "ranking", selector.ranking_