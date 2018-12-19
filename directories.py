import os
from os.path import normpath, join, exists

LOCAL_DRIVE = 'C:/Users/uskla/Desktop/reports'
ONE_DRIVE = 'C:/Users/uskla/OneDrive - LINAK/reports'
F_DRIVE = 'F:/Operations/QUALITY/QUALITY SYSTEMS/Quality log reports'


def make_dir(root, name=None):
    d = root if name is None else join(root, name)
    if not exists(d):
        os.mkdir(d)
    return normpath(d)


class Directories:
    def __init__(self):
        self._local = MakeLocal(normpath(LOCAL_DRIVE))
        self._onedrive = MakeTree(normpath(ONE_DRIVE))
        self._fdrive = MakeTree(normpath(F_DRIVE))

    def __iter__(self):
        return (d for d in [self._local, self._onedrive, self._fdrive])

    def list(self):
        return list(self.__iter__())

    @property
    def local(self):
        return self._local

    @property
    def onedrive(self):
        return self._onedrive

    @property
    def fdrive(self):
        return self._fdrive


class MakeTree(dict):
    __slots__ = []

    def __init__(self, root, subs=('stop', 'mi')):
        self.update({'root': root})
        for s in subs:
            self.update({s: make_dir(root, s)})

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, name, value):
        raise Exception('directories are read only')


class MakeLocal(MakeTree):
    def __init__(self, root):
        MakeTree.__init__(self, root)

        self.update({'data': MakeTree(make_dir(root, 'data'), subs=['stop', 'mi'])})
