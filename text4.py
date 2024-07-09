#User Input
Product_ID = float(input("Please enter product ID: "))
Name = input("Please enter name: ")
ProdCost = float(input("Please enter product cost: "))
SellPrice = float(input("Please enter sell price: "))
VAT = float(input("Please enter VAT amount: "))

#Calulations#
vatamount = VAT * ProdCost 
profit = SellPrice - (ProdCost - vatamount)
markup = (profit / ProdCost) * 100

#Requesting the user to specify, what they want
question = input("Would you like to see the. Please choose vatamount, profit, markup or detailed report ")
print(question)

#The program goes through the if statements to check what the user wants
if question == "vatamount":
    print("VAT Amount:R", vatamount)

#Will print profit if requested
elif question == "profit":
    print("Profit:R", profit)

#Will print markup if requested
elif question == "markup":
    print("Markup:R", markup)
    
elif question == "detailed report":
    print(Product_ID)
    print("Name: ",Name)
    print("VAT: ",VAT , "%")
    print("COS: ", ProdCost)
    print("SP:  ",SellPrice)   
    print("VAT Amount:R", vatamount)
    print("Profit:R", profit)
    print("Markup:R", markup)

#If valid option is not selected, the computer will ask he user to choose on of the options
else:
    print("Please choose a valid option")




