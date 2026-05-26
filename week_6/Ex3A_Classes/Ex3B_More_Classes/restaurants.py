class Restaurant:
    '''This class stores restaurant information and displays simple restaurant messages.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


rest1 = Restaurant("Giordano's", "pizza")
rest2 = Restaurant("Portillo's", "hot dogs")
rest3 = Restaurant("Taco Bell", "Mexican food")

rest1.describe_rest()
rest1.rest_open()

print()

rest2.describe_rest()
rest2.rest_open()

print()

rest3.describe_rest()
rest3.rest_open()