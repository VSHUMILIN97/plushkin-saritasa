import os
import sys
import collections

REPORT_TEMPLATE = collections.namedtuple(
    'REPORT', (
        'errors_occurred',
        'files_removed',
        'size_cleaned',
        'errors_counter',
    )
)


class Cleaner(object):
    """ Class that erase all files that stored in list
        except one, which index was fetched from UI

    Attributes:
        group (list): Stores all paths to files that are duplicates
        index (int): Index to path of the file,
                    that that user want to keep

    Notes:
        It is important, that this class is initialised every time
        for the every new group
        Slots strictly disallow to add new attributes for Cleaner instance
    """

    __slots__ = ['__delete_group',
                 '__errors_occurred',
                 '__size_cleaned',
                 '__files_removed']

    def __init__(self, group, index):
        try:
            self.__delete_group = [x for x in group]
            self.__delete_group.pop(index)
        except (TypeError, ValueError, KeyError):
            self.__delete_group = []
        self.__errors_occurred = []
        self.__size_cleaned = 0
        self.__files_removed = 0

    def __remove(self):
        """ Inner method that tries to delete all of the files
            given in group list and change inner attributes to
            complete the report file.

        Returns:
            None
        """
        for path in self.__delete_group:
            if not os.path.isfile(path):
                self.__errors_occurred.append(f'{path} is not a file!')
                continue
            try:
                self.__size_cleaned = sys.getsizeof(path)
                os.remove(path)
                self.__files_removed += 1
            except OSError:
                self.__errors_occurred.append(
                    f'{path} cannot be removed. No such file or directory!')
                self.__size_cleaned = 0

    def clean_and_report(self):
        """ Method runs inner method __remove to store values in

        Returns:
            tuple: Stores all the attributes for displaying in UI
        """
        self.__remove()
        return REPORT_TEMPLATE(
            errors_occurred=self.__errors_occurred,
            files_removed=self.__files_removed,
            size_cleaned=self.__size_cleaned,
            errors_counter=len(self.__errors_occurred),
        )
