# linear

stack, queue, deque, linked list, double linked list

insert,/delete, search, max/min, successor/predecessor

## HEAP

binary tree
n.parent = n//2
n.left = 2n
n.right = 2n+1

height = lg n

### max/min heap
max heap: parent>n>children

### Priority Queue (heap powered)

given arr

```python
def showmax(arr):
	return arr[0]

```

## current issues
* no examplary implementation, most are arbitary code snippets
* confusion between functional programming and object-oriented programming
*** use provided list/dict and user-defined funcs
*** design new class objects with funcs included
* reuse of code from .py to .md

## hashing:
direct vs. chaining vs. open address

## binary search tree

###tree walk: in-, pre- and post- tree walk

## REDBLACK TREE
### origined from B-Tree
each node saves a lot keys
black nodes are saving keys
when black nodes full, they turn read and keys become dividents for sub nodes of black trees
keys in red node become 1st key of each subnodes

### representation
so RBT is presenting a 3-4 B tree:
a node with two red links represents a 3-key 4-link node; while one red link a 2-3 node;
fixup if parent is red:
1. if uncle is red: change n.p.p to red and n.p and uncle black, then check n <= n.p.p
2. if n on antidir of n.p to n.p.p: rotate n.p down and n up, chec n <= just rotated mate
3. if uncle is black: rorate n.p up and n.p.p down, color n.p black and n.p.p red

### left lean RBT:
a variant of RBT for easier manipulation with same performance #check out princeton algo class
fixup:
1. red link always lean left
2. when two left red link, rotate middle node up right
3. when one left with one right: rotate the bottom up left to case 2
4. when two red children, recolor the parent link
