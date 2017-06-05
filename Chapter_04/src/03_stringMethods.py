myString = '''Finished files are the re-
                sult of years of scientif-
                ic study combined with the
                experience of years'''
print("myString.splitlines: ", myString.splitlines())               
print("myString.lower(): ", myString.lower())
print("myString.lower().count('f'): ", myString.lower().count('f'))

query = "user=pilgrim&database=master&password=PapayaWhip"
a_list = query.split('&')
print("a_list: ", a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v ]
print("a_list_of_lists:: ", a_list_of_lists)
a_dict = dict(a_list_of_lists)
print("a_dict: ", a_dict)
