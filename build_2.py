# build_2.py

# main.py
# This is the entry point of the program.

import numpy as np

# from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# import svmc

# dataset = svmc.load_kdd_cup_99_dataset()

# for item in dataset:
#     print item[column_name_index.protocol_type]

# print len(dataset)

# -------------------

import values

# from pprint import pprint

dataset_file = open('corrected')

dataset_lines = dataset_file.readlines()

pair_values = values.get_list()

final_array = list()

target = []

for line in dataset_lines:
    line = line.replace('\n', '')

    temp = line.split(',')
    items = temp[:len(temp) - 1]

    temp_arr = []

    for item in items:
        if item == 'exec':
            item = 'exec_val'
        try:
            temp_arr.append(float(item))
        except ValueError:
            temp_arr.append(pair_values[item])

    final_array.append(temp_arr)

    target.append(pair_values[temp[-1]])

# for i in final_array:
# 	print i
# 	raw_input()

# print len(final_array[0])

# raw_input()

# -------------------

# for line in dataset_lines:
# 	line = line.replace('\n', '').split(',')

# 	item = line[-1]

# 	# if item == 'exec':
# 	# 	item = 'exec_val'

# 	try:
# 		target.append(float(item))
# 	except ValueError:
# 		target.append(pair_values[item])



# print (target)

df_data = np.asarray(final_array)
df_target = np.asarray(target)

print type(df_data)
print type(df_target)

# data = np.asarray(final_array)
# target = np.asarray(svmc.target)

# data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.3, random_state=0)

# standardScalar = StandardScaler()

# standardScalar.fit(data_train)

# data_train_std = standardScalar.transform(data_train)
# data_test_std = standardScalar.transform(data_test)

# svm = SVC(kernel='linear', C=1.0, random_state=0)
# svm.fit(data_train_std, target_train)

# y_pred = svm.predict(data_test_std)
# print('Misclassified samples: %d' % (target_test != y_pred).sum())

# print('Accuracy: %.2f %%' % (accuracy_score(target_test, y_pred) * 100))
