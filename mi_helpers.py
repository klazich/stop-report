import datetime
import os
import os.path as path
from directories import Directories

#  0  A  1  ITEM NUMBER              '@  l
#  1  B  2  INVENTORY MODEL GROUP    '@  c
#  2  C  3  SKIP LOT ID              '@  c
#  3  D  4  OVERRIDE INSPECTION      '@  c
#  4  E  5  MANUAL INSPECTION        '@  c
#  5  F  6  COUNTER STARTUP TRIGGER  '0  r
#  6  G  7  COUNTER TRIGGER          '0  r
#  7  H  8  COUNTER SKIPPED          '0  r

dr = Directories()

MI_DATA = dr.local.data.mi
TODAY = datetime.date.today().strftime('%Y%m%d')


def get_stop_data(date=TODAY, data_file=None):

    if data_file is not None:
        ax_data = path.normpath(data_file)
    else:
        ax_data = path.join(MI_DATA, '{}.txt'.format(date))

    dirname  = path.dirname(ax_data)
    basename = path.basename(ax_data)

    with open(ax_data, 'r') as in_file:
        a = in_file.read().split('\n')

    if a[0].startswith('Item number'):

        if not path.exists(path.join(dirname, '_')):
            os.mkdir(path.join(dirname, '_'))

        move_path = path.join(dirname, '_', basename)
        if path.exists(move_path):
            os.remove(move_path)
        os.rename(ax_data, move_path)

        headers = a[0]
        del a[::70]

    else:
        headers = a[0]
        del a[0]

    if a[-1] == '':
        del a[-1]

    data = '\n'.join([headers] + [x.replace(',', '') for x in a if not x.startswith('\t')])

    with open(ax_data, 'w') as out_file:
        out_file.write(data)

    return data


def format_mi_data(data):

    acc = []

    for l,line in enumerate(data.split('\t')):

