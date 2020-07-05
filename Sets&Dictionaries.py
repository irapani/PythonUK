
d={}
print(d)
print(type(d))

d1={1:"welcome",2:"to",3:"python",4:"tutorial"}
print(d1)

d2={"name":"sam","age": 22,"profession":"student"}
print(d2)

d3=dict({1:"welcome",2:"to",3:"python",4:"tutorial"})
print(d3)

d5=dict([(1,"welcome"),(2,"to"),(3,"python"),(4,"tutorial")])
print(d5)

# Adding Element

d={}
d[0]="welcome"
print(d)

d[1]=("how","are", "you")
print(d)

d["name"]="sam"
print(d)

d["name"]={"first":"sam","last":"smith"}
print(d)

print(d["name"]["first"])
print(d)

# Deleting elements

d.pop(0)
print(d)

d.popitem() # last elemet
print(d)

# Using buile in function

d.values()
print(d)

# keys={a,b,c,d}
# value=1
# dict.fromkeys(keys,value)
# print(d)

# Sets, unordered collection of unique elemets

s = set([1,2,3,4])
print(s)
print(type(s))

s.add('a')
print(s)

fs=frozenset([1,2,3,4])
print(fs) # cant be added any thing else

s1 = set([1,4,3,2])
s2 = set([3,4,5,2])

s1.union(s2)
print()
