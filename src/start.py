import DiskSizeUtility
import DiskObject

# The target folder for scanning.
scanpath = "C:\\Users\\"
# The result file.
filepath = "D:\\filesizescan.txt"

# Filters out all files, that are smaller that the threshold.
minimum_file_size_mb = 0

disk_util = DiskSizeUtility.DiskSizeUtility(scanpath)
print("Starting disk scan ...")

# Invoke a new scan.
disk_objects = disk_util.get_directories(minimum_file_size_mb)

print("Disk scan completed! Writing results to a file ..." + filepath)

f = open(filepath, "a", encoding="utf-8")

for i in disk_objects:
    if i.is_directory:
        f.write(f"Size of the folder including sub folders ({i.object_path}) is {i.object_size} MB")
    else:
        f.write(f"Size of the file ({i.object_path}) is {i.object_size} MB")
    f.write('\n')
f.close()

print("The operation has been completed. Please check the result file: " + filepath)
