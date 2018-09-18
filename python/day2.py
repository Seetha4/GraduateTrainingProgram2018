a=input("enter a year ")
if(a%4==0):
 print("leap year")
else:
 print("not a leap year")


a=raw_input("Enter a string ")
c=0
d=0
for i in a:
 if (i.isupper()):
  c+=1
 elif (i.islower()):
  d+=1
print("upper case %s" %c)
print("lower case %s" %d)



a=[]
for i in range(11):
 if(i%2==0):
  a.append(i)
print(a)
print(sum(a))


a=str(raw_input("enter numbers"))
x=[]
x=a.split(',')
c=tuple(x)
print(x) 
print(c)
