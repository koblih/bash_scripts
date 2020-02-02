
class Cars:

    # available car types are sedan, hatchback and SUV
    cars = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def display_available_cars(self):
        print("These are our available cars:")
        for key, value in  self.cars.items():
            print(key, value)

    def get_price(self, requested_car):
        '''
        get daily price for selected car
        '''
        for key, value in self.cars.items():
            if requested_car == key:
                return value

    def rent_a_car(selif, number_days, price, requested_car):
        '''
        display confirmation and the total price
        '''
        print("You have rented {} car for {} days".format(requested_car, number_days))
        total_price = number_days * price
        print("The total price will be: {}".format(total_price))


class Customer:
    
    def requested_car(self):
        '''
        request a type of car
        '''
        print("Please enter the car you wish to rent:")
        self.selection = input()
        return self.selection

    def request_no_days(self):
        print("Please enter the number of days you wish to rent the car for:")
        self.no_days = int(input())
        return self.no_days


cars = Cars()
customer = Customer()
cars.display_available_cars()
requested_car = customer.requested_car()
price = cars.get_price(requested_car)
number_days = customer.request_no_days()
cars.rent_a_car(number_days, price, requested_car)
