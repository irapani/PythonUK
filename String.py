
stg = "simplilear"
print(stg)
stg = "tim's birthday"
print(stg)
stg = 'tim said , "I\ busy today"'
print(stg)
stg = '''hey there
there i'm'''
print(stg)

stg = "simeplilearn"
print(len(stg))
print(stg[3])

stg  = "Simplilearn"
for i in stg:
    print(i, end="")

#slissing

stg="Simplilearn"
print(stg[0:5])
print(stg[:5])
print(stg[5:])
print(stg[2:5])

stg="welcome to simplilearn"
print(stg.upper())
print(stg.lower())
print(stg.find('i'))
print(stg.index('s'))

print(stg.split(" "))

x=stg.split(" ")
print(x)
print(stg.replace("simplilearn ", "python"))

# returns tuple

print(stg.rpartition(" to "))

stg1="good"
stg2="morning"
stg = stg1 +" " + stg2
print(stg)

stg1="hey"
stg2="there"
stg3="all"
stg="{} {}, {}!".format(stg1,stg2,stg3)
print(stg)
