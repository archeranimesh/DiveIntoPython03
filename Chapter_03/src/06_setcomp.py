a_set = set(range(10))
print(a_set)

new_set = { x **2 for x in a_set }
print(new_set)

another_set = {x for x in a_set if x % 2 == 0 }
print(another_set)

yanother_set = {2 ** x for x in range(10) }
print(yanother_set)
