class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'Blah blah blah u talk ')
i=input("Enter your name: ")
p1=Person(i)

print(p1.name)
p1.talk()

