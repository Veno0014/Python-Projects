def read_data(filename):
    #To write on the file#
    with open(filename, "w") as file:
        line = file.readLine()
        
        for line:
            name, surname, qualifcation = line.strip().split(',')
            print("Name: {name}, Surname: {surname}, Qualifications: {qualification}")
            line = file.readLine()
filename = "datatxt"
read_data(filename)

def read_data(filename):
    #Read the file#
    with open(filename, "r") as file:
        line = file.readline()
        #replaced for loop with while because execution count is unknown#
        #The indentation was incorrect bc a different loop was used#
        while line:
            name, surname, qualification = line.strip().split(',')
            #the f-string is included to add more clarity#
            print(f"Name: {name}, Surname: {surname}, Qualifications: {qualification}")
            line = file.readline()

filename = "data.txt"
read_data(filename)