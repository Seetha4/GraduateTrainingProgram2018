from heapq import nlargest
name = list(raw_input("enter the name:"))
a = {}
if(len(name) > 3 and len(name) < 100):
    for i in name:
        a[i] = name.count(i)
    print(a)
    if(len(a) > 3):
        three_largest = nlargest(3, a, key=a.get)
        for i in three_largest:
            for k, v in a.iteritems():
                if(k == i):
                    print k, v
    else:
        print("enter atleast 3 distinct characters")
else:
    print("enter correct value")
