def check(input_string):
    str = ""
    list = input_string.split()
    if len(input_string) > 0 and len(
            input_string) < 1000 and input_string.isalnum():
        for i in list:
            if i[0].isalpha():
                str += i.title() + " "
            else:
                str += i + " "

    print str

    str1 = raw_input("Enter a string: ")
    cap(str1)


student = {}
count = raw_input("Enter the student count")
for i in range(int(count)):
    name = raw_input("Enter the name")
    mark_list = []
    for j in range(3):
        marks = input("enter marks: ")
        mark_list.append(marks)
        student[name] = mark_list
print(student)
name = raw_input(" enter student name :")
if name in student:
    sum1 = sum(student[name])
    avg = sum1 / 3
    print(round(avg, 2))
else:
    print("No such student in the list")

try:
    dict = {}
    n = input("Enter the no of test case")
    for i in range(n):
        s = raw_input("Enter a and b")
        l1 = s.split(" ")
        dict[i] = l1
    for i in range(n):
        print int(dict[i][0]) / int(dict[i][1])
    #print dict
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
except ValueError as Argument:
    print("Error Code: invalid literal for int() with base 10:%s" % l[1])

dict={}
l=[]
n=input("Enter the no of commands")
for i in range(n):
      s=raw_input();
      l1=s.split(" ")
      dict[i]=l1
print dict
for i in range(n):
      if(dict[i][0]=="insert"):
           l.insert(int(dict[i][1]),int(dict[i][2]))
      elif(dict[i][0]=="print"):
           print l
      elif(dict[i][0]=="remove"):
           l.remove(int(dict[i][1]))
      elif(dict[i][0]=="append"):
           l.append(int(dict[i][1]))
      elif(dict[i][0]=="sort"):
           l.sort()
      elif(dict[i][0]=="pop"):
           l.pop(len(l)-1)
      elif(dict[i][0]=="reverse"):
           l.reverse()
