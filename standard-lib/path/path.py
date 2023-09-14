from pathlib import Path
from time import ctime

Path.cwd()  # Current working directory
Path.home()  # Home directory

# Working with files and folders
Path('my_folder').mkdir()  # Create a folder
Path('my_folder').rmdir()  # Remove a folder
Path('my_file.txt').touch()  # Create a file
Path('my_file.txt').unlink()  # Remove a file
Path('my_file.txt').rename('my_file.py')  # Rename a file or folder


path = Path(Path.cwd(), 'my_folder', 'my_file.txt')
# or
path = Path.joinpath(Path.cwd(), 'my_folder', 'my_file.txt')  # Join paths
# or
path = Path.cwd() / 'my_folder' / 'my_file.txt'
path.iterdir()  # Iterate over the content of the directory
path.glob('*.txt')  # Iterate over the content of the directory with a pattern
path.rglob('*.txt')  # Iterate over the content of the directory recursively

path.exists()  # Check if the path exists
path.is_file()  # Check if the path is a file
path.is_dir()  # Check if the path is a directory
path.absolute()  # Return the absolute path
path.name  # Get the name of the file
path.stem  # Get the name of the file without the extension
path.suffix  # Get the extension of the file
path.parent  # Get the parent directory of the file
path.with_suffix('.py')  # return a new path with the suffix changed
path.with_name('my_file.py')  # return a new path with the name changed

print(path)
print(ctime(path.stat().st_ctime))  # Get the creation time of the file

path.write_text('Hello World')  # Write text to a file
path.read_text()  # Read text from a file

path.chmod(0o755)  # Change the permissions of a file
