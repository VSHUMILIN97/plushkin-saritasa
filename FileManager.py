class FileManager:

    def __init__(self, clone_groups, exceptions,
                 sc_files_num, sc_fold_num):
        self.clone_groups = dict(clone_groups)  # dict: {group_id:[file_clones]}
        self.exceptions = exceptions  # dict: {file:exception}
        self.scanned_files_num = sc_files_num  #
        self.scanned_folders_num = sc_fold_num
        self.duplications_num = len(clone_groups)
