# list comprehension
x = [100,110,120,130,140,150]
y=[]
for i in x:1
c=i*5
y.append(c)
print(y)
# testing for conditions
def divisible_by_three(n):
        for number in range(n):
            if number%3==0:
              return "{} is divisible by 3".format(number)
        else:
         return "{} is not divisible by 3".format(number)

print(divisible_by_three(20))
x = [[1,2],[3,4],[5,6]]
z=[]
def flatten():
    a=x[0][0],x[0][1],x[1][0],x[1][1],x[2][0],x[2][1]
    z.append(a)
    return z
print(flatten())
# finding the minimum value in a list
def smallest(*args):
   b=[args]
   x=min(b)
   return x
print(smallest(9,5,18,19,11,25,1))

# sets
x = ['a','b','a','e','d','b','c','e','f','g','h']
b=set(x)
c=list(b)
print(c)

def divisible_by_seven():
    my_list=[]
    for num in range(100,200):
        if num%7==0:
            my_list.append(num)
            return my_list
        else:
            return "{} is not divisible by 7".format(num)

print(divisible_by_seven())

students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
for student  in students:
    name=student["name"]
    year=2021-student["age"]
greeting="Hello {}.You were born in the year {}".format(name,year)
print(greeting)

# classes
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def Area(self):
        area=self.width*self.length
        return "The area of this rectangle is {}".format(area)

    def perimeter(self):
        perimeter=self.length+self.width+self.length+self.width
        return "The perimeter is of this rectangle is {}".format(perimeter)

rectangle=Rectangle(10,20)
print(rectangle.Area())
print(rectangle.perimeter())





