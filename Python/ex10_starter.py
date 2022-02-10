import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print(hdir)
# TODO: Use the glob.glob() function to obtain the list of filenames

#printing out list of file names in home directory
home_directory = glob.glob(pattern)
for filename in home_directory:   #make glob.glob(pattern) a variable
    print(filename)
    size = os.path.getsize(filename)
    if size != 0:
        print("size of '%s' in bytes: " % filename, size)
# TODO: use os.path.getsize to find each file's size
#this is the size of the file that describes the directory

#prints the number of files/subdirectories in the path
no_of_files = (len(os.listdir(hdir)))
#prints the size of files in the directory
allfiles = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))

# TODO: Add a test to only display files that are not zero length


# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
basename = os.path.basename(pattern)
print(basename)
shortfiles = glob.glob(basename)
print(shortfiles)

