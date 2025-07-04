from typing import List, Tuple

def filter_orders(orders: List[Tuple]) -> List[Tuple]:
    result = list()
    for order in orders:
        if order[0] % 2 == 0:
            result.append(order)
    return result        

orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
even_orders = filter_orders(orders)
print(even_orders)