# List of plant height in meters
plant = [0.25, 0.5, 0.75, 1, 2, 3 , 4, 5]

def plants_height(heights):
    # Checks if the list has 5 more elements
    if len(heights) < 5:
        print("The list need 5 plant heights")
    
    else:
        #Checks for heights taller than 1m and prints new list
        heights = list(filter(lambda heights:  heights > 1, heights))
        print(heights)

#Executes function
anser = plants_height(plant)
print("The heights of the plants taller than 1m:", anser)
