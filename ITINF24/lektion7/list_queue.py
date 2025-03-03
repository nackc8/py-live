# listor som en kö

# I utvecklingstermer benäms en
# en kö ofta som: FIFO (first in first out)

customer_queue = []

customer_queue.append("Mayank")
customer_queue.append("Prathiba")

served = customer_queue.pop(0)
print(f"{served} Det blir ... kr")
served = customer_queue.pop(0)
print(f"{served} Det blir ... kr")
