from threading import Thread, Lock
import queue


class Cafe:
    def __init__(self, tables_):
        self.queue = queue.Queue(maxsize=3)
        self.tables = tables_
        self.lock = Lock()

    def customer_arrival(self):
        pass

    def serve_customer(self, customer):
        pass


class Table:
    def __init__(self, number):
        self.number = number
        self.busy = False


class Customer(Thread):
    def run(self):
        for i in cafe.tables:
            if not i.busy:
                i.busy = True
            else:





table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

# customer_arrival_thread = Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
# customer_arrival_thread.join()
# for i in cafe.tables:
#     if not i.busy:
#         print(i.number)

# if any(i.busy for i in cafe.tables):
#     print(i.number)
# else:
#     print('All tables are busy')