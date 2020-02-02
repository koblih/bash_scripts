
class Cars:

    '''
    at the start of the program display all car types with numbers
    and ask customer to select one
    '''
    # available car types are sedan, hatchback and SUV
    available_cars = ['Hatchback', 'Sedan', 'SUV']
    car_prices = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def display_available_cars(self):
        print("These are our available cars:")
        for car in self.available_cars:
            print(car)

    def display_price(self, requested_car):
        '''
        after the car is selected display the price per day
        and ask for number of days
        '''
        for key in self.car_prices:
            if requested_car == key:
                print("The price per day is: {}".format(self.car_prices[key]))
                break
            else:
                print("Please try again")
                continue

    def rent_a_car(selif, number_days):
        '''
        display confirmation and the total price
        '''
        print("You have rented ### car for {} days".format(number_days)) #add name of the car
        


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
        self.no_days = input()
        return self.no_days


cars = Cars()
customer = Customer()
cars.display_available_cars()
requested_car = customer.requested_car()
cars.display_price(requested_car)
number_days = customer.request_no_days()
cars.rent_a_car(number_days)
