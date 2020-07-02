# # class Point:
# #     def __int__(self, x, y):  # initallizing
# #         self.x = x
# #         self.y = y
# #
# #     def move(self):
# #         print("move")
# #
# #     def draw(self):
# #         print("draw")
# #
# #
# # point = Point(10, 20)
# # point.x = 12
# # print(point.x)
#
# class Computer:
#     def __int__(self):
#         self.name = "uk"
#         self.age = 30
#
# c1 = Computer()
# c2 = Computer()
#
# print(c1.name)
# print(c2.name)
#
# # c1 = Computer()
# # c2 = Computer()
# #
# # # c1.name = "su"
# #
# # print(c1.name)
# # print(c2.name)
# # c1 = Computer()
# # c2 = Computer()
# #
# # c1.name = "su"
# # # c2.age = 28
# #
# # print(id(c1.name))
# # print(id(c2.name))
#
# class Computer:
#
#     def __int__(self):
#         self.name = "uk"
#         self.age = 30
#
# c1 = Computer()
# c2 = Computer()
#
# print(c1.name)
# print(c2.name)

# class GeekforGeeks:
#
#     def __int__(self):
#         self.geek = "GeekforGeeks"
#
#     def print_Geek(self):
#         print(self.geek)
#
# obj = GeekforGeeks()
#
# obj.print_Geek()


# class Employee:
#     def __int__(self,name, id):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print("ID: %d \nName: %s" %(self.id, self.name))
#
# emp1 = Employee("John",101)
# emp2 = Employee("David",102)
#
# emp1.display()
# emp2.display()

# class Person:
#
#     def __int__(self):
#         self.name="sam"
#         self.gender="M"
#         self.age=22
#
#     def talk(self):
#         print("Hi I'm ", self.name)
#
#     def vote(self):
#         if self.age < 18 :
#             print("i'm not eligible to vote")
#         else:
#             print("I can vote")
#
#
#     object = person()
#     Person.talk(object)
#     Person.vote(object)

class DemoClass:
    def __int__(self):
        self.num=1000

    def read_number(self):
        print(self.num)


obj = DemoClass()
obj.read_number()
