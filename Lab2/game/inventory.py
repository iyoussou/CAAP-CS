import scenes as S

class Inventory(object):

	storage = []

	def store_item(self, item):
		self.item = item
		self.storage.append(self.item)

	def check_inventory(self):
		if storage[0]:
			print("\n----------------------------------------------------------------")
			for i in range(len(self.storage)):
				print(self.storage[i])
			print("\n----------------------------------------------------------------")

	def storage(self, item):
		self.item = item
		for i in range(len(self.storage)):
			if storage[i] == self.item:
				return True