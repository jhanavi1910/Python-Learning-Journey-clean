class Payment:
    def pay(self):
        print("Making payment")


class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")


class Card(Payment):
    def pay(self):
        print("Payment made using Card")


class Cash(Payment):
    def pay(self):
        print("Payment made using Cash")


payments = [UPI(), Card(), Cash()]

for payment in payments:
    payment.pay()