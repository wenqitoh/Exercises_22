"""Practice exercise - Bus Company
create a Class to store info for a bus company, store: bus number,
bus route key, bus driver. Create 3 buses & print info
By Wen Qi Toh
17/2/22"""


class Bus:
    def __init__(self, number, route_key, driver):
        self.number = number
        self.route_key = route_key
        self.driver = driver


    def print_details(self):
        print(f"The bus {self.number}")
