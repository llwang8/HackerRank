
#==============================================
# Q. 1


#==============================================
# Q. 2
#!/bin/python

import sys

if __name__ == "__main__":
    n, x, m = raw_input().strip().split(' ')
    n, x, m = [int(n), int(x), int(m)]
    #wheel = []
    profit = 0
    for a0 in xrange(n):
        w, p = raw_input().strip().split(' ')
        w, p = [int(w), int(p)]
        #wheel.append([w, p])
        profit += 1.0 * (x - w) * p / 100.0

    profit *= m
    print format(profit, '.1f')

#==============================================
# Q. 3
#!/bin/python

# First Attempt
import sys
from itertools import combinations

def solve(n, m, d, c):
    diff = sum(d) - sum(c) # difference between sum of debit and sum of credit
    all_operations = d
    min_diff_operations = []

    # find the min absolute of sum of tuple minus diff from a list of tuple
    def find_min_diff(li):
        result = [abs(sum(tup)-diff/2) for tup in li]
        #mn,idx = min( (l[i],i) for i in xrange(len(l)) )
        return min(result)

    for e in c:
        all_operations.append(-e)

    for k in range(1, (n+m)):
        comb = list(combinations(all_operations, k))
        min_diff_operations.append((find_min_diff(comb), k)) # list of tuples stores min diff with number of operations

    diff_dict = {}
    for tup in min_diff_operations:
        if tup[0] not in diff_dict:
            diff_dict[tup[0]] = [tup[1]]
        else:
            diff_dict[tup[0]].append(tup[1])
    #print diff_dict
    min_diff = min(diff_dict.keys())
    return str(min_diff) + '' + str(min(diff_dict[min_diff]))

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    d = map(int, raw_input().strip().split(' '))
    c = map(int, raw_input().strip().split(' '))
    result = solve(n, m, d, c)
    print " ".join(map(str, result))


# Second Attempt
#!/bin/python

import sys
from itertools import combinations

def solve(n, m, d, c):
    diff = sum(d) - sum(c) # difference between sum of debit and sum of credit
    all_operations = d
    min_diff_operations = []

    # find the min absolute of sum of tuple minus diff from a list of tuple
    def find_min_diff(li):
        result = [abs(sum(tup)-diff/2) for tup in li]
        return min(result)

    for e in c:
        all_operations.append(-e)

    for k in range(1, (n+m)):
        comb = list(combinations(all_operations, k))
        min_diff_operations.append((find_min_diff(comb), k)) # list of tuples stores min diff with number of operations

    l = min_diff_operations
    return min( (l[i]) for i in xrange(len(l)) )


if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    d = map(int, raw_input().strip().split(' '))
    c = map(int, raw_input().strip().split(' '))
    result = solve(n, m, d, c)
    print " ".join(map(str, result))

#==============================================
# Q. 4
#!/bin/python

import sys

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fib_friendly = []

def is_fib_friendly(n):
    d_dict = {}
    for e in str(n).split():
        if e in d_dict:
            d_dict[e] += 1
        else:
            d_dict[e] = 1
    for k in d_dict:
        if d_dict[k] not in fib:
            return False

def solve(n):
    count = 1
    k = 1
    while count <= n:
        if k not in fib_friendly:
            if is_fib_friendly(k):
                count += 1
                fib_friendly.append(k)
        k += 1
    return k


q = int(raw_input().strip())
for a0 in xrange(q):
    n = long(raw_input().strip())
    result = solve(n)
    print(result)



#==============================================
# Q. 5
