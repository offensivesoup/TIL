class Person:
    # 속성
    blood_color = "red"

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다'

# 인스턴스 생성
    
singer1 = Person('iu')
singer2 = Person('bts')

# 메서드 호출

print(singer1.singing())
print(singer2.singing())

print(singer1.blood_color)
print(singer2.blood_color)