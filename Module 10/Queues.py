from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.busy = bool


class Cafe:
    def __init__(self, tables_):
        self.queue = 0
        self.tables = tables_

    def customer_arrival(self):
        pass

    def serve_customer(self, customer):
        pass


class Customer(Thread):
    pass


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
