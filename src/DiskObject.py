class DiskObject:
    """The DiscObject is used for handling a folder or file information."""
    object_size = 0
    object_path = ""
    is_directory = bool(0)

    def __init__(self, path, size, directory):
        self.object_path = path
        self.object_size = size
        self.is_directory = directory
