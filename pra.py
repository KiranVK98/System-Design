class IceCreamFlavor:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Topping:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Inventory:
    def __init__(self):
        self.flavors = []
        self.toppings = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)


    def get_flavor(self):
        for item in self.flavors:
            print(item.name, item.price, item.quantity)

    def add_topping(self, topping):
        self.toppings.append(topping)

    def update_inventory(self, item_name):
        for item in self.flavors + self.toppings:
            if item.name == item_name:
                item.quantity -= 1
                break

    def check_inventory(self, item_name):
        for item in self.flavors + self.toppings:
            if item.name == item_name:
                return item.quantity
        return 0

# Sample usage:
inventory = Inventory()

# Add flavors to inventory
vanilla = IceCreamFlavor("Vanilla", 2.0, 10)
chocolate = IceCreamFlavor("Chocolate", 2.5, 10)
inventory.add_flavor(vanilla)
inventory.add_flavor(chocolate)

print(inventory.get_flavor())

# Add toppings to inventory
# sprinkles = Topping("Sprinkles", 0.5, 20)
# chocolate_chips = Topping("Chocolate Chips", 0.75, 15)
# inventory.add_topping(sprinkles)
# inventory.add_topping(chocolate_chips)

# # Create an order
# order = Order()

# # Add items to the order
# order.add_item(vanilla)
# order.add_item(sprinkles)
# order.add_item(chocolate)

# # Calculate total
# total_cost = order.calculate_total()
# print("Total cost:", total_cost)

# # Update inventory after order
# for item in order.items:
#     inventory.update_inventory(item.name)

# # Check inventory after order
# print("Vanilla remaining:", inventory.check_inventory("Vanilla"))
# print("Sprinkles remaining:", inventory.check_inventory("Sprinkles"))
