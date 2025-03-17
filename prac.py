class Car:
    # Think of the __init__ function as the class Constructor.
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color

    # Dunder method returns the license plate, model and color
    # whenever we print an instance of the class to the console
    def __repr__(self):
        return f'{self.license_plate}, {self.model}, {self.color}'



c=Car("123",2022,"green")

print(c)