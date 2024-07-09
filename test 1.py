#Dimensions of the roof, body and floor
roof = 7
body = 6
floor = 13

# Printing the roof
for i in range(roof):
    # Printing spaces
    for j in range(roof - i - 1):
            print(" ", end="")
    # Print asterisks
    for j in range(2 * i + 1):
        print("*", end="")
        
    print()

    # Printing the body
for i in range(body):
    print("*           *")

    # Printing the floor
for i in range(floor):
    print("*", end="")
print()



