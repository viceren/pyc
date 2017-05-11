class ProtectProperty(object):
	"""docstring for ProtectProperty"""
	def __init__(self, name, age, id):
		self.set_name(name)
		self.set_age(age)
		self.set_id(id)

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_age(self):
		return self.__age

	def set_age(self, age):
		if 0 <= age <= 150:
			self.__age = age
		else:
			raise ValueError('Are you human?')

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id

	def print_info(self):
		print('%s: %s %s' %(self.get_name(), self.get_age(),self.get_id()))		

viceren = ProtectProperty('viceren', 151, 156789343)
viceren.print_info()	
		