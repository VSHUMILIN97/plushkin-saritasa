import glob
import filecmp
import os
from FileManager import FileManager


class Searcher:
    @staticmethod
    def search_clones(path):
        """
        Searches for all file clones in path,
        including files in directories
        Returns: FileManager - contains all found file clones

        """
        errors_reading_files = set()  # dict: {file_name}
        files = Searcher.get_all_files_in_path(path)
        number_of_scanned_folders = len([x[0] for x in os.walk(path)])
        groups_of_clones = {1: []}  # dict: {group_id:[file_names]}
        id = 0
        for file_name in files:
            try:
                file1 = open(file_name)
                for group in groups_of_clones.values():
                    flag_break = False
                    for file2_name in group:
                        file2 = open(file2_name)
                        if filecmp.cmp(file1, file2):
                            group.append(file_name)
                            flag_break = True
                            break
                    if flag_break:
                        break
                else:
                    groups_of_clones[id] = [file_name]
                    id += 1

            except BaseException:
                errors_reading_files.add(file_name)

        return FileManager(clone_groups=groups_of_clones, exceptions=errors_reading_files,
                           sc_files_num=len(files), sc_fold_num=number_of_scanned_folders, fold_name=path)

    @staticmethod
    def get_all_files_in_path(path):
        return tuple(glob.glob("{}/**/.*".format(path), recursive=True))

    @staticmethod
    def test():
        print(open('asdf'))

