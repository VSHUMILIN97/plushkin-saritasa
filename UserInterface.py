"""UserInterface

This module is responsible for showing information to a user and interacting
with them

"""

import os
import time


class UserInterface:

    def __init__(self, search_report):
        """The constructor that saves search report

        Args:
            search_report (FileManager): report from the Search module.

        """

        self.__search_report = search_report

        self.big_line = \
            '---------------------------------------------------------'

        # statistic values for the overall report

        # count removed files
        self._removed_files = 0
        # count errors
        self._errors = 0
        # count cleaned size
        self._size_cleaned = 0

        # the amount of clone groups
        self.clone_groups_len = len(search_report.clone_groups)

    @property
    def search_report(self):
        return self.__search_report

    def exceptions_information(self):
        """Information about exceptions that occurred during the search"""

        if self.search_report.unavailable_files:
            print("The following files can't be read:")

        for file in self.search_report.unavailable_files:
            print(file)

    def general_information(self):
        """General information of the search's results"""

        print(
            'Scan report for folder:',
            self.search_report.name_scanned_folder
        )
        print(
            'Files scanned:',
            self.search_report.scanned_files_num
        )
        print(
            'Folders scanned:',
            self.search_report.scanned_folders_num
        )

    def show_search_report(self):
        """Report that is shown in displaying mode"""

        self.general_information()

        self.exceptions_information()

        # for each group of duplicates that were found
        for group_id, file_clones in self.search_report.clone_groups.items():

            print(self.big_line)

            print(
                'Duplications found:',
                len(file_clones)
            )

            # show the file's size (as an instance, we take the first file)
            size = os.path.getsize(file_clones[0])
            print(f'size: {size} bytes')

            # show the date of creation the file
            date = time.ctime(os.path.getctime(file_clones[0]))

            # list all files
            for file in file_clones:
                print(f'[{file_clones.index(file)}]: {file} (Created: {date})')

            print(self.big_line)

    def show_cleaning_input(self, group_index):
        """Input interface that is shown in interacting mode"""

        if group_index == 0:
            self.general_information()

            self.exceptions_information()

            print(self.big_line)
            print('CLEANING started')

        print(self.big_line)

        print(
            'Duplications found:',
            len(self.search_report.clone_groups[group_index])
        )

        # list files from the particular group
        for file in self.search_report.clone_groups[group_index]:

            # index of the duplicate
            index = self.search_report.clone_groups[group_index].index(file)

            # show the date of creation the file
            date = time.ctime(
                os.path.getctime(
                    self.search_report.clone_groups[group_index][0]
                )
            )

            print(f'[{index}]: {file} (Created: {date})')

        print(
            'Choose file to keep by entering its number or press enter to '
            'skip it\n'
        )

        while True:
            try:
                # let a user choose which of them to keep
                file_to_keep = input()

                if file_to_keep == '':
                    return 0, 0
                else:
                    file_to_keep = int(file_to_keep)

                print(
                    'File {} was kept'.format(
                        self.search_report.clone_groups[group_index][
                            file_to_keep]
                    )
                )
                break

            except (ValueError, IndexError) as e:
                print(e)

        # create a tuple for Cleaner, ([duplicates], which_to_delete)
        what_to_delete = (
            self.search_report.clone_groups[group_index],
            file_to_keep
        )

        # return it
        return what_to_delete

    def report(
            self,
            cleaner_report,
    ):
        """Report of the previous remove"""

        if cleaner_report[0]:
            print("Errors occurred:")
        for error in cleaner_report[0]:
            print(error)

        # add their values to overall variables
        self._removed_files += cleaner_report[1]
        self._size_cleaned += cleaner_report[2]
        self._errors += cleaner_report[3]

    def overall(self):
        """The overall report that covers all statistics"""

        print(self.big_line)
        print('CLEANING finished')
        print(self.big_line)

        # print overall information
        print('Files removed:', self._removed_files)
        print('Errors:', self._errors)
        print('Size_cleaned:', self._size_cleaned)


def main():
    pass


if __name__ == '__main__':
    main()
