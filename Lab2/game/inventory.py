import scenes as S

class Inventory(object):

	storage = ['Inventory:']

	def store_item(self, item):
		self.item = item
		self.storage.append(self.item)

	def check_inventory(self):
		print("\n----------------------------------------------------------------")
		for i in range(len(self.storage)):
			print(self.storage[i])
		print("\n----------------------------------------------------------------")

	def return_item(self, item):
		self.item = item
		for i in range(len(self.storage)):
			if self.storage[i] == self.item:
				return True
