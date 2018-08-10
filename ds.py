class Stack:
	def __init__(self):
		self.items = []
		self.top = -1

	def push(self, item):
		self.items.append(item)
		self.top += 1

	def pop(self):
		if self._isempty():
			raise EmptyStackError("Empty Stack")
		self.items.pop()
		self.top -= 1

	def _isempty(self):
		return self.items == []

class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty: cannot pop an empty stack")

class priority_queue():
	def __init__(self):
		pass