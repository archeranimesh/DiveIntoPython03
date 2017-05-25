import os

print("os.getcwd(): ", os.getcwd())
os.chdir("../")
print("After chdir os.getcwd(): ", os.getcwd())
print("os.path.join('/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src', humansize.py): ", os.path.join('/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src', 'humansize.py'))
# "myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/humansize.py"
print("os.path.expanduser('~'): ", os.path.expanduser('~'))
print("os.path.join(os.path.expanduser('~'), 'myWork', 'PythonLearning', 'books', 'DiveIntoPython03', 'Chapter_01', 'src', 'humansize.py'):: " ,os.path.join(os.path.expanduser('~'), 'myWork', 'PythonLearning', 'books', 'DiveIntoPython03', 'Chapter_01', 'src', 'humansize.py'))

pathname = '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/humansize.py'
print('os.path.split(pathname) :: ', os.path.split(pathname))
(directory, filename) = os.path.split(pathname)
print("directory:: ", directory, " filename:: ", filename)
(shortname, extension) = os.path.splitext(filename)
print("shortname:: ", shortname, " extension: ", extension)
