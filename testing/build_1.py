# build_1.py

import values

# from pprint import pprint

dataset_file = open('corrected')

dataset_lines = dataset_file.readlines()

pair_values = values.get_list()

final_array = list()

for line in dataset_lines:
    line = line.replace('\n', '')

    items = line.split(',')

    temp_arr = []

    for item in items:
        if item == 'exec':
            item = 'exec_val'
        try:
            temp_arr.append(float(item))
        except ValueError:
            temp_arr.append(pair_values[item])

    final_array.append(temp_arr)

print len(final_array)
