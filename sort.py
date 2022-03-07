namelist = []
print("enter 5 names")
for i in range(0,5):
    name = input("enter name")
    namelist.append(name)
    namelist.sort()
    print(namelist)