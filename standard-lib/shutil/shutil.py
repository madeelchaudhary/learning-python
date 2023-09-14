from shutil import copy, move
from pathlib import Path

source = Path.cwd() / 'my_folder' / 'my_file.txt'
destination = Path.cwd() / 'my_folder' / 'new_folder'

#  Copy a file
copy(source, destination)

#  Move a file
move(source, destination)
