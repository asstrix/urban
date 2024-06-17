import time, threading


class BankAccount(threading.Thread):
    def __init__(self):
        super(BankAccount, self).__init__()
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance: {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
            print(f'Withdrawn {amount}, new balance: {self.balance}')


def deposit_task(acc, amount):
    for i in range(5):
        time.sleep(1)
        acc.deposit(amount)


def withdraw_task(acc, amount):
    for i in range(5):
        time.sleep(1)
        acc.withdraw(amount)


account = BankAccount()
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
time.sleep(0.1)
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()