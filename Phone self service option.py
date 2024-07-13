def calser():
    # Price of Packages
    premium = 250
    regular = 100

    # Customer Input
    user = input("Please enter your full name ")
    acc= input("Enter account number: ")
    #.lower() allows the user to enter a uppercase or lowercase number
    service = input("Enter service code (R for Regular, P for Premium): ").lower()

    #If regular service is chosen
    if service == 'r':
        print("Regular Service")
        day = float(input("Enter number of minutes used during the day: "))
        print(day)
        
        total = regular + (day *2)
        #If minusted used is less that 50, then no charge
        if day <=50:
            print("no charge")
        
        #If charge is more than or equal to 50 mins, calculation takes place
        elif day >= 50:
            print("Name", user)
            print("account number", acc)
            print("type of service: regular")
            print("R", total)
        
        # If no valid option is given, computer will prompt the user
        else:
            print("Please enter a valid number")
        

    # If premium service is chosen
    elif service == 'p':
        print("Premium Service")
        day = float(input("Enter number of minutes used between 6am tp 6pm: "))
        night = float(input("Enter number of minutes used 6pm tp 6am:: "))
    
        #Calculations, if user exceed his limit
        totalday = (day * 1)
        totalnyt = (night * 0.5)

        total =  premium + (totalday + totalnyt)
    
        #If minusted used is less that or equal to 75, then no charge
        if day <=75:
            print("No Charge")

        #If minusted used is more that 75, then no charge
        elif day >= 75:
            print("Name", user)
            print("account number", acc)
            print("type of service: premium")
            print("R", total)
        
        #If minusted used is less that or equal to 100, then no charge
        elif night <=100:
            print("No charge")
        
        #If minusted used is more than 100, then no charge
        elif night >=100:
            print("Name", user)
            print("account number", acc)
            print("type of service", service)
            print("R", total)

        else:
            print("Please enter a valid number")

        


    else:
        print("Invalid service code. Please enter 'R' for Regular or 'P' for Premium.")

# Execute the function
calser()