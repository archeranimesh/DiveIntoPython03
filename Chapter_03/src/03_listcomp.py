import os
import glob
import sys
sys.path.insert(0, '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/')
import humansize
pathname = '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_02/src/'

a_list = [1, 9, 8, 4]
new_list = [elem * 2 for elem in a_list ]
print("Orig List: ", a_list)
print("New List: ", new_list)

os.chdir(pathname)
pyList = glob.glob("*.py")
print(pyList)

realPathList = [os.path.realpath(f) for f in glob.glob("*.py") ]

for eachfile in realPathList:
    print(eachfile)
    print(os.stat(eachfile).st_size)

filterlist = [ f for f in glob.glob("*.py") if os.stat(f).st_size > 500 ]
print(filterlist)

comliComprelist = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob("*.py") ]
print("\n\ncomliComprelist: ", comliComprelist)
comliComprelist = [(humansize.approximate_size(os.stat(f).st_size), os.path.realpath(f)) for f in glob.glob("*.py") ]
print("\n\ncomliComprelist: ", comliComprelist)
