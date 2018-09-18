a=''
b=''
a=raw_input("Enter first name")
b=raw_input("Enter second name")
print("full name %s%s" %(a,b))


a=raw_input("Enter full name ")
b=raw_input("Enter age ")
print("First name %s" %a[0:6])
print("second name %s" %a[7:14])
print("age %s" %b)


a=input("enter number")
b=input("enter number")
c=input("enter number")
if a==b or b==c or c==a:
 print("sum =0")
else:
 d=a+b+c
 print("sum %s" %d)


var="26/05/1997"
sum=int(var[0])+int(var[1])+int(var[3])+int(var[4])+int(var[6])+int(var[7])+int(var[8])+int(var[9])
print(sum)


str1 = 'Hello'

str2 ='World!'


print('str1 + str2 = ', str1 + str2)


print('str1 * 3 =', str1 * 3)


str = "hellooo"
print "str.capitalize() : ", str.capitalize()

str = "hellooo"
print "Length of the string: ", len(str)

str = "HELLOOO"
print str.lower()

str = "hellooo"
print "Max character: " + max(str)

str = "hellooo"
print "Min character: " + min(str)

str = "0000000hellooo0000000";
print str.strip( '0' )

str = "hellooo"
print str.replace("e", "a")
print str.replace("o", "r", 1)
