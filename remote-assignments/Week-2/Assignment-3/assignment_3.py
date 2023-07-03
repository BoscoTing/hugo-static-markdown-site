def avg(data):
    total_price = 0
    number_of_product = 0
    for products in data['products']:
        total_price += products['price']
        number_of_product += 1
        average_price = total_price / number_of_product
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