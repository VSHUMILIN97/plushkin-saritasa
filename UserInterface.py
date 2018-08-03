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

        self.search_report = search_report

        self.big_line = \
            '---------------------------------------------------------'

        # statistic values for the overall report

        # count removed files
        self.removed_files = 0
        # count errors
        self.errors = 0
        # count cleaned size
        self.size_cleaned = 0

    def exceptions_information(self):
        """Information about exceptions that occurred during the search"""

        print("The next files can't be read:")

        for file in self.search_report.exceptions:
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
        print(
            'Duplications found:',
            self.search_report.duplications_num
        )

    def show_search_report(self):
        """Report that is shown in displaying mode"""

        self.general_information()

        self.exceptions_information()

        # for each group of duplicates that were found
        for group_id, file_clones in self.search_report.clone_groups.items():

            print(self.big_line)

            # show the file's size (as an instance, we take the first file)
            size = os.path.getsize(file_clones[0])
            print(f'size: {size} bytes')

            # show the date of creation the file
            date = time.ctime(os.path.getctime(file_clones[0]))

            # list all files
            for file in file_clones:
                print(f'[{file.index()}]: {file} (Created: {date})')

            print(self.big_line)

    def show_cleaning_input(self, group_index):
        """Input interface that is shown in interacting mode"""

        self.general_information()

        self.exceptions_information()

        print(self.big_line)
        print('CLEANING started')
        print(self.big_line)

        # list files from the particular group
        for file in self.search_report.clone_groups[group_index]:
            print(f'[{file.index()}]: {file} (Created: {date})')

        # let a user choose which of them to keep
        file_to_keep = input(
            'Choose file to keep by entering '
            'its number or press enter to skip it'
        )

        # notify the user's decision
        print(
            f'File'
            f' {self.search_report.clone_groups[group_index][file_to_keep]}'
            f' was kept'
        )

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

        print("Errors occurred:")
        for error in cleaner_report[0]:
            print(error)

        print('Files removed:', cleaner_report[1])
        print('Errors:', cleaner_report[3])
        print('Size_cleaned:', cleaner_report[2])

        # add their values to overall variables
        self.removed_files += cleaner_report[1]
        self.size_cleaned += cleaner_report[2]
        self.errors += cleaner_report[3]

    def overall(self):
        """The overall report that covers all statistics"""

        print(self.big_line)
        print('CLEANING finished')
        print(self.big_line)

        # print overall information
        print('Files removed:', self.removed_files)
        print('Errors:', self.errors)
        print('Size_cleaned:', self.size_cleaned)


def main():
    pass


if __name__ == '__main__':
    main()





