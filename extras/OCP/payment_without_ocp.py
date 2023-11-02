class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        if payment_method == "credit_card":
            print(f"Paying {amount} using credit card")
        elif payment_method == "paypal":
            print(f"Paying {amount} using paypal")
        elif payment_method == "bitcoin":
            print(f"Paying {amount} using bitcoin")


pay_amount = PaymentProcessor()
pay_amount.process_payment("paypal", 3000)
