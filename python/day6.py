class Shape:
	def area(self):
		return 0
class Square(Shape):
	def __init__(self,l):
		self.l=l
		res=Shape.area(self)
		print(res)
	def area(self):
		Area=self.l*self.l
		return Area
obj=Square(5)
result=obj.area()
print(result)

class Person:
    def get_gender(self):
        print("male")


class Male(Person):
    def get_gender(self):
        print("male")


class Female(Person):
    def get_gender(self):
        print("female")


Male().get_gender()
Female().get_gender()
