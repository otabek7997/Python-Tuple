orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

even_orders = [order for order in orders if order[0] % 2 == 0]
print(even_orders)