from datetime import datetime
import os

# OS name
print(os.name)

# OS system cpu count
print(os.cpu_count())


'''Working with Environment Variables'''

# OS environ
print(os.environ)  # returns a dictionary

# OS environ HOME
print(os.environ.get('HOME'))  # returns a string

# OS getenv
print(os.getenv('HOME'))  # returns a string

# OS envs with default
print(os.getenv('HOME', 'default'))  # returns a string


'''Working with Directories'''

# OS current working directory
print(os.getcwd())  # returns a string

# OS change directory
# os.chdir('/Users/robertbunch/Desktop')  # returns None

# OS current working directory
print(os.curdir)  # returns a string

# OS list directory
print(os.listdir())  # returns a list of strings

# OS make directory
os.mkdir('OS-Demo-2')  # returns None

# OS make directories
os.makedirs('OS-Demo-3/Sub-Dir-1')  # returns None

# OS remove directory
os.rmdir('OS-Demo-2')  # returns None

# OS remove directories
os.removedirs('OS-Demo-3/Sub-Dir-1')  # returns None


'''Working with Files'''

# OS create file
os.writeFile('test.txt', 'Hello World')  # returns None

# OS rename
os.rename('test.txt', 'demo.txt')  # returns None

# OS stat
print(os.stat('demo.txt'))  # returns a stat_result object

# OS stat file size
print(os.stat('demo.txt').st_size)

# OS stat file modified time
print(os.stat('demo.txt').st_mtime)  # returns a float

# OS report modified time
mod_time = os.stat('demo.txt').st_mtime

print(datetime.fromtimestamp(mod_time))  # returns a datetime object

# OS open file
fd = os.open('demo.txt', os.O_RDWR | os.O_CREAT)

# OS close file
os.close(fd)  # returns None

# OS remove file
os.remove('demo.txt')  # returns None

# OS walk through the directory tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


'''Working with Paths'''

# OS path join
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print(file_path)  # returns a string

# OS path basename
print(os.path.basename('/tmp/test.txt'))  # returns a string

# OS path dirname
print(os.path.dirname('/tmp/test.txt'))  # returns a string

# OS path split
print(os.path.split('/tmp/test.txt'))  # returns a tuple

# OS path exists
print(os.path.exists('/tmp/test.txt'))  # returns a boolean

# OS path isdir
print(os.path.isdir('/tmp/test.txt'))  # returns a boolean

# OS path isfile
print(os.path.isfile('/tmp/test.txt'))  # returns a boolean

# OS path splitext
print(os.path.splitext('/tmp/test.txt'))  # returns a tuple

# OS path splitext
print(os.path.splitext('/tmp/test.txt')[1])  # returns a extension string

# OS path splitext
print(os.path.splitext('/tmp/test.txt')[0])  # returns a file name string

# OS path splitext
print(os.path.splitext('/tmp/test.txt')[0] + '.bak')  # returns a path string

# OS path splitext
print(os.path.splitext('/tmp/test.txt')[0] + '.txt')  # returns a path string


'''Working with Process Parameters'''

# OS process id
print(os.getpid())  # returns an integer

# OS process parent id
print(os.getppid())  # returns an integer

# OS kill process
# os.kill(4532, signal.SIGKILL)

# OS kill process
# os.kill(4532, signal.SIGTERM)

# OS kill process
# os.kill(4532, signal.SIGINT)


'''Working with Permissions'''

# OS check access to path
print(os.access('test.txt', os.R_OK))  # returns a boolean

# OS chmod
# os.chmod('test.txt', 0o777)

# OS chown
# os.chown('test.txt', uid, gid)

# OS chroot
# os.chroot('/tmp')


# OS times
print(os.times())  # returns a tuple


'''Working with Links'''

# OS system
os.system('ls -l')

# OS system
os.system('pwd')

# OS system
os.system('touch test.txt')

# OS system
os.system('ls -l')
