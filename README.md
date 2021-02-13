# FindLargeDiskFiles
A small python demo, that collects large filenames and write them into a text file.
It should help to identify large unused files that increase your disk usage.

Folders like `C:\User\myUser\AppData` are growing over the years.

Example result:
`Size of the folder including subfolders (C:\Users\myuser\AppData) is 34433 MB
Size of the folder including subfolders (C:\Users\myuser\AppData\Local) is 27064 MB`


Parameter:

`start.py arg1=scanfolder arg2=Resultfile arg3=minimumscansize`

`python ./src/start.py C:\\Users\\ D:\\filesizescan.txt 5`

_Written in Python 3.9_