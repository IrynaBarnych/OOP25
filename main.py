class Animal:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def breath(self):
        print("дихає")
    def move(self):
        print("бігає")
class Dog(Animal):
    def voice(self):
        print("Гавкає!")
class Cat(Animal):
            ...
# Створення екземпляра класу "Собака"
my_bird = Animal("Вуді", 70, "синьо-білий", 120)
print(my_bird.name)
bobik = Dog("Бобініо", 3, "красівий", 60000)
murchik = Cat("Мурчелло", 10, "срібний табі", 3700)
print(murchik.color)#атрибут об'єкта
bobik.weight = 42000
bobik.height = 60
print(bobik.height)
print(bobik.weight)
# #методи
bobik.breath()
bobik.voice()
murchik.move()