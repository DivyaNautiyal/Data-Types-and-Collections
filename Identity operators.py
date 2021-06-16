'''Identity operators compare the memory locations of two objects. You already know by now that we use the id() to check memory location of an object. There are two Identity operators as explained below:

Operator: is
Description: Evaluates to true if the variables on either side of the operator point to the same object and false otherwise
Example: x is y, here is results in 1 if id(x) equals id(y)
 
 
Operator: is not
Description: Evaluates to false if the variables on either side of the operator point to the same object and true otherwise
Example: x is not y, here is not results in 1 if id(x) is not equal to id(y)'''

# initialize variables
x1 = 6142
y1 = 3629
x2 = 'Hello'
y2 = 'Hello'
d1={'a':1, 'b':2}
d2={'a':1, 'b':2}
# Code starts here

print(id(x1),id(y1))
x1_is_y1=id(x1) is id(y1)
print(x1_is_y1)


x2_is_y2=x2 is y2
print(x2_is_y2)

d1_is_d2=d1 is d2
print(d1_is_d2)