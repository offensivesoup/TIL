class Father:
    gender = 'xy'
    
    def save(self):
        print(f'{self.name} {self.age}')
        print('DB에 저장')
    
class Child(Father):
    name = ''
    age = 0
    pass

c1 = Child()
print(c1.gender)
c1.save()
c1.name = '자식1의 이름'
c1.age  = 29
c1.save()

c2 = Child()
c2.name = '자식2의 이름'
c2.age = 28
c2.save()

'''
class Article(models.Model):
    title = models.CharField(max_length = 100)
    ...
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.p1 = Point(x1,y1)
        self.p2 = Point(x2,y2)
        
p1 = Point(0,0)
p2 = Point(2,2)
r1 = Rectangle(p1.x, p1.y, p2.x, p2.y)


'''
@login_required ~~
'''
def my_decorator(func):
    def wrapper(*args, **kwagrs):
        print(args)
        print('데코레이터가 하는 일')
        return func(*args, **kwagrs)
    return wrapper        

@my_decorator
def my_function(a,b):
    return a+b

print(my_function(1,3))

def login_required(func):
    def wrapper(*args, **kwargs):
        request, args = args
        if request.user.is_authenticated:
            return view_func(request, args)
        return redirect('accounts:login')
    return wrapper