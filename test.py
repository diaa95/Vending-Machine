import unittest
from snackMachine import VendingMachine, Item
# from mock import Mock

class snackMachineTest(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine([Item("Sneakers Bar", 2.00, 4), Item("Mars Bar", 3.00, 5)])
        self.itemTest = Item("Doretos", 4.00, 0)

    def test_add_quantity(self):
        self.itemTest.add_quantity(3)
        self.assertEqual(3, self.itemTest.quantity, "Test item quantity should become 3")

    def test_add_item(self):
        self.machine.add_item("Doretos", 4.00, 5)
        self.assertEqual(3, len(self.machine.items), "Machine should have three items")

    def test_delete_item(self):
        self.machine.delete_item(self.machine.items[0])
        self.assertEqual(1, len(self.machine.items), "Machine should contain one item after deletin the first Item")

    def test_insert_money(self):
        self.machine.insert_money(1.0)
        self.machine.insert_money(0.5)
        self.assertEqual(1.5, self.machine.money_inserted, "inserted money should be $2.0")

    def test_dispense_change(self):
        self.machine.dispense_change()
        self.assertEqual(0.0, self.machine.money_inserted, "inserted money should be $0.0 after dispensing change")

    def test_dispense_item(self):
        item = self.machine.items[0]
        self.machine.dispense_item(item)
        self.assertEqual(3, item.quantity, "quantity of Sneakers Bar should be 3 after dispensing 1")

    # def test_isert

if __name__ == '__main__':
    unittest.main()