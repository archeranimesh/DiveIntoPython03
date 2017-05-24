from boolcontext import is_it_true
a_tuple = ("a", "b", "mpilgrim", "z", "example")
print("Original Tuple: ", a_tuple)
print("a_tuple[0]: ", a_tuple[0])
print("a_tuple[-1]: ", a_tuple[-1])
print("a_tuple[1:3]: ", a_tuple[1:3])
try:
    a_tuple.append('new')
except AttributeError as error:
    print("Appending to a tuple gives error: ", error)
try:
    a_tuple.remove('a')
except AttributeError as error:
    print("Removing from a tuple gives error: ", error)

print("a_tuple.index('example'): ", a_tuple.index('example'))
print("'z' in a_tuple: ", ('z' in a_tuple))
print("is_it_true(()): ", is_it_true(()))
print("is_it_true(('a', 'b')): ", is_it_true( ('a', 'b')  )) 
print("is_it_true((False)): ", is_it_true((False)))
print("is_it_true((False, )): ", is_it_true((False, )))

v = ('a', 2, True)
(x, y, z)  = v
print("x ", x)
print("y ", y)
print("z: ", z)

(MONDAY, TUESDAY, WEDNESSDAY, THRUSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(MONDAY)
