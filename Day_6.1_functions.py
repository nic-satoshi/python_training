shop = [
    {"name": "Apple", "quantity": 30, "price": 0.50},
    {"name": "Banana", "quantity": 20, "price": 0.20},
]


def add_new_product(shop):
    while True:
        name = input("What is the product name? ")
        quantity = int(input("What is the quantity? "))
        price = float(input("What is the price? "))
        shop.append({"name": name, "quantity": quantity, "price": price})
        print(shop)
        if input("Do you add more Y/N? ") == "N":
            break


def showMainMenu():
    print(
        """\
          Main Menu
            1. Add Product
            2. Print all product in shop
            3. Exit"""
    )

    return int(input("What you liked about the training? "))


while True:

    num = showMainMenu()

    if num == 1:
        add_new_product(shop)
    elif num == 2:
        print(shop)
    else:
        print("Bye")
        break
