# Loops
# repeating statments

# print("Yoshiki")
# print("Yoshiki")
# print("Yoshiki")

# i = 1
# while i <= 10:
#     print("Yoshiki")
#     i = i + 1


# Task - 1
# Expected output
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥

# i = 1
# no_of_rows = int(input("input number : "))
# pattern = input("input puttern : ")
# while i <= no_of_rows:
#     print(f"{"  "*(no_of_rows-i)}{pattern*(i*2-1)}")
#     i = i + 1


# no_of_rows = int(input("input number : "))
# pattern = input("input puttern : ")

# i = no_of_rows
# while i != 0:
#     print(f"{"  "*(no_of_rows-i)}{pattern*(i*2-1)}")
#     i = i - 1


# Task 1.2 - Convert below to for loop

# i = 1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# while i <= rows:
#     print(pattern * i)
#     i = i + 1

no_of_rows = int(input("input number : "))
pattern = input("input the pattern : ")
for i in range(1, no_of_rows + 1):
    print(f"{pattern*i}")
