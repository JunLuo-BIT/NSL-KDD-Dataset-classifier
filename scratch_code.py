from sklearn.feature_selection import RFE
from sklearn.svm import SVR

import dataframe
import datetime

x, y = dataframe.df_data, dataframe.df_target
cx = x
cy = y

f = open('/home/dtlabz/result.txt', 'a')

estimator = SVR(kernel='linear')

for i in range(10):
    selector = RFE(estimator, i, step=1)

    print 'Fitting selector'

    f.write('Current i: ' + str(i) + ' ')
    f.write('Time ' + str(datetime.datetime.now()))

    print 'Current i: ' + str(i) + ' '
    print 'Time ' + str(datetime.datetime.now())

    selector = selector.fit(x, y)

    print selector.support_

    try:
        f.write(str(selector.support_) + '\n')
        print str(selector.support_) + '\n'
    except:
        print 'Error with f.write selector support'

    print selector._get_param_names()

    try:
        f.write(str(selector._get_param_names()))
        print str(selector._get_param_names())
    except:
        print 'Error with f.write selector param names'

    f.write('Done with iteration ' + str(i) + '\n\n')
    print 'Done with iteration ' + str(i) + '\n\n'

f.close()
