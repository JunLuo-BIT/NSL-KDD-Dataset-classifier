# dataframe.py
# This is the dataframe code.
# This is a pillar code, i.e these are the helper codes.

# This script will create data and target as a numpy array
# and it can be used by others.

# ------------------------------------------------------------------------------
# This python script will read the provided dataset
# and it will generate a list 'df_data' and 'df_target' which are numpy arrays.

import getpass

import numpy as np
import values

file_name = "/home/%s/dataset/corrected" % (getpass.getuser())

with open(file_name) as dataset_file:
    dataset_lines = dataset_file.readlines()

# Get the key value pair which has been already done.
pair_values = values.get_list()

# contains the training data.
final_array = []

target = []  # contains the target label.

for line in dataset_lines:
    items = line.replace('\n', '').split(',')

    # Get the n-1 data, (i.e features)
    features = items[:len(items) - 1]

    temp_arr = []

    for attrib in features:
        try:
            temp_arr.append(float(attrib))
        except ValueError:
            temp_arr.append(pair_values[attrib])

    final_array.append(temp_arr)

    # append the label to target list.
    target.append(pair_values[items[-1]])

# convert the regular list into numpy array.
df_data = np.asarray(final_array)
df_target = np.asarray(target)
