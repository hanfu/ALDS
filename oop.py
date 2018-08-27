#static variable
class theclass:
	#variables defined at class level are static
	staticv = 10

a = theclass()
a.staticv #10
a.staticv = 9#only change instance a
theclass.staticv = 9#change at the class level

#instance property, getter, setter
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

#static, class, instance method
class theclass:
	def insm(self):
		pass
		#modify instance, called only at instance level

	@classmethod
	def clsm(cls):
		pass
		#modify cls, callable to both instance and cls level
		#useful for class' utility func, 

	@staticmethod
	def staticm():
		pass
		#access only input args, callable at both levels

#function-oriented decorators
def decor_func(innerfunc):
    def wrapper(*a, **kw):
        print("entering")
        innerfunc(*a, **kw)
        print("exited")
    #wrapper.__name__ = innerfunc.__name__
    #if name matters
    return wrapper

def func1(*a, **kw):
    print("Wheee!")

func1_d = decor_func(func1)

@decor_func
def newfunc1(*a, **kw):
	print("whoooa")

print(newfunc1.__str__)
#returns function decor_func.<locals>.wrapper


#class-oriented decorator equavalent to previous
class decor_obj:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@decor_obj
def func2():
    print("whaiii")



#even change the function call
class myDecorator:
    def __init__(self, f):
        print("inside myDecorator.__init__()")
        f() # Prove that function definition has completed
    def __call__(self):
        print("inside myDecorator.__call__()")

@myDecorator
def aFunction():
    print("inside aFunction()")
#decorator declared with __init__now:
#as soon as func defined, it prompts
#__init__
#inside func()

#aFunction is a myDecorator object
aFunction()
#print 
#now prints myDecorator.__call__()
#NOT inside func because class attr overwrite

def decorator(func):
	pass

@decorator
def foo(*args, **kwargs):
    pass
#translates to
foo = decorator(foo)

#So if the decorator had arguments,
def decorator_arg(arg):
	return decorator
	#return a decorator func

arg = 'someblah'
@decorator_arg(arg)
def foo(*args, **kwargs):
    pass
#translates to
foo = decorator_arg(arg)(foo)


#talking about super()
#1. pass subclass' args to superclass
class Superclass(object):
    def __init__(self, arg1, arg2, arg3):
        #Initialise some variables
        #Call some methods
        pass

class Subclass(Superclass):
    def __init__(self, subclass_arg1, *args, **kwargs):
        super().__init__(*args, **kwargs)
		#same as Superclass.__init__(*a, **kw)
		#if python2, super(ClassName, self).__init__()
        pass


#2. shortcut for parent class in more subtle inherentence
class A():
    def __init__(self):
        print("A")
        self.a = 'a'

class B(A):
    def __init__(self):
        print("B")
        self.b = 'b'
        #class A not init at all. 
        #no 'first' printed, nor attr a.

class C(B):
    def __init__(self):
        super().__init__()
        print("C")
        #super calls class B
        #prints second and third, and have attr b = 'b'


#override: subclass replace the method/attr
#overload: same method act differently on different input(mostly data type)



#try except testing
arr = [1,2,3]
def tryindex(arr):
	try:
		maximum = 1
		maximum = max(arr[2],  arr[3], 2)
		maximum = 10
	except IndexError:
		pass
        maximum = 100
	else:
    #optional if you only want it execute when no exception
        return maximum
	#conclusion: run till error line
	#conclusion: python will abort entire line 

#__getattr__三连
getattr
setattr
hasattr#only return AttributeError

#generator
'''
coroutine vs. subroutine
subroutines are like functions/methods/callables, takes one return
return implies that the function is returning control of execution to the point where the function was called
coroutine yields results and remember the state, and can continue after one "return" and produce a series of yields
Yield, implies that the transfer of control is temporary and voluntary, and our function expects to regain it in the future
compare with multi-threading, coroutine is a cooperative multitasking with memory, while threads is pre-emptive multitasking
'''
iterables = ['a', 'bb', 'ccc']
iterator = iter(iterables)
next(iterator)
def generator(): #the generator function
	yield 'a'
	yield 'bb'
	yield 'ccc'
gener = generator()#gener is now a generator
next(gener)

def count4ever(start):
	while True:
		start += 1
		yield start

g = count4ever(10)
g.next()

def fib():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b


def count4ever_send():
	while True:
		start = yield
		yield start+1
gsend = count4ever_send()
gsend.send(None) # to init the generator
gsend.next() # or use next to init the generator
gsend.send(10)#free to change parameter on the fly

#generator expressions
gsq = (x**2 for x in range(999))
sum(gsq)# takes almost no memory!! efficient!!
 
#in term of efficiency
#map, filter, reduce

###homemade iterator
class ExampleIterator:
	def __init__(self, datalist):
		self.index = 0
		self.data = datalist
	def __iter__(self):
		return self
	def __next__(self):
		if self.index >= len(self.data):
			raise StopIteration()
		rslt = self.data[self.index]
		self.index += 1
		return rslt

g = ExampleIterator([1,2,3])

#ascii
ord('a')
chr(97)