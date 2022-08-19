class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')

p1.say_hi()
p2.say_hi()
p3.say_hi()
