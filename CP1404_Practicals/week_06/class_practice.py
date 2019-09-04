class Product:
    def __init__(self, product_name="", price=0.0, is_on_sale=False):
        self.product_name = product_name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = "On sale"
        return "{} ${:.2f} {}".format(self.product_name, self.price, on_sale_string)


p = Product("Phone", 340)
print(p)
p2 = Product("PC", 1420.95, True)
print(p2)
