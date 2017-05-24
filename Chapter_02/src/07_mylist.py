from boolcontext import is_it_true

a = ['a', 'b', 'mpilgrim', 'z', 'example']
print("The list is: a: ", a)
print("indexing in list a[0]: ", a[0])
print("indexing in list a[1]: ", a[1])
print("indexing in list a[-1]: ", a[-1])
print("indexing in list a[-3]: ", a[-3])
print("indexing in list a[len(a) - 3]: ", a[len(a) - 3]," str(len(a) -3): " ,str(len(a) - 3))

print("\n\n=================list slice================================\n")

print("list a: ", a)
print('a[1:3]: ', a[1:3])
print('a[1:-1]: ', a[1:-1])
print('a[0:3]: ', a[0:3])
print('a[:3]: ', a[:3])
print('a[3:]: ', a[3:])
print('a[:]: ', a[:])


print("\n\n=================list Updation================================\n")
print("Original List: a = ", a)
print("a + ['g', 'l']: ", a + ['g', 'l'])
print("a.append(True): ", a.append(True), " list: ", a)
print("a.extend(['four', 't']): ", a.extend(['four', 't']), " List: " ,a)
print("a.insert(0, 'p'): ", a.insert(0, 'p'), " list: ", a)


print("\n\n==================Extend vs Append===============================\n")
print("original list: ", a)
a.extend(['d', 'e', 'f'])
print("extended list a.extend(['d', 'e', 'f']) : ", a, " length: ", str(len(a)), " last element: ", a[len(a) - 1])
a.append(['g', 'h', 'i'])
print("appended list a.append(['g', 'h', 'i']) : ", a, " length: ", str(len(a)), " last element: ", a[len(a) - 1])


print("\n\n==================list searching==================================\n")
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print("original list: ", a_list)
print("a_list.count('new']: ", a_list.count('new')) # returns the first instance which matched.
print("'new' in a_list: ", ('new' in a_list))
print("a_list.index('mpilgrim') : ", a_list.index('mpilgrim'))

try:
    a_list.index('c')
except ValueError as error:
    print("When a value is not in a list it returns a ValueError")
    print(error)


print("\n\n==================Delete List======================================\n")
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print("Original List: ", a_list)
print("Before deletion a_list[1]: ", a_list[1])
del a_list[1]
print("After deletion a_list[1]: ", a_list[1], " list: ", a_list)
print("Remove with content: a_list.remove('new'): ", a_list.remove('new'), " list: ", a_list)   # Deletes the first occurence.
a_list.remove('new')
print("Current List: ", a_list)
try:
    a_list.remove('new')    # Returns a ValueError
except ValueError as error:
    print(error)

a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print("Original List: ", a_list)
print("a_list.pop(): ", a_list.pop(), " list: ", a_list)
print("a_list.pop(1): ", a_list.pop(1), " list: ", a_list)
print("a_list.pop(): ", a_list.pop(), " list: ", a_list)
print("a_list.pop(): ", a_list.pop(), " list: ", a_list)
print("a_list.pop(): ", a_list.pop(), " list: ", a_list)
try:
    print("a_list.pop(): ", a_list.pop(), " list: ", a_list)
except IndexError as error:
    print("Poping from empty list gives: ", error)


print("\n\n===================Boolean Content=====================================\n")
print("is_it_true([]): ", is_it_true([]))
print("is_it_true(['a']): ", is_it_true(['a']))
print("is_it_true([False]): ", is_it_true([False]))
