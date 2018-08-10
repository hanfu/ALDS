#getter, setter, property
class java:
	def __init__(self, n):
		self._value = n

	#traditiona getter and setter methods
	def getter(self):
		return self._value

	def setter(self, newn):
		self._value = newn

	#add the property
	value = property(fget=getter, fset=setter, doc="Property: value")

class python:
	def __init__(self,n):
		self._value = n

	#read-only getter
	@property
	def value(self):
		#possible for statements
		return self._value

	#the property setter
	@value.setter
	def value(self, n):
		#possible for validation
		self._value = n
	
#properties

