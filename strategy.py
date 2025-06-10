class Payment:
    def pay(self, value: float) -> str:
        raise NotImplementedError("Must be implemented")


class CardPayment(Payment):
    def pay(self, value: float):
        return f"Paying {value} with card..."


class CashPayment(Payment):
    def pay(self, value: float):
        return f"Paying {value} with cash..."


class PaymentRegister:
    def __init__(self, payment: Payment):
        self.payment = payment

    def checkout(self, value: float):
        return self.payment.pay(value)


payment_with_card = PaymentRegister(CardPayment())
assert payment_with_card.checkout(10) == "Paying 10 with card..."


payment_with_cash = PaymentRegister(CashPayment())
assert payment_with_cash.checkout(10) == "Paying 10 with cash..."
