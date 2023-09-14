from zipfile import ZipFile

# Create a Zip
with ZipFile('my_zip.zip', 'w') as zip:
    zip.write('my_file.txt')
    zip.write('my_folder')

# Extract a Zip
with ZipFile('my_zip.zip', 'r') as zip:
    zip.extractall("new_folder")

# Read a Zip
with ZipFile('my_zip.zip', 'r') as zip:
    print(zip.namelist())
    print(zip.getinfo('my_file.txt'))
    print(zip.read('my_file.txt'))
    zip.extract('my_file.txt')
