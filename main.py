# How to Copy Files and Rename them in Python

from shutil import copy

src_path = 'example.txt'
destination_path = 'example-new.txt'

copy(src_path, destination_path)

print('File copied and renamed successfully!')