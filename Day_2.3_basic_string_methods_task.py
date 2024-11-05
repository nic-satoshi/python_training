# Task 1.1
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Clue:
# Slice operator

# Expected Output
# "PYTHON-POWERFUL"

secret_message_shaped = secret_message.strip().upper()
print(f"{secret_message_shaped[15:21]}-{secret_message_shaped[34:42]}")


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

message = flipped_message[::-1].lower()
print(f"{message[0:6]} 🗡️  {message[12:20]} 🌸")