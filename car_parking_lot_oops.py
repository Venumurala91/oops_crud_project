# Defining the Car class
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


class Garage:
    # Class Constructor with four attributes
    def __init__(self):
        self.cars_added = []
        self.spots = 20
        self.car_info = {}
        self.bill = 0
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1',
                           'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1',
                           'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']

    # This function returns the number of spots available
    def spots_available(self):
        return self.spots

    # The add_car function adds a car to the parking lot
    def add_car(self, car):
        # Here we check if we have any spots available
        if self.spots > 0:
            # Create a list of the car details and add to cars_added
            self.cars_added.append(str(car).split(', '))

            # Subtract one from spots as we have one less spot available
            self.spots -= 1

            # Update the car_info dictionary with the new car details
            if 'code' not in self.car_info:
                self.car_info = {'code': [], 'license plate': [], 'Model': [], 'Color': []}

            for index, car_info in enumerate(self.cars_added):
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license plate'].append(car_info[0])
                self.car_info['Model'].append(car_info[1])
                self.car_info['Color'].append(car_info[2])

            return "Car successfully added to the parking lot"
        else:
            return f"We have {self.spots} spots available. I am sorry, the parking lot is full."

    # This function removes the car from the parking lot
    def remove_car(self, given_code, bill_hours):
        # Here we check how many codes we have in the car_info dict
        past_len = len(self.car_info['code'])

        # If the given code is not in our dictionary
        if given_code not in self.car_info['code']:
            return "We could not find your car. Are you sure you parked your car here?"

        # If the code is found in the dictionary, loop through the codes
        for index, value in enumerate(self.car_info['code']):
            if value == given_code:
                # Print car information
                print("Your car's license plate is:", self.car_info['license plate'][index])
                print("Your car's model is:", self.car_info['Model'][index])
                print("Your car's color is:", self.car_info['Color'][index])

                # Remove car details from car_info dictionary
                self.car_info['code'].pop(index)
                self.car_info['license plate'].pop(index)
                self.car_info['Model'].pop(index)
                self.car_info['Color'].pop(index)

                # Increase spots as car is removed
                self.spots += 1

                # Calculate the bill based on parked hours
                while True:
                    if bill_hours.isnumeric():
                        # Bill calculation logic
                        bill_hours = int(bill_hours)
                        if bill_hours < 20:
                            self.bill = bill_hours * 5
                            return f'Your total bill is ${self.bill}'
                        else:
                            self.bill = bill_hours * 5 + 100  # Additional fine for exceeding 20 hours
                            return f'Your total bill is ${self.bill}'
                    else:
                        bill_hours = input("Your input must be an integer. Example input: 5 --> ")
                        if bill_hours in ['q', 'Q']:
                            break
        return ""

    # Displays all cars in garage
    def cars_in_garage(self):
        for i in range(len(self.car_info['code'])):
            print(f"Code: {self.car_info['code'][i]}, License Plate: {self.car_info['license plate'][i]}, "
                  f"Model: {self.car_info['Model'][i]}, Color: {self.car_info['Color'][i]}")


# Creating instances of each class
my_garage = Garage()

# Printing available spots
print(my_garage.spots_available())

# Adding cars to the garage
my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
my_garage.add_car(Car('LVG34', 'Optra', 'Red'))


# Displaying cars in garage
my_garage.cars_in_garage()

# Removing a car and calculating the bill
print(my_garage.remove_car('A1', '10'))

# Printing available spots after removal
print(my_garage.spots_available())

