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
final_array = list()

target = []  # contains the labels.

for line in dataset_lines:
    line = line.replace('\n', '')

    temp = line.split(',')

    # Get the n-1 data, (i.e features)
    items = temp[:len(temp) - 1]

    temp_arr = []

    for item in items:
        if item == 'exec':
            item = 'exec_val'
        try:
            temp_arr.append(float(item))
        except ValueError:
            temp_arr.append(pair_values[item])

    # we can select the required fields(columns) here.
    # if not simply pass temp_arr.
    # final_array.append(temp_arr[:6] + temp_arr[20:])
    final_array.append(temp_arr)

    # append the label to target list.
    target.append(pair_values[temp[-1]])

# This is done to select the first 80000 records of the dataset.
# Frankly speaking this is not necessary.
final_array = final_array[:8000]
target = target[:8000]

# convert the regular list into numpy array.
df_data = np.asarray(final_array)
df_target = np.asarray(target)
