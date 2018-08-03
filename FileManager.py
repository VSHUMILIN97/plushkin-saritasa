class FileManager:

    def __init__(self, clone_groups, exceptions):
        self.clone_groups = dict(clone_groups)  # dict: {group_id:[file_clones]}
        self.exceptions = exceptions  # dict: {file:exception}