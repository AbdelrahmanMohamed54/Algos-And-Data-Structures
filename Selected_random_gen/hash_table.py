
from map_table import MapBase, UnsortedTableMap
from random import randrange

class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) \
                    % self._prime % len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        return bucket[k]
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j])>oldsize:
            self._n += 1
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        del bucket[k]
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                yield from bucket
