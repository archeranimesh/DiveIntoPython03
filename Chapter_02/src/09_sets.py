from boolcontext import is_it_true
a_set = {1}
print("a_set: ", a_set)
print("type(a_set): ", type(a_set))

a_set = {1, 2}
print("a_set: ", a_set)
print("type(a_set): ", type(a_set))

a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
print("a_set with list: ", a_set)

a_set = set()
print("type(a_set): ", type(a_set), " len(a_set): ", str(len(a_set)))

not_sure = {}       # Empty set is not created from {}
print("type(not_sure): ", type(not_sure), " len(not_sure): ", str(len(not_sure)))
not_sure = {1}
print("type(not_sure): ", type(not_sure), " len(not_sure): ", str(len(not_sure)))


a_set = {1, 2}
print("a_set.add(4): ", a_set.add(4), " new set: ", a_set, " len(a_set): ", str(len(a_set)))
print("a_set.add(1): ", a_set.add(1), " new set: ", a_set, " len(a_set): ", str(len(a_set)))        # Not adding duplicate entry

a_set = {1, 2, 3}
print("Original Set: ", a_set)
print("a_set.update({2, 4, 6}): ", a_set.update({2, 4, 6}), " new set: ", a_set)
print("a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13}): ", a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13}), " new set: ", a_set)
print("a_set.update([10, 20, 30]): ", a_set.update([10, 20, 30]), " new set: ", a_set)


a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print("\n\nOriginal Set: ", a_set)
print("a_set.discard(10): ", a_set.discard(10), " new set: ",a_set)
print("a_set.remove(21): ", a_set.remove(21), " new set: ", a_set)
try:
    print("a_set.remove(21): ", a_set.remove(21), " new set: ", a_set)
except KeyError as error:
    print("Removing a value from set not present raises: ", error)


a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print("Original Set: ", a_set)
print("a_set.pop(): ", a_set.pop())
print("a_set.pop(): ", a_set.pop())
print("a_set.pop(): ", a_set.pop())

print("a_set.clear(): ", a_set.clear())
try:
    print("a_set.pop(): ", a_set.pop())
except KeyError as error:
    print("Poping from empty set give: ", error)

print("\n\n=================================common set operations===========================================\n\n")
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
print("Original List: ", a_set)
print("30 in a_set: ", (30 in a_set))
print("31 in a_set: ", (31 in a_set))
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print("a_set: ", a_set)
print("b_set: ", b_set)
print("a_set.union(b_set): ", a_set.union(b_set))
print("a_set.intersection(b_set): ", a_set.intersection(b_set))
print("a_set.difference(b_set): ", a_set.difference(b_set))
print("a_set.symmetric_difference(b_set): ", a_set.symmetric_difference(b_set))
print("b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set): ", b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set))
print("b_set.union(a_set) == a_set.union(b_set): ", b_set.union(a_set) == a_set.union(b_set))
print("b_set.intersection(a_set) == a_set.intersection(b_set): ", b_set.intersection(a_set) == a_set.intersection(b_set))
print("b_set.difference(a_set) == a_set.difference(b_set): ", b_set.difference(a_set) == a_set.difference(b_set))

a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
print("a_set.issubset(b_set): ", a_set.issubset(b_set))
print("b_set.issuperset(a_set): ", b_set.issuperset(a_set))

print("is_it_true(set()): ", is_it_true(set()))
print("is_it_true({'a'}):  ", is_it_true({'a'}) )
