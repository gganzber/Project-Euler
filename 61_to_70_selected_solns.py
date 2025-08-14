# ~~~~~~ PROBLEM 61 ~~~~~~~~

def tr(n):
    return (n * (n + 1)) // 2

def sq(n):
    return n * n

def pt(n):
    return (n * (3 * n - 1)) // 2

def hx(n):
    return n * (2 * n - 1)

def ht(n):
    return (n * (5 * n - 3)) // 2

def ot(n):
    return n * (3 * n - 2)

lst = [[], [], [], [], [], []]

x = 1

while tr(x) < 10000:
    a, b, c, d, e, f = tr(x), sq(x), pt(x), hx(x), ht(x), ot(x)

    l = [a, b, c, d, e, f]
    for i in range(6):
        if 1000 <= l[i] and l[i] < 10000:
            lst[i].append(l[i])
    x += 1

from collections import defaultdict

tr_starts = defaultdict(list)
sq_starts = defaultdict(list)
pt_starts = defaultdict(list)
hx_starts = defaultdict(list)
ht_starts = defaultdict(list)
ot_starts = defaultdict(list)

starts = [tr_starts, sq_starts, pt_starts, hx_starts, ht_starts, ot_starts]

for i in range(6):
    elt = lst[i]
    for num in elt:
        s = str(num)
        starts[i][s[:2]].append(num)

import itertools

# Since the order of terms could come from any permutation of collections of numbers, we can start
# with an octogonal number, without loss of generality (by cyclical property of the solution), and permute the remaining first five lists in starts.
ind_lst = [0, 1, 2, 3, 4]
perms = list(itertools.permutations(ind_lst))

for elt in new_lst[-1]:
    s = str(elt)
    start, end = s[:2], s[2:]
    for l in perms:
        i1, i2, i3, i4, i5 = l[0], l[1], l[2], l[3], l[4]

        if len(starts[i1][end]) == 0:
            break
        for elt2 in starts[i1][end]:
            s2 = str(elt2)
            end2 = s2[2:]

            if len(starts[i2][end2]) == 0:
                break
            for elt3 in starts[i2][end2]:
                s3 = str(elt3)
                end3 = s3[2:]

                if len(starts[i3][end3]) == 0:
                    break

                for elt4 in starts[i3][end3]:
                    s4 = str(elt4)
                    end4 = s4[2:]

                    if len(starts[i4][end4]) == 0:
                        break

                    for elt5 in starts[i4][end4]:
                        s5 = str(elt5)
                        end5 = s5[2:]

                        if len(starts[i5][end5]) == 0:
                            break

                        for elt6 in starts[i5][end5]:
                            s6 = str(elt6)
                            end6 = s6[2:]

                            if len(starts[-1][end6]) == 0:
                                break

                            for elt7 in starts[-1][end6]:
                                if elt7 == elt:
                                    print(elt7, elt2, elt3, elt4, elt5, elt6)
                                    
# This prints the unique solution:
# 1281 8128 2882 8256 5625 2512
# Their sum is:

# SOLUTION:
# 28684

# ~~~~~~ PROBLEM 62 ~~~~~~~~

from collections import Counter

# return a tuple, where index i counts the number of the digit 0 <= i <= 9 in a number num
def tup_dig(num):
    lst = [0] * 10
    s = str(num)
    for elt in s:
        lst[int(elt)] += 1
    return tuple(lst)

c = Counter()
cubes = []
for i in range(100000):
    x = i ** 3
    c[tup_dig(x)] += 1
    cubes.append(x)

# print the first cube who shares the same digit count with exactly five other cubes
# which is equivalent to exactly 5 permutations of the printed number being cubes.
for elt in cubes:
    if c[tup_dig(elt)] == 5:
        print(elt)
        break

# SOLUTION:
# 127035954683

# Note that (10 ** 5) ** 3 has 16 digits and our answer has 12 digits,
# so no number greater than 10 ** 5 could possibly cube to a permutation of our solution.
# So 127035954683 has exactly 5 permutations which are cubes.

# ~~~~~~ PROBLEM 63 ~~~~~~~~

# note 1, 2, ..., 9 are all 1-digit 1-powers.
total = 9
# now 10 ** i has i + 1 digits for all i >= 1
# so we need only check base values 2,...,9 (since 1 ** i = 1 for all i >= 2)
# and 9 ** 22 has 21 digits, so n ** i cannot have i digits for 2 <= n <= 9 and i >= 22
# thus we check:
for i in range(2, 22):
    for n in range(2, 10):
        if len(str(n ** i)) == i:
            total += 1
print(total)

# SOLUTION:
# 49

# ~~~~~~ PROBLEM 64 ~~~~~~~~

from math import sqrt
# Returns the numerator and denominator a, b of the fraction (integer part + (sqrt(sq) - a) / b)
# of the reciprocated fraction (denom / (sqrt(sq) - num)). We write "num" to denote starting numerator
# and "denom" to denote starting denominator.
def flip(sq, num, denom):
    new_denom = (sq - num ** 2) // denom

    int_part = int((sqrt(sq) + num) / new_denom)

    new_num = (int_part * new_denom) - num

    return (new_num, new_denom)

# Returns the period length of an irrational square root sqrt(sq) for sq a non-square integer
def period(sq):
    seen = set()

    num = int(sqrt(sq))
    denom = 1

    # we continue to compute the continued fraction sqrt(sq) until we
    # reach a (numerator, denominator) pair already seen, which will create a loop
    while (num, denom) not in seen:
        seen.add((num, denom))
        num, denom = flip(sq, num, denom)

    return len(seen)

