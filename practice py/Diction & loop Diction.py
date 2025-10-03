# DICTIONARY 
# 1.KEY VALUE PAIRS
# 2.Curly brackets
# 3.All pairs comma seprated
# syntax: {key : value}

MyDictionary = {"name":"john" , "age":22 , "gender":"Male"}
print(MyDictionary)

#Dictinary Method
FruitsDictionary = {
    "Apple":"Red",
    "Quantity":6, #print one time
    "Flavour":"Juicy",
    "Cherry":"Deep Red",
    "Test":"Soure",
    "Quantity":6 #not print
}
print(FruitsDictionary.keys())
print(FruitsDictionary.values())

veg = {}
veg["lady_finger"] = "vegatables"
veg["potato"] = "1kg"
veg["tomato"] = "is_red"
veg["red"] = 4
print(veg)

# . keys pss hoe list format main
# syntaz:
# . print(var.keys(not argument pss))
print(veg.keys()) 

# . values pss hoe list format main
# syntaz:
# . print(var.values(not argument pss))
print(veg.values()) 

# . how to use items()
# . this is dictionay method.
# . print(var.items(no argument pss))
# . every key value pairs convert to tuple
print(veg.items()) 

# . syntax pop():
# . print(var.pop(key pss))
# . only value mily ga output main
print(veg.pop("potato"))

# . syntax update():
# . var.update({"new_key_pss":new_value_pss"})
# . print(var)
veg.update({"beatroot" : "1/2 kg"})
print(veg)

# Looping Dictionary:
for temp_var in veg:
    print(f"Key = {temp_var}")

for temp_var in veg.values():
    print(f"value = {temp_var}")    

for temp_var in veg.keys():
    print(f"keys = {temp_var}")    

for temp_var in [veg.keys()]:
    print(f"{temp_var}only keys pss but list format main") 
