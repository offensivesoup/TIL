class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.name = 'kim'

p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)

p2.ssafy = 11
print(p2.ssafy)

class Circle():
    pi = 3.14
    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

c2.pi = 5

print(Circle.pi)
print(c1.pi)
print(c2.pi)        

class MyClass:

    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'

# 클래스가 전부다 호출해보기   
    # 전부다 동작은 한다. => 문법적으로 봤을때, 틀린게 없다. 
instance = MyClass()
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())

# 인스턴스가 전부다 호출해보기

instance = MyClass()
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())

