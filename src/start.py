#!/usr/bin/python
import DiskSizeUtility
import DiskObject
import sys


def get_help():
    """ Prints the help text for the '-p' argument """
    print("start.py Scanfolder:[arg1] Resultfile[arg2] Minimum size in megabyte[arg3]")
    print("Example: python ./src/start.py 'C:\\Users\\' 'D:\\filesizescan.txt'")


def run(scan_path, file_path, minimum_file_size_mb):
    """ Invokes a scan of a folder. Uses scan_path, file_path and minimum_file_size_mb as arguments."""
    disk_util = DiskSizeUtility.DiskSizeUtility(scan_path)
    print("Starting disk scan ...")

    # Invoke a new scan.
    disk_objects = disk_util.get_directories(int(minimum_file_size_mb))

    print("Disk scan completed! Writing results to a file ..." + file_path)
    # prepare file for results
    f = open(file_path, "a", encoding="utf-8")

    # iterating through the results and printing the folders out.
    for i in disk_objects:
        if i.is_directory:
            f.write(f"Size of the folder including sub folders ({i.object_path}) is {i.object_size} MB")
        else:
            f.write(f"Size of the file ({i.object_path}) is {i.object_size} MB")
        f.write('\n')
    f.close()

    print("The operation has been completed. Please check the result file: " + file_path)


# The help text for the '-h' argument
if "-h" in sys.argv:
    print('Number of arguments:', len(sys.argv), 'arguments.')
    get_help()
    sys.exit(0)

# Check, if there are not enough arguments to run this method.
if len(sys.argv) < 4:
    print("Error: Three arguments required.")
    get_help()
    sys.exit(1)

print(sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])

run(sys.argv[1], sys.argv[2], sys.argv[3])
