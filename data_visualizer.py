"""
This script contains methods which will help to visualize data.
"""


def show_pie_chart(data_count_dict):
    """Create a Pie chart
    :param data_count_dict: A dictionary containing item and count of item.
    :return None:
    """

    from pylab import *

    figure(1, figsize=(6, 6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    total = 0
    for i in data_count_dict.values():
        total += i

    label = []
    frac = []
    for key, val in data_count_dict.iteritems():
        label.append(key)
        frac.append(float(100 * val / total))

    pie(frac, labels=label, autopct='%1.1f%%', shadow=True, startangle=90)

    title('Raining Hogs and Dogs', bbox={'facecolor': '0.8', 'pad': 5})

    show()
