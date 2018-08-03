import glob
import filecmp
import os
from FileManager import FileManager


class Searcher:
    """
    Class that provides finding all clone files
     in specified path recursively
    """

    @staticmethod
    def search_clones(path):
        """
        Searches for all file clones in path,
        including files in directories
        Returns: FileManager - contains all found file clones and other info,
        for more information look at FileManager

        """
        errors_reading_files = set()  # dict: {file_name}
        files = Searcher.get_all_files_in_path(path)
        number_of_scanned_folders = len([x[0] for x in os.walk(path)])  # getting number of subdirectories in path
        groups_of_clones = {}  # dict: {group_id:[file_names]}
        id = 0
        for file_name in files:
            try:
                for group in groups_of_clones.values():
                    flag_break = False

                    for file2_name in group:
                        if filecmp.cmp(file_name, file2_name):
                            group.append(file_name)
                            flag_break = True
                            break

                    if flag_break:
                        break
                else:
                    # if clone not found creating new list with file_name in it
                    groups_of_clones[id] = [file_name]
                    id += 1

            except BaseException:
                errors_reading_files.add(file_name)

        id = 0
        groups_of_clones_exclude_1 = {}
        for x, y in groups_of_clones.items():
            if len(groups_of_clones[x]) > 1:
                groups_of_clones_exclude_1[id] = y[:]
                id += 1

        # groups_of_clones = {x: y for x, y in groups_of_clones.items() if len(y) > 1}

        return FileManager(clone_groups=groups_of_clones_exclude_1, exceptions=errors_reading_files,
                           sc_files_num=len(files), sc_fold_num=number_of_scanned_folders, folder_name=path)

    @staticmethod
    def get_all_files_in_path(path):
        return tuple(glob.glob("{}/**/*.*".format(path), recursive=True))
