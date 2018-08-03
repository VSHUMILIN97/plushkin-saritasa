import os
import sys


class Cleaner:

    __slots__ = ['group', 'error_counter', 'error_list', 'size_cleaned']

    def __init__(self, group, index):
        self.group = [x for x in group]
        self.error_counter = 0
        self.error_list = []
        self.size_cleaned = 0
        self.group.pop(index)

    def __remove(self):
        for path in self.group:
            if os.path.isfile(path):
                try:
                    self.size_cleaned = sys.getsizeof(path)
                    os.remove(path)
                except OSError as e:
                    self.error_list.append(f'{path} cannot be removed\n'
                                           f'{e}')
                    self.size_cleaned = 0
                    self.error_counter += 1
            else:
                self.error_list.append(f'{path} is not a file')

        return self.error_list, self.size_cleaned, self.error_counter,

    def report(self):
        return self.__remove()

