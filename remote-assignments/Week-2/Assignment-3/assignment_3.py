def avg(data):
    total_price = 0
    number_of_products = 0
    for product in data['products']:
        total_price += product['price']
        number_of_products += 1
        average_price = total_price / number_of_products
    return average_price

print(
    avg({
        "products": [
            {
                "name": "Product 1",
                "price": 100
            },
            {
                "name": "Product 2",
                "price": 700
            },
            {
                "name": "Product 2",
                "price": 700
            }
        ]
    })
) # print the average price of all products (round to 3 decimal)
