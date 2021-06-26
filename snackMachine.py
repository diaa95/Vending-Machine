import time
accepted_coins= [0.10, 0.20, 0.50, 1.00, 20.00, 50.0]
password = 12345678

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def add_quantity(self, quantity):
        self.quantity += quantity


class VendingMachine:
    def __init__(self, items):
        self.items = items
        self.money_inserted = 0.00

    def display_items(self):
        """
        this method displays all the products with their prices and availability status
        """
        print(" *********************************************")
        print("     WELCOME TO THE VENDING MACHINE           ")
        print(" *********************************************")
        print("                 Products:                    ")
        for code, item in enumerate(self.items, start=1):
            if item.quantity > 0:
                print(f"[{code}] - {item.name} (${item.price:.2f}) status: available")
            else:
                print(f"[{code}] - {item.name} (${item.price:.2f}) status: not available")


    def insert_money(self, money):
        """
        this method validates the inserted moeny and accepts it if valid
        """
        if money not in accepted_coins:
            print("only accepts: ")
            for coin in accepted_coins:
                print(f"${coin}")
            raise ValueError
        self.money_inserted += money
        # print(f"You've inserted ${self.money_inserted:.2f} into the machine so far. price is ${item.price:.2f}")


    def insert_card(self, item, card_number):
        """
        implement card validation process here
        assuming that the card passed the validation process
        """
        print(f"your card is valid! please confirm transaction of ${item.price:.2f}\n 1)confirm\n 2)reject")


    def card_transation(self, amount):
        """
        this method excutes the card transaction process
        """
        self.money_inserted += amount
        print(f"Transaction of ${self.money_inserted:.2f} has been succesfully made !")


    def dispense_item(self, item):
        """
        dispenses the selected item to customer and displays the change at panel
        """
        item.quantity -= 1
        print(f"Thank you! Please take your \"{item.name}\".")
        self.money_inserted -= item.price


    def dispense_change(self):
        """
        this method dispenses the customer's change
        """
        print(f"The remaining change in the machine is ${self.money_inserted}.")
        if self.money_inserted > 0:
            print(f"Thank you! Please take your change \"{self.money_inserted}\".")
            self.money_inserted = 0

    def controll(self):
        print("Choose required operation:\n 1) add item \n 2) add quantity\n 3) delete item")
        selection = int(input("Please enter the desired item code: "))
        if selection == 1:
            name = str(input("Please enter the item's name: "))
            price = float(input("Please enter the item's price: "))
            quantity = int(input("please enter the inserted quantity: "))
            self.add_item(name, price, quantity)
        if selection == 2:
            self.display_items()
            user_selection = int(input("Please enter the desired item code: "))
            if user_selection in range(1, len(self.items)+1):
                item = self.items[user_selection-1]
                quantity = int(input("please enter the added quantity: "))
                item.add_quantity(quantity)
                print(f"{item.name} new quantity is {item.quantity}")
        if selection == 3:
            self.display_items()
            user_selection = int(input("Please enter the desired item code: "))
            if user_selection in range(1, len(self.items)+1):
                item = self.items[user_selection-1]


    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        lst = self.items
        lst.append(item)

    def delete_item(self, item):
        lst = self.items
        lst.remove(item)


def main():
    vending_machine = VendingMachine([Item("Sneakers Bar", 2.00, 4), Item("Mars Bar", 3.00, 5)])

    while True:
        vending_machine.display_items()

        while True:
            try:
                user_selection = int(input("Please enter the desired item code: "))
            except ValueError:
                continue
            if user_selection in range(1, len(vending_machine.items)+1):
                if vending_machine.items[user_selection-1].quantity > 0:
                    item = vending_machine.items[user_selection-1]
                    print(f"You've selected \"{item.name}\" - the price is ${item.price:.2f}")
                    break
                else:
                    print("Sorry !!the required item is not available at the moment!")

            if user_selection == password:
                user_selection = None
                vending_machine.controll()
                item = vending_machine.items[len(vending_machine.items)-1]
                break

        while vending_machine.money_inserted < item.price and user_selection:
            print("payment methods: \n 1) credit card \n 2) cash")
            payment_method = int(input("Please choose your payment method: "))
            if payment_method == 1:
                card_number = int(input("Please insert your card number: "))
                vending_machine.insert_card(item, card_number)
                confirmation = int(input("Please choose your confirmation status: "))
                if confirmation == 1:
                    vending_machine.card_transation(item.price)
                    vending_machine.dispense_item(item)
                    user_selection = None
                    break
                else:
                    print("transaction has been rejected!")
                    break
                
            if payment_method == 2:
                while True:
                    try:
                        money_to_insert = float(input("Please enter the amount of money you'd like to insert: "))
                        vending_machine.insert_money(money_to_insert, item)
                    except ValueError:
                        continue
                    if vending_machine.money_inserted >= item.price:
                        vending_machine.dispense_item(item)
                        vending_machine.dispense_change()
                        user_selection = None
                        break
            else:
                continue
        time.sleep(2)


if __name__ == "__main__":
    import sys
    sys.exit(main())