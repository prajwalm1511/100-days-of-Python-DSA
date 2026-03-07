###
# u can use list in print statement,u can't concatenate list, only happens with string
#inside list, u can put positive and negative numbers , remember numbering starts from 0
print("hello"[2]) #list

print("123_123" + "hello") #string

print(123_123_123) #large number

print(123.78) # float

print(123+11) # integer
print(123)

#true, false - boolean
###

###
# for len , the data type should be declared when we use len
#len(1234) # this is wrong
#len will return the length(number of items) of an object. argument/parameter should a sequence 
#string, bytes,tuple,list or range
# not integer
print(len("1234"))

# print( "no of letters in ur name:"+len(input("Enter your name ")))
# this line of code will show VALUE ERROR cause, we cant concatenate a str and an integer.
# here we use type conversion - int to str
print( "no of letters in ur name:"+str(len(input("Enter your name "))))
 

# round function
a= 22/7
print(round(a))
b=2/3
print(round(b,3))

