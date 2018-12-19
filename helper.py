import datetime
import os
import os.path as path
from directories import Directories

#  0  A  1  ITEM NUMBER          '@      l
#  1  B  2  ITEM NAME            '@      l
#  2  C  3  LOCATION             '@      l
#  3  D  4  PALLET ID            '@      l
#  4  E  5  AVAILABLE INV        '0      r
#  5  F  6  INV VALUE IN TOTAL   '$0.00  r

dr = Directories()

STOP_DATA = dr.local.data.stop  # STOP Axapta reports directory
TODAY = datetime.date.today().strftime('%Y%m%d')


def get_stop_data(date=TODAY, data_file=None):
    if data_file is not None:
        ax_data = path.normpath(data_file)
    else:
        ax_data = path.join(STOP_DATA, '{}.txt'.format(date))

    dirname = path.dirname(ax_data)
    basename = path.basename(ax_data)

    with open(ax_data, 'r') as in_file:
        a = in_file.read().split('\n')

    if a[0].startswith('LINAK'):

        if not path.exists(path.join(dirname, '_')):
            os.mkdir(path.join(dirname, '_'))

        move_path = path.join(dirname, '_', basename)
        if path.exists(move_path):
            os.remove(move_path)
        os.rename(ax_data, move_path)

        headers = a[2]
        for i in range(3):
            del a[::71 - i]  # changed from 54 to 71

    else:
        headers = a[0]
        del a[0]

    if a[-1] == '':
        del a[-1]

    data = '\n'.join([headers] + [x.replace(',', '') for x in a if not x.startswith('\t')])

    with open(ax_data, 'w') as out_file:
        out_file.write(data)

    return data


def format_stop_data(data):
    acc = []

    for l, line in enumerate(data.split('\n')):

        sub = [None for _ in range(6)]
        line_arr = line.split('\t')
        if line_arr[4] == '0.00':
            continue  # don't add items with zero inventory

        for i, item in enumerate(line_arr):

            if l == 0 and i == 5:
                item = item.replace('Inventory', 'Inv')

            if item == '':
                item == None
            elif l in [0]:
                item = str(item)
            elif i in [0, 1, 2, 3]:
                item = str(item)
            elif i in [4]:
                item = int(float(item))
            elif i in [5]:
                item = float(item)

            sub[i] = item

        acc.append(sub)

    return acc


def sort_stop_data(data, col=5):
    table = sorted(data[1:], reverse=True, key=lambda x: x[col])
    data = [data[0]] + table

    return data


def get_value_total(data):
    return round(sum(n[5] for n in data[1:] if n[5] > 0), 2)
