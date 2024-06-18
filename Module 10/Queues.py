import queue
from threading import Thread, Lock
import time


class Table:
    def __init__(self, id):
        self.id = id
        self.busy = False
        self.lock = Lock()


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue(maxsize=3)
        self.tables = tables
        self.customer_id = 0

    def customer_arrival(self):
        for _ in range(20):
            self.customer_id += 1
            print(f"Customer {self.customer_id} arrived")
            customer_thread = Thread(target=self.serve_customer, args=(self.customer_id,))
            customer_thread.start()
            time.sleep(3)  # Simulate real - time arriving, else a customer will go out 

    def serve_customer(self, customer_id):
        while True:
            for table in self.tables:
                if not table.busy:
                    with table.lock:
                        if not table.busy:
                            table.busy = True
                            print(f"Customer {customer_id} sat at table {table.id}")
                            time.sleep(5)
                            table.busy = False
                            print(f"Customer {customer_id} has left table {table.id}")
                            return
            try:
                self.queue.put(customer_id, timeout=1)
                print(f"Customer {customer_id} is waiting for free table")
                break
            except queue.Full:
                print(f"Customer {customer_id} omg, the queue is so big, im leaving!")
                return


tables = [Table(i) for i in range(1, 4)]
cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
