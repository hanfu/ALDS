class vertice():
	def __init__(self, value):
		self._value = value
		self._edge = []

	def __str__(self):
		return str(self._value)

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	@property
	def edge(self):
		return self._edge

	@edge.setter
	def edge(self, edges):
		self._edge.append(edges)
	
class Graph():
	def __init__(self):
		pass

#dict of v + list of neighbor
gdict = {1:[2,3,4],
		  2:[1,4],
		  3:[1,5,6],
		  4:[2,1,5],
		  5:[3,4],
		  6:[3,4,7],
		  7:[]}

#list of v + list of neighbor
'''
a=b=c=d=e=f=[]
glist = [a,b,c,d,e,f]
num = 0
for i in glist:
	num += 1
	i = gdict[num]
'''
# not working in py cuz of pass by reference

def bfs_gdict(gdict, start):
	done = []
	frontier = [start]
	while frontier:
		#for frontv in frontier:
		for neighborv in gdict[frontier[0]]:
			if neighborv not in done and neighborv not in frontier:
				frontier.append(neighborv)
				# print("n:",neighborv)
		done.append(frontier[0])
		print("v",frontier[0])
		frontier.pop(0)

'''global variables are dangerous
you have to clean them before every call
done = []
frontier = []
'''
'''
The default value is evaluated only once. 
This makes a difference when the default is a mutable object 
such as a list, dictionary, or instances of most classes.
use None if needed
'''
def dfs_gdict(gdict, start, frontier=None):
	if frontier==None:
		frontier = []
	if start not in frontier:
		# print(start)
		frontier.append(start)
		# while frontier:
		print(start)
		#try:
		#because it will always have an income edge so no need to worry about KeyError
		#unless directed
		for v in gdict[start]:
			dfs_gdict(gdict, v, frontier)
		# done.append(start)
		# frontier.pop(0)

def toposort(gdict, done=None, frontier=None):
	if frontier==None:
		frontier = []
	if done == None:
		done = []
	for i in gdict:
		if i not in frontier and i not in done:
			frontier,done=dfs_visit(gdict, i, done, frontier)
	done.reverse()	
	return done

def dfs_visit(gdict, start, done, frontier):
	frontier.append(start)
	for v in gdict[start]:
		if v not in frontier and v not in done:
			dfs_visit(gdict, v, done, frontier)
	done.append(start)
	return frontier,done

#test for toposort
topodict = {
	1:[2],
	2:[3,4],
	3:[],
	4:[],
	5:[4],
	6:[]
}