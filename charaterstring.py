# print string
message = "'This is an example of string'"
print (message)

# newline
message= "First line. \nSecond Line\nThird Line "
print (message)

# many lines
message = ("""\
this is an example
of message
that contains
many lines
""")
print (message)

# concatenate
message = "new" + "line"
print (message)

message = 3 * 'ta' + 'ra'
print (message)

message = 'Py' 'Thon' ' 3.2'
print(message)

message = ('First Line'
           ' Second Line'
           ' Third line')
print(message)

# index string
index = 'Python'
print (index[0])
print (index[1])
print (index[2])
print (index[3])
print (index[4])
print (index[5])

print (index[-1])
print (index[-2])
print (index[-3])
print (index[-4])
print (index[-5])
print (index[-6])

# substring
string = "this is an string"

print (string[0:3])
print (string[-1])
print (string[1:3])
print (string[:3]) # from the start to an index
print (string[3:]) # from an index until the finish
print (string[-2:])

#len
string = "alksjdklasjdklajsdklajsdljalsdjlasasdasdasdad"
print (len(string))

#upper and lower
string = "escuela"
print (string.upper())
print (string.lower())
