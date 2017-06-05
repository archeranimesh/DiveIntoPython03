import sys
sys.path.insert(0, '/home/animeshkbhadra/myWork/PythonLearning/books/DiveIntoPython03/Chapter_01/src/')
import humansize

username = "animeshb"
passoword = "12345"
print("{0}'s password is {1}".format(username, passoword))

si_suffixes = humansize.SUFFIXES[1000]
print("si_suffixes:: ", si_suffixes)
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))
print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))
print('{0:.1f}{1}'.format(698.24, 'GB'))
