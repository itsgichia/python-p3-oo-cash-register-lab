class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []  # Holds item names for simplicity
        self.transactions = []  # Keeps track of each transaction as a tuple (price, quantity)

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)  # Add item names, considering quantity
        self.transactions.append((price, quantity))  # Record transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.transactions:
            last_price, last_quantity = self.transactions.pop()
            self.total -= last_price * last_quantity
            # Assume each transaction adds unique items, for simplicity
            for _ in range(last_quantity):
                self.items.pop()  # Remove the last item(s) added
        else:
            self.total = 0  # Reset total if no transactions left
