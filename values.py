# values.py
# This module will go through the files_list, each file in the list contains
# a bunch of key=value pair.
#
# This python script will create a dictionary from the key=value pair.

value_dict = {}

tag = 'key_val/'

files_list = ['attack.py', 'protocols.py', 'service.py', 'flags.py']

debug = True


def get_list():
    for file in files_list:
        with open(tag + file) as f:
            all_lines = f.readlines()

        for line in all_lines:
            if line == '' or line == '\n':
                continue

            val = line.split('=')

            if debug:
                print val

            value_dict[val[0]] = int(val[1])

    return value_dict
