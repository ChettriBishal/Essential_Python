from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paying {amount} using credit card")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paying {amount} using paypal")


class BitcoinPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paying {amount} using bitcoin")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.process_payment(amount)


paypal_payment = PayPalPayment()
payment_processor = PaymentProcessor(paypal_payment)


payment_processor.process_payment(5000)
