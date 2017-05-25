import os
import glob
import sys
sys.path.insert(0, '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/')
import humansize
pathname = '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_02/src/'

os.chdir(pathname)
pyList = glob.glob("*.py")
print(pyList)

metadata = [(f, os.stat(f)) for f in glob.glob("*.py") ]
print("\n\nmetadata:: ", metadata)

metadatadict = {f:os.stat(f) for f in glob.glob("*.py")} 
print("\n\nmetadatadict:: ", metadatadict)
print("\n\n", metadatadict['04_myfractions.py'].st_size)
print("\n\nKEYS:: ", metadatadict.keys())

humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) for f, meta in metadatadict.items() if meta.st_size > 500 }
print("\n\nhumsizeDict:: ", humansize_dict)
