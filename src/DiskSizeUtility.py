import os
import DiskObject


def get_size(path, entries):
    size = 0

    for entry in entries:
        if entry.object_path.startswith(path) and entry.is_directory is False:
            size = size + entry.object_size
    return size


class DiskSizeUtility:
    rootFolder = ""

    def __init__(self, target_folder):
        self.rootFolder = target_folder

    def get_directories(self, minimum_file_size_mb):
        entries = []
        result_directories = []
        for root, directories, files in os.walk(self.rootFolder, topdown=False):
            for name in files:
                fi = os.path.join(root, name)
                # File size in megabyte
                file_size = int(os.path.getsize(fi) / 1024 / 1024)
                if file_size > 0:
                    entry = DiskObject.DiskObject(fi, file_size, bool(0))
                    # print(f"Size of the file ({fi}) is {file_size} MB")
                    entries.append(entry)

            for directory in directories:
                size = 0
                dir_path = os.path.join(root, directory)
                matches = filter(lambda x: dir_path in x.object_path, entries)

                for entry in matches:
                    size = size + entry.object_size

                if size >= minimum_file_size_mb and size != 0:
                    scan_dir = DiskObject.DiskObject(dir_path, size, True)
                    result_directories.append(scan_dir)

        # Sort the entries by size.
        entries.extend(result_directories)
        entries.sort(key=lambda x: x.object_size, reverse=True)
        # Contains all investigated values
        return entries
