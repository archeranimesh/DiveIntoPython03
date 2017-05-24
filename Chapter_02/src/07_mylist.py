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
print("a + ['g', 'l']: ", a + ['g', 'l'])
