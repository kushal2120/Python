#casting in python- changing one data type to another

a = 1
print(type(a)) 
b = "1"
print(type(b))

c = a + int(b)
print(c)

#all string type can't be casted into numerical type
# name = "kushal"
# newName = int(name)
# print(newName) #shows error

#all numerical type can be into string
muNum = 26
myNum2 = str(myNum)
print(type(myNum2))


f1 = 22.45
f2 = int(f1)
print(f2)
print(type(f2))

in1 = 24
in2 = float(in1)
print(type(in2))

#implicit casting = by default or automatically change data type
var1 = 10 #int type
var2 = 15.5 #float type
var3 = var1 + var2
print(var3)
print(type(var3))

#explicit casting = performed manually 
#above all code are explicit
intNum = 101
strNum = str(intNum)
print(type(strNum))

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))