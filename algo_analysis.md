## notation
theta: give both upper and lower bound by c*g(x)
big O: upper bound
omega: lower bound

## divide and conquer
based on recurrsion, write
T(n) = divide.k*T(n.sub) + conquer.n

1. guess T(n), plug back to equation to verify
2. draw recurrsion tree and count n of each level, and # of total levels
3. master method, empirical cookbook method

## Probabilistic Analysis
Expectation of Event E(e)

### Ex. E(# of inversion pairs in a random array)
E(#) = \sum i=1~n E(ni's pair#) = 1/2*((n-1)+...1) = 1/4n(n-1)
