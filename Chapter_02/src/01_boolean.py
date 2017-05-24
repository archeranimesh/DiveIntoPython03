size = 1
print("size = {0} size < 1 : {1}".format(size, size < 1))

size = 0 
print("size = {0} size < 0 : {1}".format(size, size < 0))
size = -1 
print("size = {0} size < 0 : {1}".format(size, size < 0))


print("Booleans can be used as numbers")
print("True + True = ", True + True)
print("True + False = ", True + False)
print("True * False = ", True * False)

try:
    print("Divide by zero : True/False = ", True/False)
except ZeroDivisionError as error:
    print(error)


