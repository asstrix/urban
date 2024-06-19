from multiprocessing import Process, Lock


class WarehouseManager():
	def __init__(self):
		self.data = {}
		self.lock = Lock()

	def process_request(self, req):
		item, action, quantity = req
		with self.lock:
			if action == "receive":
				if item in self.data:
					self.data[item] += quantity
				else:
					self.data[item] = quantity

			elif action == "shipment":
				if item in self.data and self.data[item] > 0:
					self.data[item] = max(self.data[item] - quantity, 0)

	def run(self, req):
		processes = []
		for i in req:
			process = Process(target=WarehouseManager.process_request(self, i))
			processes.append(process)
			process.start()
		for process in processes:
			process.join()


if __name__ == '__main__':
	# Создаем менеджера склада
	manager = WarehouseManager()

	# Множество запросов на изменение данных о складских запасах
	requests = [
		("product1", "receive", 100),
		("product2", "receive", 150),
		("product1", "shipment", 30),
		("product3", "receive", 200),
		("product2", "shipment", 50)
	]

	# Запускаем обработку запросов
	manager.run(requests)
	# manager.process_request(requests)

	# Выводим обновленные данные о складских запасах
	print(manager.data)

