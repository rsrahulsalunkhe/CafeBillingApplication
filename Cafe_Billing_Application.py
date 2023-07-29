class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity


class CafeBillingApplication:
    def __init__(self):
        self.menu = []
        self.current_order = []

    def add_menu_item(self, name, price):
        menu_item = MenuItem(name, price)
        self.menu.append(menu_item)

    def display_menu(self):
        print("Menu:")
        for idx, item in enumerate(self.menu, start=1):
            print(f"{idx}. {item.name} - ${item.price}")

    def take_order(self):
        menu_index = int(input("Enter the menu item number : "))
        quantity = int(input("Enter the quantity : "))

        if 1 <= menu_index <= len(self.menu):
            menu_item = self.menu[menu_index - 1]
            order_item = OrderItem(menu_item, quantity)
            self.current_order.append(order_item)
            print(f"Added {quantity} {menu_index}(s) to the order.")
        else:
            print("Invalid menu item.")

    def calculate_bill(self):
        total = 0
        for order_item in self.current_order:
            total += order_item.menu_item.price * order_item.quantity

        return total

    def apply_discount(self, discount_percentage):
        bill = self.calculate_bill()
        discount_amount = bill * (discount_percentage / 100)
        return bill - discount_amount

    def apply_tax(self, tax_percentage):
        bill = self.calculate_bill()
        tax_amount = bill * (tax_percentage / 100)
        return bill - tax_amount

    def apply_service_charge(self, service_charge_percentage):
        bill = self.calculate_bill()
        service_charge_amount = bill * (service_charge_percentage / 100)
        return bill + service_charge_amount


cafe = CafeBillingApplication()
cafe.add_menu_item("Coffee", 3.5)
cafe.add_menu_item("Sandwich", 5.0)
cafe.add_menu_item("Cake", 4.0)
cafe.add_menu_item("Tea", 2.8)
cafe.display_menu()

# Take order
order_finished = False
while not order_finished:
    cafe.take_order()
    finish_order = input("Would you like to add more items to the order?")
    if finish_order.upper() == "N":
        order_finished = True

# Calculate bill
bill = cafe.calculate_bill()
print("Bill : ", bill)

# Apply discount
discount_percentage = float(input("Enter the discount percentage : "))
discount_bill = cafe.apply_discount(discount_percentage)
print("Discounted bill : ", discount_bill)

# Apply tax
tax_percentage = float(input("Enter the tax percentage : "))
bill_with_tax = cafe.apply_tax(tax_percentage)
print("Bill with Tax : ", bill_with_tax)

# Apply service charge
service_charge_percentage = float(input("Enter the service charge percentage : "))
bill_with_service_charge = cafe.apply_service_charge(service_charge_percentage)
print("Bill with Service Charge : ", bill_with_service_charge)
