fan_orders = [3, 10, 120, 73, 94, 56, 83]
fan_orders_plus_small_order_fee = []

small_order_fee_limit = 50
small_order_fee_percent = 1.2

for order in fan_orders:
    if order < small_order_fee_limit:
        order = order * small_order_fee_percent
        fan_orders_plus_small_order_fee.append(order)
