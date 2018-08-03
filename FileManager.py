class FileManager:
    """
    Class FileManager is a result of Searcher.search(path) method.
    It contains in itself such information as:
        Attributes:
             clone_groups: holds groups of file_clones
             unavailable_files: contains all file path that couldn't be read
             scanned_files_num: number of scanned files
             scanned_folders_num: number of scanned folders
             name_scanned_folder: name of scanned folder
    """

    def __init__(self, clone_groups, exceptions,
                 sc_files_num, sc_fold_num, folder_name):
        self.clone_groups = dict(clone_groups)  # dict: {group_id:[file_clones]}
        self.unavailable_files = exceptions  # set: {file}
        self.scanned_files_num = sc_files_num  #
        self.scanned_folders_num = sc_fold_num
        self.name_scanned_folder = folder_name
