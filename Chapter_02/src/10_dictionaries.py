from boolcontext import is_it_true
a_dict = {
    'server': 'db.diveintopython3.org',
    'database': 'mysql'
}
print("original dict: ", a_dict)
print("a_dict['server']: ", a_dict['server'])
print("a_dict['database']: ", a_dict['database'])
try:
    print("a_dict['db.diveintopython3.org']: ", a_dict['db.diveintopython3.org'])
except KeyError as error:
    print("Error when accessing a value: ", error)

print("\n\n================================Modifying Dict=============================\n")    
a_dict['database'] = 'blog'
print("a_dict['database']: ", a_dict['database'])
a_dict['user'] = 'dora'
print("Modified Dict: ", a_dict)
a_dict['User'] = 'mark'
print("Modified Dict: ", a_dict)

print("is_it_true({}): ", is_it_true({}))
print("is_it_true({'a': 1}) : ", is_it_true({'a': 1}))
