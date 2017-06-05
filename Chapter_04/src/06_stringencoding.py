a_string = '深入 Python' 
print("a_string: ", a_string)
print("len(a_string): ", len(a_string))

by = a_string.encode('utf-8')
print("byte: ", by)
print("len(by): ", len(by))

by = a_string.encode('gb18030')
print("byte: ", by)
print("len(by): ", len(by))

by = a_string.encode('big5')
print("byte: ", by)
print("len(by): ", len(by))
roundtrip = by.decode('big5')
print(roundtrip)
