# Abstract Data Type:
interface spec.

# Data Structure:
algorithm of operations

## linear

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
the most popular ADT in CS

direct vs. chaining vs. open address

python has hash(variable) as pre-hash

### hash func: 
division, multiplication, universal
1. division: v%k
k not be 2 poly or 10 poly
2. multiplication: (v * k)%(2^w) >> (w-r) 
where 2^(w-1) < a < 2^w; or bit size of a
r will be length of hash
fast
3. universal: a little advanced; optimal

### probe func:
permutation is required

linear: (h(v) + k) % m
cause clustering
double hashing: (h1(v)+k * h2(v)) % m
h2(r for all real) should be relatively prime to m

probe performance:
t < 1/(1-ratio)
each probe has p of 1-ratio to succeed
so expect 1/(1-ratio) times

## chaining vs OA
OA:better cache performance(better memory usage, no pointers needed)
Chaining:less sensitive to hash functions (OA requires extra care to avoid clustering) and the load ratio (OA degrades past 70% or so and in any event cannot support values larger than 1)

### hashtable size
grow/shrink performance:
if m += k: t(1+2+..+n) = bigO(n^2)
if m * = k: t(1+k+k^2..+n) = bigO(n), so average constant time for each input
rehashing is necessary as # of buckets changed

### hashtable application: grep
basic: target == [i:i+target.len] for i in source-target.len, cost = target.len* source.len
hash: hash on both side: cost = source.len * hashing cost
rotate hash: save hash time by character editing, make hashing cost to constant time

### rolling hash
base = 265 for ascii
window string as a n-digit number where n = len(window)
the rolling: pop first char and append next char
next window value= window*base - prev_digit*base^n + next_digit
next window hash = hash*base - prev_digit*(base^n%hash)<-pre_calculated + next_digit%hash

## binary search tree

###tree walk: in-, pre- and post- tree walk

## ADT Augment: RBT, AVLT

## REDBLACK TREE
### origined from B-Tree
each node saves a lot keys
black nodes are saving keys
when black nodes full, they turn read and keys become dividents for sub nodes of black trees
keys in red node become 1st key of each subnodes

### representation
[good lecture slides from princeton](https://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf)
so RBT is presenting a 2-3-4 B tree:
a node with two red links represents a 3-key 4-link node; while one red link a 2-3 node;
when insert, if 3-key 4-link full, the middle key move upward and rest two keys splits, the inserted key join one of them

fixup if parent is red:
1. if uncle is red: change n.p.p to red and n.p and uncle black, then check n <= n.p.p
2. if n on antidir of n.p to n.p.p: rotate n.p down and n up, chec n <= just rotated mate
3. if uncle is black: rorate n.p up and n.p.p down, color n.p black and n.p.p red

### left lean RBT:
# todo
a variant of RBT for easier manipulation with same performance #check out princeton algo class
fixup:
1. red link always lean left
2. when two left red link, rotate middle node up right
3. when one left with one right: rotate the bottom up left to case 2
4. when two red children, recolor the parent link


## AVL Tree
# todo
node remembers height
leaf.h = 0, leaf.l/r = -1

### analysis of balance
worst case: Nh = 1 + Nh-1 + Nh-2
<2Nh-2 = 2^(h/2) => bigO(2logn)

### fixups
rotate l and r
double rotate for tri-node structure, because merely one rotate is not enough
insert(6-8-7)=>insert(7-6-8)