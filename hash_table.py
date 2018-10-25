from util import log


class HashTable(object):
    def __init__(self):
        self.size = 31
        self.table = []

        # Initialize the hash table
        for i in range(self.size):
            self.table.append([])

    def _hash(self, s):
        total = 0
        factor = 1



if __name__ == '__main__':
    test = HashTable()
    log(test.size)
    log(test.table)
