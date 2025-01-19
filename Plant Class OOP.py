# Question A, create plant class with name, biome and height attributes
class Plant:
    def __init__(self, name, biome, height):
        self.name = name
        self.biome = biome
        self.height = height

    #decribe method in place
    def describe(self):
        print(f"The Plant Name: {self.name}")
        print(f"The type of Biome is: {self.biome}")
        print(f"The Height is: {self.height} meters")

    def __str__(self):
        return(f"{self.name} ({self.biome})")


# Question B
# FloweringPlant class is created and inherits Plants Class
class FloweringPlant(Plant):
    def __init__(self, name, biome, height, flowercol):
        super().__init__(name, biome, height)
        self.flowercol = flowercol

    def describe(self):
        print(f"The Plant Name: {self.name}")
        print(f"The type of Biome is: {self.biome}")
        print(f"The Height of the plant is: {self.height} meters")
        print(f"The Flower Color is: {self.flowercol}")


# Question C
# Tree class is created and inherits from Plant class 
class Tree(Plant):
    def __init__(self, name, biome, height, age, leaft):
        super().__init__(name, biome, height)
        self.age = age
        self.leaft = leaft

    def describe(self):
        print(f"The Plant Name: {self.name}")
        print(f"The Biome: {self.biome}")
        print(f"The Height of the plant: {self.height} meters")
        print(f"The Age of the tree is: {self.age} years")
        print(f"The Leaf Type is: {self.leaft}")

    # Method checks if tree is older than 100 years
    def is_old(self):
        print(self.age > 100)


# Printing the classes
if __name__ == "__main__":
    # Prints the Plant Class
    plant = Plant("Water Tree", "Desert", 2)
    print(plant)
    plant.describe()
    print()

    # Prints the Flowering Plant class
    marigold = FloweringPlant("Marigold", "Grassland", 1.5, "Orange")
    print(marigold)
    marigold.describe()
    
    

    # Print Tree class
    Baobab_tree = Tree("Baobab", "Savannah", 200, "Evergreen")
    print(Baobab_tree)
    Baobab_tree.describe()
    print(f"The Baobab tree is over 200 years old")
