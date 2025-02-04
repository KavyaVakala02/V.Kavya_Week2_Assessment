class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass not implement this method")
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"
class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"
class BitcoinPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Bitcoin payment of {amount} "
# Creating instances of payment type
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
bitcoin_payment = BitcoinPayment()
# Process payments using each payment type
print(credit_card_payment.process_payment(5000))  # Credit card payment of 5000
print(paypal_payment.process_payment(700))      # PayPal payment of 700
print(bitcoin_payment.process_payment(200))   # Bitcoin payment of 200
