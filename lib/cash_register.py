class CashRegister:
    
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0
        self.discount = discount

    def add_item(self, item_name, price, quantity=1):
        transaction_value = float(price * quantity)
        self.total += transaction_value

        for _ in range(quantity):
            self.items.append(item_name)

        self.last_transaction = transaction_value

    def apply_discount(self):
         if self.discount > 0:
              multiplier = 1.0 - (self.discount / 100.0)
              self.total *= multiplier
              print(f"After the discount, the total comes to ${int(self.total)}.")
         else:
              print("There is no discount to apply.")

       

    def void_last_transaction(self):    
        self.total -= self.last_transaction
        self.last_transaction = 0.0