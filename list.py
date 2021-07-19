

friends = ["Uday","kumar","Irapani", "kranthi","kumar","Irapani"]
friends.insert(2,"rao")
friends.remove("kranthi")
lucky_numbers = [2,8,4,6,5,7]
friends.extend(lucky_numbers)
friends.append("jaya")
friends[0] = "kranthi"

for x in friends:
    print(x)

print (friends)
print (friends.count("kumar"))


fruits = ["Apple", "Mango", "Banana", "Cherry"]
print(fruits)

fruits[1] = "lychee"


for item in fruits:
    print(item)

color = []
color.append("red")
color.append("green")
color.append("pink")
color.append("Yellow")
color.insert(1,'Black')
#for color in color:
print(color)


color = ["red", "green", "blue", "Black", "Yellow"]
print(" the length of the list is ", len(color))

