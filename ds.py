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

    def peak(self):
        return self.items[-1]

    def _isempty(self):
        return self.items == []

class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty: cannot pop an empty stack")

#an stack application on parenthesis checker
def checkp(input):
    s = Stack()
    for e in input:
        if e in '([':
            s.push(e)
        elif e in ')]':
            if e != s.peak():
                return False
            else:
                s.pop()
    return s._isempty()

#an stack application to base convention
def base_convert(decimaln, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    newString = ""

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    while not remstack._isempty():
        newString = newString + digits[remstack.pop()]
    return newString

class Queue:
    def __init__(self, max=10):
        self._items = []
        self._head = 0
        #self._tail = -1
        #instead of tail, track length
        self._length = 0
        self._max = max
        pass
        #need to calc. size of queue
        #http://openbookproject.net/thinkcs/python/english3e/queues.html
class Deque:
    pass
    #double ended queue, add/remove front/rear

    def enqueue(self, item):
        self._items.append(item)
        self._tail +=1

    def dequeue(self):
        del(self._items[self._head])
        self._head +=1

class Node2:
    def __init__(self, value):
        self._prev = None
        self._next = None
        self._v = value

#dll can delete node in bigO(1)
#while sll have to go through the nodes in sequence thus bigO(n)
class DLinkedList:
    def __init__(self):
        self._head = None
        #the input will because the name of head "pointer"

    def insert_front(self, value):
        newn = Node2(value)
        newn._prev = None
        if isinstance(self._head, Node2):
            newn._next = self._head
        self._head = newn

    def search(self, key):
        n = self._head
        #while n.next!=None:
            #if n.value == key: 
                #blah blah
                #bad logic
        while n != None and n._v != key:
            n = n._next
        return n

    def delete(self, key):
        n = self.search(key)
        if n == None:
            raise ValueError('no such value')
        if n._prev == None:
            self._head = n._next            
        else:
            n._prev._next = n._next
        if n._next != None:
            n._next._prev = n._prev

    def printlist(self):
        n = self._head
        while n != None:
            print(n._v)
            n = n._next
        
        


class SLL_arrays:
    #represent linkedlist by three-row arrays
    #arrays means prev, v, next
    pass

class Node3:
    def __init__(self, value):
        self._p = None
        self._l = None
        self._r = None
        self._v = value
    
    def __cmp__(self, other):
        if self.v<other.v:
            return -1        
        elif self.v>other.v:
            return 1
        else:
            return 0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, value):
        self._v = value




class BTree(Node3):
    #no integrate btree class, but enhenced Node3 class
    
    #unnecessary super inherientence in this case
    #def __init__(self, value):
    #    super(BTree, self).__init__(value)

    @property
    def l(self):
        return self._l
    @l.setter
    def l(self, value):
        self._l = value

    @property
    def r(self):
        return self._r
    @r.setter
    def r(self, value):
        self._r = value


class multibranchtree:
    #right node points to same-level nodes, until None
    pass

class PQueue_arr():
    def __init__(self):
        self._items = []

    def _reorder(self, i):
        size = len(self._items)
        l = 2*(i+1) - 1
        r = 2*(i+1)
        maxnode = None
        if l<size and self._items[l] > self._items[i]:
            maxnode = l
        if r<size and self._items[r] > self._items[l]:
            maxnode = r
        if maxnode:
            self._items[maxnode], self._items[i] = self._items[i], self._items[maxnode]
            self._reorder(maxnode)

    def peak(self):
        return self._items[0]

    def givemax(self):
        self._items[0], self._items[-1] = self._items[-1], self._items[0]
        value = self._items.pop()
        self._reorder(0)
        return value

    def enqueue(self, value):
        self._items.append(value)
        self._items[0], self._items[-1] = self._items[-1], self._items[0]
        self._reorder(0)

    #errors:
    #mis-spell names: miss '_'; 
    #wrong methods to python DS,

class PQueue_btree():
    def __init__(self, value):
        self._root = BTree(value)



    def _reorder(self, node):
        maxnode = None
        if node.l and node.l > node:
            maxnode = node.l
        if node.r and node.r >node:
            maxnode = node.r
        if maxnode:
            maxnode.v, node.v = node.v, maxnode.v
            self._reorder(maxnode)

    def enqueue(self, value):
        pass
        #do not know how to implement


class hashtable:

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size


    #if # of slots is proportional to # of keys
    #load factor will be constant
    #search/insert/delete will all be constant time

    #hash func: direct key vs. hashkey
    #hashkey: division, multi, universal
    def hashkey(self, value):
        return value % self.size

    #methods: insert, search, delete
    def insert_chaining(self, value):
        hkey = self.hashkey(value)

        if self.table[hkey] == None:
            self.table[hkey] = [value]
        else:
            self.table[hkey].append(value)

    def insert_openaddr(self, value):
        hkey = self.hashkey(value)
        probe = 0
        while probe<=10 and self.table[hkey] is not None:
            hkey += 3
        self.table[hkey] = value

    def search_chaining(self, value):
        hkey = self.hashkey(value)
        return value in self.table[hkey]

    def search_openaddr(self, value):
        hkey = self.hashkey(value)
        probe = 0
        while probe<=10:
            if self.table[hkey] is not value:
                hkey += 3
                probe += 1
            else:
                return True
        return False
    #collision: slot chaining vs. open addressing
    
    #open address probing: linear, quadratic, double hashing

#if load factor is large, collisions tends to be more
#so lower performance in general