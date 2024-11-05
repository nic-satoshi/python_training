# pi = 3.14
# radius = float(input(
# "Please tell me the radius of the circle? "))
# print(f"Area of the cirlce : {pi*radius**2}")

# Task 2.1: With f-string
# Fahrenheit to Celcius
# Please provide your Fahrenheit: 98.6
# The 98.6°F is 37°C
# °C = (°F - 32) × 5/9

fahrenheit = float(input(
  "Please provide your Fahrenheit: "))
celcius = round((fahrenheit-32)*5/9)
print(f"The {fahrenheit}°F is {celcius}°C")