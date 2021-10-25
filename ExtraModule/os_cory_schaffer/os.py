import os
from datetime import datetime


# All for os molule.
# print(dir(os))


# Current Directory
# print(os.getcwd())

# Changing directories
# /ExtraModule/os_cory_schaffer
# os.chdir('/home/mlobf/Documents/my_git/new_pandas_course/new_pandas_course/')
# print(os.getcwd())


# Listing Directories
# print(os.listdir())

# How to create a new folder name
nf = 'OS-DEMO-2'

try:
    os.rmdir(nf)
    # os.removedirs(nf)

except Exception:
    pass


# os.mkdir(nf)
# This method allow sub directories.
# os.makedirs("OS_DEMO/Sub-Dir-1")


# to rename a folder,
try:
    os.rename('test.txt', 'demo.txt')
except Exception:
    pass


# to show all info of a file.
# print(os.stat('os.py'))

# To Show to last modification time date.
# lmt = os.stat(('os.py')).st_mtime
# print(datetime.fromtimestamp(lmt))

# The os.walk method

current_dir = os.getcwd()
# current_dir = "/home/mlobf/"
# print(current_dir)

# for dirpath, dirnames, filenames in os.walk(current_dir):
# for _ in os.walk(current_dir):
# print(' ')
# print(_)

# print(os.walk())

# print(os.listdir())


# To remove directories recursion
# os.removedirs()
# To remove directories
# os.rmdir()


# To rename a file or a folder
# os.rename(original, renamed)


# to see the variables's environment
# print(os.environ)

# To see a specific variables's environment
# print(os.environ.get('HOME'))

# To join a path in os.
#file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)


# To check is a os path exist.
# print(os.path.exists('/tmp/'))

# To check if something is a directory or a file.
# To dir
# print(os.path.isdir('/tmp/'))
# To file
# print(os.path.isfile('/tmp/'))

# To split the root and the filename.
the_path = '/home/mlobf/text.txt'
print(os.path.splitext(the_path)[0])
print(os.path.splitext(the_path)[1])

# Para checar o tipo de arquivo.
# print((os.path.splitext(the_path)[1]))

# print(os.path.splitext(the_path))

my_generator = os.walk(the_path)


# print(my_generator.__next__())

for x in my_generator:
    print(str(x))
