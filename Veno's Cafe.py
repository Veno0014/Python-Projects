name = input("What is your name? ")

if name == "Veno":
    mood_status = input("Are you evil?")
    if mood_status == "Yes":
        print("You are not welcomed here")
        exit()

else:
    print("Welcome to Veno's," + name)

menu = ("chesse cake, chesse toast, cake, pizza, burger and chips")

print("What would like to order from the menu" + menu)

order = input("please input order here ")

amount = float(input ("How much would you like? "))

#Price

if "Chesse Cake":
    price = 24.99
elif "cheese cake":
    price = 24.99

elif "Cheese Toast":
    price = 9.99
elif "chesse toast":
    price = 9.99

elif "Cake":
    price = 29.99
elif "cake":
    price = 29.99

elif "Pizza":
    price = 39.99
elif "pizza":
    price = 39.99 

elif "Burger and Chips":
    price = 49.99
elif " burger and chips":
    price = 49.99

elif "Sorry we dont serve that item here. Please choose an item from the menu":
    print("We dont serve this item here. Please choose an item from the menu")

cost = (price * amount)
print("Thank you for your support your total is R" + str(cost))
