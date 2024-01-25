class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.p1 = x.x - y.x
        self.p2 = y.y - x.y

    def get_area(self):
        return abs(self.p1 * self.p2)
    
    def get_perimeter(self):
        if self.p1 == 0 or self.p2 == 0:
            return '일직선상에 있습니다.'
        else:
            return (abs(self.p1) + abs(self.p2)) * 2


    def is_square(self):
        if abs(self.p1) == abs(self.p2):
            return True
        else:
            return False

p1 = Point(-1,3)
p2 = Point(-1,1)

test = Rectangle(p1,p2)


print(test.get_area())
print(test.get_perimeter())
print(test.is_square())