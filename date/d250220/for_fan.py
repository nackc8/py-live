fan_orders = [3, 10, 120, 73, 94, 56, 83]
fan_orders_plus_small_order_fee = []

small_order_fee_limit = 50
small_order_fee_percent = 1.2

for banan in fan_orders:
    if banan < small_order_fee_limit:
        banan = banan * small_order_fee_percent
