import os
import time
import glob
import sys
sys.path.insert(0, '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/')
import humansize

pathname = '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_02/src/'
os.chdir(pathname)
print("os.path.getcwd(): ", os.getcwd())
print("glob.glob('*.py'): ")
#boolcontext.py
metadata = os.stat('boolcontext.py')
print("metadata:: ", metadata)
print("modified time:: ", time.localtime(metadata.st_mtime))
print("metadata.size: ", metadata.st_size)
print("proper size: ", humansize.approximate_size(metadata.st_size))
print("Real Path: ", os.path.realpath('boolcontext.py'))
