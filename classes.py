#for class we need cap's first letter/ camel case
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
point1 = Point()
point1.x = 10
point1.y = 30
point1.draw()
print(point1.x)
print(point1.y)

point2 = Point()
point2.x = 1
point2.y = 2
print(point2.x)
print(point2.y)