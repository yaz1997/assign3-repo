from abc import abstractmethod

class Product:
    def __init__(self, price):
        self.price = price
    @abstractmethod
    def calculate_price(self):
        pass



class discountedProduct(Product):
    def __init__(self, price,discount):
        super().__init__(price)
        self.discount=discount
    def calculate_price(self):
        discounted_price = self.price - (self.price * self.discount)
        return (discounted_price)
    

class regularProduct(Product):
    def calculate_price(self):
        return (self.price)


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

products = [
        regularProduct(100),
        discountedProduct(200, 0.2),
        regularProduct(50)
    ]

total_price = calculate_total_price(products)
print(f"Total Price: {total_price}")