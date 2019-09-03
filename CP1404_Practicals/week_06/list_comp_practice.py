products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = [sale for sale in products if True in sale]
print(on_sale_products)
