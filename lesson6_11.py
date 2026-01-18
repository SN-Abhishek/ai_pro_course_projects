class Dog:
    # This is the constructor method.
    # It runs automatically whenever a new Dog object is created.
    def __init__(self, name, breed):
        print(f"A new dog named {name} was just created!")

# These are the attributes. We are attaching the data to the specific object (self).
        self.name = name
        self.breed = breed 

    def __init__(self, name, breed):
        # ... (same as before) ...
        print(f"A new dog named {name} was just created!")
        self.name = name
        self.breed = breed

    # This is a method. It's a function that belongs to the Dog class.
    def bark(self):
        # We use self.name to access this specific dog's name
        print(f"{self.name} says: Woof!")



# Here, we are "instantiating" the Dog class to create a Dog object.
fido = Dog("Fido", "Golden Retriever") 


rover = Dog("Rover", "German Shepherd") 

# Call the bark() method on each object
fido.bark()
rover.bark()

