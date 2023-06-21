import sys, glob, os

# Get the directory name for correct OS
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a directory path for correct OS
directory = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# Making  a list of all files in directory
print(' ')
print('These are the complete list of folders')
print(' ')
print(glob.glob(directory))
list_of_folders = glob.glob(directory)

# TODO: use os.path.getsize to find each file's size
for x in list_of_folders:
    print(x, os.path.getsize(x))

# TODO: Add a test to only display files that are not zero length
print(' ')
print('These are folders that do not have size of 0')
print(' ')
list_of_folders = glob.glob(directory)
for x in list_of_folders:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
print(' ')
print('These are folders without the full directory that do not have size of 0')
print(' ')
list_of_folders = glob.glob(directory)
for x in list_of_folders:
    if os.path.getsize(x) > 0:
        print(os.path.basename(x), os.path.getsize(x))
