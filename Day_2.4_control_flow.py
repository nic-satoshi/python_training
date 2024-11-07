# if ... else -> decision making

# person = 1
# if person <= 2:
#    print("We will take a bike")
# else :
#    print("We will take a car")


# Task
# Get two person name
# Case 1:
# Luffy, Zoro
# 173cm, 163cm
# Expected
# Luffy is taller than Zoro by 10cm
# Case 2:
# Luffy, Zoro
# 173cm, 185cm
# Expected
# Zoro is taller than Luffy by 12cm

# get name1's info
# name1 = input("input name1 : ")
# name1_height = float(input(f"input {name1}'s height : "))

# get name2's info
# name2 = input("input name2 : ")
# name2_height = float(input(f"input {name2}'s height : "))


# diff_height = abs(name1_height - name2_height)
# if  name1_height > name2_height:
#     print(f"{name1} is taller than {name2} by {diff_height}cm")
# elif name2_height > name1_height:
#     print(f"{name2} is taller than {name1} by {diff_height}cm")
# else:
#     print(f"{name1} and {name2} are the same height")


# Input
fav_flavour = input("what's your favo flevour?").strip().lower()
# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

# if fav_flavour == stock1:
#     print(f"Yes, we do have {stock1}")
# elif fav_flavour == stock2:
#     print(f"Yes, we do have {stock2}")
# elif fav_flavour == stock3:
#     print(f"Yes, we do have {stock3}")
# elif fav_flavour == stock4:
#     print(f"Yes, we do have {stock4}")
# else:
#     print(f"Sorry, we ran out of {fav_flavour}")

if fav_flavour in [stock1, stock2, stock3, stock4]:
    print(f"Yes, we do have {fav_flavour}")
else:
    print(f"Sorry, we ran out of {fav_flavour}")
# Case 1:
# Yes, we do have vanilla
# Case 2:̥
# "orange"
# Sorry, we ran out of orange
