inventory = {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
                }
inventory['pocket']=['seashell', 'strange berry','lint']
inventory['backpack'].sort()
print("sort of backpack %s" %inventory['backpack'])
inventory['backpack'].remove('dagger')
print("sort of backpack %s" %inventory['backpack'])
inventory['gold']+=50
print(" gold list %s" %inventory['gold'])

d={}
i=raw_input("Enter no of students ")
x=0
while x<int(i):
	s=raw_input("enter the name ")
	r=raw_input("enter no of subjects ")
	d[s]=[]
	f=0
	while f<int(r):
		t=raw_input("enter the subject marks ")
		d[s].append(t)
		f+=1
	x+=1
print(d)
for k in d.keys():
	l=sum(d[k])
	h=l/r
	print("student name %s" %d[k])
	print("sum %s" %str(l))
	print("avg %s" %str(h))
