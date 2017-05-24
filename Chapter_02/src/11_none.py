from boolcontext import is_it_true
print("type(None): ", type(None))
print("None == False: ", (None == False))
print("None == True: ", (None == True))
print("None == 0: ", None == 0)

print("is_it_true(None): ", is_it_true(None))
print("is_it_true(not None): ", is_it_true(not None))
