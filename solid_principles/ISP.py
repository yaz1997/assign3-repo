# from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     @abstractmethod
#     def process_refund(self, amount):
#         pass

# class OnlinePaymentProcessor(PaymentProcessor):
#     def process_payment(self, amount):
#         print(f"Processing payment of ${amount}")

#     def process_refund(self, amount):
#         print(f"Processing refund of ${amount}")


class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("process_payment method not implemented.")

class RefundProcessor:
    def process_refund(self, amount):
        raise NotImplementedError("process_refund method not implemented.")

class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of amount {amount}")

class OnlinePaymentRefundProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of amount {amount}")

    def process_refund(self, amount):
        print(f"Processing refund of amount {amount}")

def main():
    payment_processor = OnlinePaymentProcessor()
    refund_processor = OnlinePaymentRefundProcessor()

    payment_processor.process_payment(1000)
    refund_processor.process_refund(500)

if __name__ == "__main__":
    main()
