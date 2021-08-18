s=input()
d={"o":0,"l":1,"z":2,"e":3,"a":4,"s":5,"g":6,"t":7,"b":8,"q":9}
j=""
for i in s:
    if i.lower() in d:
        j+=(str(d[i.lower()]))
    else:
        j+=(str(i))
print(j)
        