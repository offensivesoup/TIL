class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('김싸피') # 생성자 함수가 없으면 찾으러 올라간다. => Person까지
print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene) # Dad가 먼저 상속되어 있기 떄문에 XY로 나타난다.