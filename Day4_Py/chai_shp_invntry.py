from abc import ABC, abstractmethod

class Chai(ABC):
    def __init__(self, name, base_price, quantity_in_stock):
        self.name = name
        self.base_price = base_price
        self.quantity_in_stock = quantity_in_stock

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def display_info(self):
        
        pass

class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price + 10
    def display_info(self):
        print(f"Name : {self.name} | Price per Cup : ₹{self.calculate_price()} , Stock: {self.quantity_in_stock}")

class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price + 8

    def display_info(self):
        print(f"Name : {self.name} | Price per Cup : ₹{self.calculate_price()} , Stock: {self.quantity_in_stock}")


class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price + 12  

    def display_info(self):
        print(f"Name : {self.name} | Price per Cup : ₹{self.calculate_price()} , Stock: {self.quantity_in_stock}")

class ChaiInventory:
    def __init__(self):
        self.inventory = []

    def add_chai(self, Chai):
        
        self.inventory.append(Chai)

    def show_inventory(self):
       
        for chai in self.inventory:
            chai.display_info()

    def get_total_inventory_value(self):
   
        total_value = sum(Chai.calculate_price() * Chai.quantity_in_stock for Chai in self.inventory)
        return total_value


inventory = ChaiInventory()

chai1 = MasalaChai("Masala Chai", 20, 50)  
chai2 = GingerChai("Ginger Chai", 18, 40) 
chai3 = ElaichiChai("Elaichi Chai", 25, 30)  
inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())
