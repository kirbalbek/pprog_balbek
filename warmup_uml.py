#1 задача
'''
class Shape:
    def __init__(self, side, height):
        self.side = side
        self.height = height


class Triangle(Shape):
    def area(self):
        return self.side*self.height/2


class Rectangle(Shape):
    def area(self):
        return self.side*self.height


a = int(input())
b = int(input())
d = Triangle(a, b)
ans = d.area()
print(ans)
'''

#2 задача
'''
class Mother:
    def print(self):
        print(self.voice())
    def voice(self):
        return "я мама"


class Daughter(Mother):
    def voice(self):
        return "я не мама, я дочка"


a = Daughter()
a.print()
'''
#3 задача
'''
class Animal:
    def __init__(self,name):
        self.name=name
        print("возвращаю я животное")


class Zebra(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        print("возвращаю я зёбра")
        print("возвращаю мне " + age +" лет")
        print("я зёбра "  + name )



class Hryusha(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        print("возвращаю я хрюша")
        print("возвращаю мне " + age +" лет")
        print("я хрюша "  + name )
        print("Верните Массимо!!! Вернулись, чтобы править!")


na = "vasya"
ag  = "18"
d = Zebra(na, ag)
print()
print()

p = Hryusha(na, ag)
'''
