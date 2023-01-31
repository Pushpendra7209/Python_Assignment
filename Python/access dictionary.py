thisdict={
    "brand":"sparrky",     
    "modal":"mostand",
    "year":"1964",
    "year":"2020"}
print(thisdict)
print(thisdict["brand"])

print(len(thisdict))

print(type(thisdict))

print(thisdict["modal"])

print(thisdict.get("modal"))

x=thisdict.keys()
print(x)

thisdict["color"]="white"
print(x)

y=thisdict.get("year")
print(y)

z=thisdict.values()
print(z)

thisdict["animal"]="dog"
print(z)

a=thisdict.items()
print(a)

thisdict["name"]="ashu"
print(a)
if "year" in thisdict:
       print("yes modal in thisdict")