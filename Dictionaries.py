#user when you need to use key value pare

# name: uday kumar
# email: uday@gmail.com
# phone: 1234567890

customer ={
    "name": "udaykumar",
    "age": 30,
    "is_verified": True
}

customer["name"]="Kranthi Kumar"
customer["birthdate"] = "jan 5th 2020"

print(customer["name"])
print(customer["age"])
print(customer.get("name"))
print(customer.get("age"))
print(customer.get("birthdate"))

#ex

phone = input("Phone")
digits_mapping = {
"1":"one",
"2": "two",
"3":"three",
"4:": "four"
}
output =""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)