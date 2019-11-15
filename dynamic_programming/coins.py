import numpy as np
from IPython import embed

def make_change(coins, n):
    m = np.zeros((len(coins)+1, n+1))
    m[0,1:n+1] = np.inf
    for c in range(1, len(coins)+1):
        for r in range(1, n+1):
            if coins[c-1] == r:
                m[c,r] = 1
            elif coins[c-1] > r:
                m[c,r] = m[c-1, r]
            else:
                m[c,r] = min(m[c-1,r], 1+m[c,r-coins[c-1]])
    return m[-1,-1]

def knapsack_problem(values, weights, W):
    m = np.zeros((len(values)+1, W+1))
    k = np.zeros((len(values)+1, W+1))
    for i in range(1,len(values)+1):
        for w in range(1,W+1):
            wi = weights[i-1] # weight of this item
            vi = values[i-1] # value of this item
            if (wi <= w ) and (vi + m[i-1,w-wi] > m[i-1,w]):
                k[i,w] = 1
            else:
                m[i,w] = m[i-1,w]
    picks = []
    C = W
    for i in range(len(values), 0, -1):
        if k[i,C] == 1:
            picks.append(i)
            C -= weights[i-1]
    picks.sort()
    picks = [x-1 for x in picks]
    print(picks)


print(make_change([1,2,10], 33))
print(knapsack_dp([2,3,4],[1,2,3],3,3))




