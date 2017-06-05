by = b'abcd\x65'
print("by: ", by)
print("type(by): ", type(by))
print("len(by): ", len(by))
by += b'\xff'
print("by: ", by)
print("len(by): ", len(by))
print('by[0]: ', by[0])

try:
    by[0] = 102
except TypeError as error:
    print(error)

barr = bytearray(by)
print("barr: ", barr)
print("len(barr): ", len(barr))
barr[0] = 102
print("barr: ", barr)

by = b'd'
s = 'abcde'
try:
    by + s
except TypeError as error:
    print(error)

try:
    s.count(by)
except TypeError as error:
    print(error)

print(s.count(by.decode('ascii')))
