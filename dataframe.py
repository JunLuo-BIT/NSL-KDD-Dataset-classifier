# dataframe.py
# This is the dataframe code.
# This is a pillar code, i.e these are the helper codes.

# This script will create data and target as a numpy array
# and it can be used by others.

# ------------------------------------------------------------------------------
# This python script will read the provided dataset
# and it will generate a list 'df_data' and 'df_target' which are numpy arrays.

import os
import numpy as np
import values


def get_all_lines_from_dataset(dataset_file):
    """Opens the dataset_file in READ MODE; returns the lines of the file."""
    with open(dataset_file) as f:
        lines = f.readlines()

    return lines


def convert_feature_to_float(features):
    """Converts the string attributes(Actual features) to appropriate float values"""

    temp_arr = []
    pair_values = values.get_list()

    for attrib in features:
        # Try to convert the attrib to float,
        # If that is not possible then look up the pair_values[]
        try:
            temp_arr.append(float(attrib))
        except ValueError:
            temp_arr.append(pair_values[attrib])

    return temp_arr


def get_dataset_from_file(input_dataset):
    """"""
    # input_dataset = 'corrected'
    # file_name = "/home/%s/dataset/%s" % (getpass.getuser(), input_dataset)

    file_name = '%s\\Documents\\dataset\\%s' % (os.path.expanduser('~'), input_dataset)

    debug = True

    # with open(file_name) as dataset_file:
    #     dataset_lines = dataset_file.readlines()

    dataset_lines = get_all_lines_from_dataset(file_name)

    if debug:
        print 'Using %s as dataset.' % file_name
        print 'Dataset has %d instances, each instance with %d attributes' % (
            len(dataset_lines), len(dataset_lines[0].split(',')))

    # Get the key value pair.
    pair_values = values.get_list()

    features = []
    label = []  # contains the target label.

    for line in dataset_lines:
        items = line.replace('\n', '').split(',')

        if False:
            print 'items length %d' % (len(items))
            print items

        # Get the n-1 data, (i.e features)
        features = items[:len(items) - 1]

        temp_arr = convert_feature_to_float(features)

        features.append(temp_arr)

        # append the label to target list.
        label.append(pair_values[items[-1]])

    # convert the regular list into numpy array.
    df_data = np.asarray(features)
    df_target = np.asarray(label)

    return df_data, df_target


def get_test_data_from_file(input_dataset):
    # file_name = "/home/%s/dataset/%s" % (getpass.getuser(), input_dataset)
    file_name = '%s\\Documents\\dataset\\%s' % (os.path.expanduser('~'), input_dataset)

    debug = True

    # with open(file_name) as dataset_file:
    #     dataset_lines = dataset_file.readlines()

    dataset_lines = get_all_lines_from_dataset(file_name)

    if debug:
        print 'Using %s as dataset.' % file_name
        print 'Dataset has %d instances, each instance with %d attributes' % (
            len(dataset_lines), len(dataset_lines[0].split(',')))

    # Get the key value pair which has been already done.
    pair_values = values.get_list()

    # contains the training data.
    data = []

    for line in dataset_lines:
        items = line.replace('\n', '').split(',')

        if False:
            print 'items length %d' % (len(items))
            print items

        # Get the n-1 data, (i.e features)
        features = items[:len(items) - 1]

        temp_arr = []

        for attrib in features:
            try:
                temp_arr.append(float(attrib))
            except ValueError:
                temp_arr.append(pair_values[attrib])

        data.append(temp_arr)

    # convert the regular list into numpy array.
    df_data = np.asarray(data)

    return df_data


def get_dataset_from_path(file_path):
    debug = True

    with open(file_path) as dataset_file:
        dataset_lines = dataset_file.readlines()

    if debug:
        print 'Using %s as dataset.' % file_path
        print 'Dataset has %d instances, each instance with %d attributes' % (
            len(dataset_lines), len(dataset_lines[0].split(',')))

    # Get the key value pair which has been already done.
    pair_values = values.get_list()

    # contains the training data.
    data = []

    target = []  # contains the target label.

    for line in dataset_lines:
        items = line.replace('\n', '').split(',')

        if False:
            print 'items length %d' % (len(items))
            print items

        # Get the n-1 data, (i.e features)
        features = items[:len(items) - 1]

        temp_arr = []

        for attrib in features:
            try:
                temp_arr.append(float(attrib))
            except ValueError:
                temp_arr.append(pair_values[attrib])

        data.append(temp_arr)

        # append the label to target list.
        target.append(pair_values[items[-1]])

    # convert the regular list into numpy array.
    df_data = np.asarray(data)
    df_target = np.asarray(target)

    return df_data, df_target
