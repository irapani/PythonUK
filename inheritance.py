
class Mammal:
    def walk(self):
        print("walk")

    def bark(self):
        print("bark")

class Dog(Mammal):
        # def walk(self):
        #     print("walk")
        pass


class Cat(Mammal):
    def be_slow(self):
        print("slow")
    pass

dog1 = Dog()
dog1.walk()

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.be_slow()

