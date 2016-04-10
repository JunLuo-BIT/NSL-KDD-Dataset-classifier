from sklearn.feature_selection import VarianceThreshold
import dataframe

debug = True

# x, y = dataframe.get_dataset_from_file('corrected')
#
# print 'Dataset contains %d instances with %d initial features.' % (len(y), len(x[0]))
#
threshold = 0
threshold_increment = 0.01


def get_transformed_matrix_with_threshold(x, y, threshold):
    sel = VarianceThreshold(threshold)
    return sel.fit_transform(x, y)

if not debug:
    while threshold <= 1.0:
        x, y = dataframe.df_data, dataframe.df_target

        selector = VarianceThreshold(threshold)
        result = selector.fit_transform(x, y)

        print 'Threshold = %f, Features remained after fit_transform %d' % (threshold, len(result[0]))

        threshold += threshold_increment

        print selector.get_support(indices=True)
