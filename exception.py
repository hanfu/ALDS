class Stack:
	pass
	def pop(self):
		if self._isempty():
			raise EmptyStackError("Empty Stack")
		self.items.pop()
		self.top -= 1

class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty: cannot pop an empty stack")

