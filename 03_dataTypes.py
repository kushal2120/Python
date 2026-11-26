#data types
#checking data type: int
a = 1
b = 2
x = a + b
print(x)
print(type(x)) 

#checking data type: string
c = "1"
d = "2"
y = c + d
print(y)
print(type(y))

#basic data type in python
#1. Numeric
a1 = 3 #a. interger
a2 = 1.5 #b. float
print(type(a2))
a3 = complex(3,5) #c. complex
print(type(a3))

#2. Sequence
#a. String
b1 = "Kushal"
print(type(b1)) 
b11 = '26'
#b. list
b2 = [1,4,3,67, "kushal"]
print(type(b2))
#c. tuple
b3 = (1,4,2,57,'Kushal')
print(type(b3))

#3. Dictionary
#key, value pairs
my_dictionary = {'name': 'Kushal', 'age': 26, 'city': 'Prayagraj'}
print(type(my_dictionary))

#4. Sets
my_sets = {1,4,2,57,'Kushal'}
print(type(my_sets))

#5.Boolean

#6.Binary Type
#a.bytes
byte1 = b"Kushal"
#b.bytearray
#c.memoryview
