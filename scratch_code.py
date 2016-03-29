from sklearn.feature_selection import RFE
from sklearn.svm import SVR

import dataframe
import datetime

import os

debug = True

x, y = dataframe.df_data, dataframe.df_target

print 'Dataset contains %d instances with %d initial features.' % (len(y), len(x[0]))

log_file = open('%s/result.txt' % os.getenv('HOME'), 'a')

estimator = SVR(kernel='linear')

for i in range(40, 12, -1):
    selector = RFE(estimator, i, step=6)

    if debug:
        temp = 'Iteration %d started at %s\n' % (i, str(datetime.datetime.now()))
        print temp
        log_file.write(temp)

    print 'Fitting selector'

    selector = selector.fit(x, y)

    if debug:
        temp = str(selector.support_) + '\n'
        log_file.write(temp)
        print temp

        temp = str(selector.get_support(indices=True)) + '\n'
        log_file.write(temp)
        print temp

log_file.close()