# The set of squares below 10000
sqrs = set()
for i in range(1, int(sqrt(10000)) + 1):
    sqrs.add(i * i)

total = 0
for i in range(1, 10000 + 1):
    if i in sqrs:
        continue
    if period(i) % 2 == 1:
        total += 1
print(total)

# SOLUTION:
# 1322

# ~~~~~~ PROBLEM 65 ~~~~~~~~

coeffs = [2, 1, 2]
index = 2
for _ in range(33):
    coeffs.append(1)
    coeffs.append(1)
    coeffs.append(2 * index)
    index += 1

b = coeffs[99]
num = 1

for n in range(99, 0, -1):
    a = coeffs[n - 1]

    x = num
    num = b
    b = a * b + x

total = 0
numerator = str(b)
for elt in numerator:
    total += int(elt)
print(total)

# SOLUTION:
# 272

# ~~~~~~ PROBLEM 67 ~~~~~~~~

# We save the integers in each row of the given triangle as list of lists l.
# We then use dynamic programming to calculate the maximal path sum into any given node
# in the triangle, starting at the top of the triangle. We store these values in the list of lists called best

best = [[0] * i for i in range(1, 101)]

best[0][0] = l[0][0]
for i in range(99):
    for j in range(i + 1):
        best[i + 1][j] = max(best[i + 1][j], best[i][j] + l[i + 1][j])
        best[i + 1][j + 1] = max(best[i + 1][j + 1], best[i][j] + l[i + 1][j + 1])

print(max(best[-1]))
# SOLUTION:
# 7273

# ~~~~~~ PROBLEM 68 ~~~~~~~~

import itertools

ans = []

digs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(itertools.permutations(digs))

# since we're only looking at 16 digit solutions, 10 must be an exterior node, since it's the only number btw 1 and 10 with 2 digits.
# we can label all the nodes in the graph, starting with the node with value 10
# we'll label the outer nodes 1 through 5, going counter-clockwise
# and we'll label the inner nodes 6 - 10, going counter-clockwise, starting at the node
# closest to the node labeled 10.

# in terms of the indices of our permutation, this would mean
# lst[0] is the node labeled 2, lst[1] the node labeled 3, etc.
# and lst[4] is the node labeled 6, lst[5] the node labeled 7, etc

for lst in perms:
    yes = False
    # note we'll check 10 + lst[4] + lst[5] == lst[0] + lst[5] + lst[6] which is equivalent to:
    if 10 + lst[4] == lst[0] + lst[6]:
        if lst[0] + lst[5] == lst[1] + lst[7]:
            if lst[1] + lst[6] == lst[2] + lst[8]:
                if lst[2] + lst[7] == lst[3] + lst[4]:
                    if lst[3] + lst[8] == 10 + lst[5]:
                        yes = True
                        #print(lst)
    if yes == False:
        continue
        
    l = [10, lst[0], lst[1], lst[2], lst[3]]
    l.sort()
    
    a = [lst[0], lst[5], lst[6], lst[1], lst[6], lst[7], lst[2], lst[7], lst[8], lst[3], lst[8], lst[4], 10, lst[4], lst[5]]
    if l[0] == lst[0]:
        new = a
    elif l[0] == lst[1]:
        new = a[3:] + a[:3]
    elif l[0] == lst[2]:
        new = a[6:] + a[:6]
    elif l[0] == lst[3]:
        new = a[9:] + a[:9]
    else:
        new = a[12:] + a[:12]

    s = ""
    for elt in new:
        s += str(elt)
    
    ans.append(s)
ans.sort(reverse = True)
ans[0]

# SOLUTION:
# 6531031914842725

# ~~~~~~ PROBLEM 69 ~~~~~~~~

# Label the non-prime indices below 10 ^ 6 as True
lst = [False] * (10 ** 6)
lst[0], lst[1] = True, True
for i in range(2, 10 ** 6):
  if lst[i] == False:
    x = i
    while x + i < 10 ** 6:
        x += i
        lst[x] = True
prims = []
for i in range(10 ** 6):
    if lst[i] == False:
        prims.append(i)

# the solution will be the largest product of the first j primes in the list prims
# such that the product is less than 10 ** 6, for some j >= 1.
num = 1
for elt in prims:
    if num * elt > 1000000:
        break
    num *= elt
print(num)

# SOLUTION:
# 510510

# ~~~~~~ PROBLEM 70 ~~~~~~~~

# Generate all primes with at most 7 digits
lst = [True] * (10 ** 5)
lst[0], lst[1] = False, False
for i in range(2, 10 ** 5):
    if lst[i] == True:
        x = i + i
        while x < 10 ** 5:
            lst[x] = False
            x += i
prims = []
for i in range(10 ** 5):
    if lst[i] == True:
        prims.append(i)
        
prims.sort(reverse = True)

# Returns True if and only if two numbers n and m are permutations of each other
def is_perm(n, m):
    n_digs = [0] * 10
    m_digs = [0] * 10
    for elt in str(n):
        n_digs[int(elt)] += 1
    for elt in str(m):
        m_digs[int(elt)] += 1
    return n_digs == m_digs

best = 10 ** 20
best_val = 0

# we use the fact that by inclusion-exclusion, the Euler totient of
# a number x = p * q for primes p and q
# equals x - x // p - x // q + 1
# where the last term in the sum comes from 1 = x // (p * q)

for p in prims:
    for q in prims:
        x = p * q
        if x >= 10 ** 7:
            continue
        if is_perm(x, x - x // p - x // q + 1):
            if float(x) / (x - x // p - x // q + 1) < best:
                best = float(x) / (x - x // p - x // q + 1)
                best_val = x
print(best_val)

# SOLUTION:
# 8319823
