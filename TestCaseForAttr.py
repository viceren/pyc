class TestCaseForAttr(object):
	"""docstring for TestCaseForAttr"""
	def __init__(self, age):
		self.set_age(age)

	def get_age(self):
			return self.__age
	
	def set_age(self, age):
			if 0 <= age <= 150:
				self.__age = age
			else:
				raise ValueError('Get Wrong Age!')
	
	def print_attr(self):
		print('%s:' % (self.get_age()))
Viceren = TestCaseForAttr(151)
Viceren.print_attr()

