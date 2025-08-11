# ~~~~~~ PROBLEM 71 ~~~~~~~~

import heapq
# given n <= 1000000, want to find largest integer a, such that a / n < 3 / 7
# i. e. 7 * a < 3 * n
# so if (3 * n) % 7 != 0, take a = (3 * n) // 7
# else take (3 * n - 1) // 7

h = []
for n in range(1, 10 ** 6 + 1):
    if (3 * n) % 7 != 0:
        a = (3 * n) // 7
    else:
        a = (3 * n - 1) // 7

    # since heaps in Python are min heaps, we multiply the first entry by -1 to effectively make it a max heap
    heapq.heappush(h, ( - float(a / n), a , n))

print(h[0][1], h[0][2])
# 428570 999997

# we check that 428570 and 999997 are coprime:
for i in range(2, 428571):
    if 999997 % i == 0 and 428570 % i == 0:
        print(i)
# since nothing printed, 428570 and 999997 are coprime.

# SOLUTION:
# 428570

# ~~~~~~ PROBLEM 72 ~~~~~~~~

# This problem reduces to summing over the Euler totient function phi(d) for all 2 <= d <= 1,000,000
# since any fraction on the list n / d with n < d will have a unique expression
# where d <= 1,000,000 and gcd(n, d) = 1. Note d must necessarily be greater
# than or equal to 2, since n, d are positive integers and n < d.

# We make use of the Euler totient formula phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
# where p1, p2, ..., pk are the distinct primes which divide n.

from collections import defaultdict

# stores a list of the distinct prime factors of every 2 <= d <= 1,000,000
prim_factors = defaultdict(list)

lst = [True] * (10 ** 6 + 1)
lst[0], lst[1] = False, False
for i in range(2, 10 ** 6 + 1):
    if lst[i] == True:
        prim_factors[i].append(i)
        x = i + i
        while x < 10 ** 6 + 1:
            prim_factors[x].append(i)
            lst[x] = False
            x += i

# we define this only for integers num >= 2.
def euler_totient(num):
    total = num
    for elt in prim_factors[num]:
        total *= (elt - 1)
        total //= elt
    return total

ans = 0
for i in range(2, 10 ** 6 + 1):
    ans += euler_totient(i)
print(ans)

# SOLUTION:
# 303963552391

# ~~~~~~ PROBLEM 73 ~~~~~~~~

# 1/3 < a / b iff b < 3 * a
# a / b < 1 / 2 iff 2 * a < b
s = set()

for b in range(4, 12001):
    for a in range(b // 3, b // 2 + 2):
        if b < 3 * a and 2 * a < b:
            s.add(float(a) / float(b))
print(len(s))
# SOLUTION:
# 7295372

# ~~~~~~ PROBLEM 74 ~~~~~~~~

def fact(num):
    prod = 1
    for i in range(2, num + 1):
        prod *= i
    return prod

facts = {}
for i in range(10):
    facts[str(i)] = fact(i)

def add_fact(num):
    total = 0
    s = str(num)
    for elt in s:
        total += facts[elt]
    return total

def loop_count(num):
    s = set()
    s.add(num)
    total = 1
    while add_fact(num) not in s:
        num = add_fact(num)
        s.add(num)
    return len(s)

total = 0
for i in range(1000000):
    if loop_count(i) == 60:
        total += 1
print(total)

# SOLUTION:
# 402

# ~~~~~~ PROBLEM 75 ~~~~~~~~

from math import sqrt
prim_pythag = set()

# Use Euclid's formula to generate all primitive Pythagorean triples whose sum doesn't exceed 1500000.
# Since we don't insist gcd(m, n) = 1, we'll generate some non-primitive triples too.
for n in range(1, int(sqrt(1500000))):
    for m in range(n + 1, int(sqrt(1500000))):
        a, b = n ** 2, m ** 2
        if (b - a + 2 * m * n + b + a) > 1500000:
            continue
        if b - a < 2 * m * n:
            prim_pythag.add((b - a, 2 * m * n, a + b))
        else:
            prim_pythag.add((2 * m * n, b - a, a + b))

l = list(prim_pythag)
l.sort()

# Add all non-primitive Pythagorean triples whose sum doesn't exceed 1500000 to prim_pythag.
for elt in l:
    A, B, C = elt[0], elt[1], elt[2]
    x, y, z = 2 * A, 2 * B, 2 * C
    while x + y + z < 1500000:
        prim_pythag.add((x, y, z))
        x, y, z = x + A, y + B, z + C

l2 = list(prim_pythag)
l2.sort()

# lst[i] will give the number of distinct Pythagorean triples in prim_pythag whose sum equals i.
lst = [0] * (1500000 + 1)

for elt in l2:
    lst[sum(elt)] += 1

total = 0

for elt in lst:
    if elt == 1:
        total += 1
print(total)

# SOLUTION:
# 161667

# ~~~~~~ PROBLEM 76 ~~~~~~~~

counts = [[0] * 101 for _ in range(101)]

# We use dynamic programming to store the following information:
# counts[i][j] will represent the number of ways to write the number i as a partition with largest part at most j.
# We recursively calculate counts[i][j], by recursing on the size of the largest part in the partition.
counts[0][0] = 0
for i in range(1, 100):
    counts[i][1] = 1
    counts[1][i] = 1
    counts[0][i] = 0
    counts[i][0] = 0

for i in range(2, 100):
    for j in range(2, 100):
        total = 0
        for k in range(j + 1):
            total += counts[i - k][k]
        if i == j:
            total += 1
        if i < j:
            counts[i][j] = counts[i][i]
        else:
            counts[i][j] = total

total = 0
for i in range(1, 100):
    total += counts[100 - i][i]
print(total)

# SOLUTION:
# 190569291

# ~~~~~~ PROBLEM 77 ~~~~~~~~

# list all the primes below 10 ** 6
lst = [True] * (10 ** 6)
lst[0], lst[1] = False, False
for i in range(2, 10 ** 6):
    if lst[i] == True:
        x = i + i
        while x < 10 ** 6:
            lst[x] = False
            x += i
prims = []

for i in range(10 ** 6):
    if lst[i] == True:
        prims.append(i)

s = set(prims)

# We use dynamic programming to store the following information:
# table[i][j] will represent the number of ways to write the number i
# as a sum of prime numbers, whose largest part is at most j.
table = [[0] * 101 for _ in range(101)]

for i in range(2, 101):
    for j in range(2,101):
        if j > i:
            table[i][j] = table[i][i]
        else:
            total = 0
            for k in range(2, j + 1):
                # we recurse on the largest part k (number) in the sum, which must
                # necessarily be a prime number
                if k in s:
                    total += table[i - k][k]
            if i == j and i in s:
                total += 1
            table[i][j] = total

# table[i][i] will represent the number of ways to write the number i
# as a sum of any prime number, including itself if it is prime.
for i in range(101):
    if table[i][i] > 5000:
        print(i)
        break

# SOLUTION:
# 71

# ~~~~~~ PROBLEM 79 ~~~~~~~~

# Save the list of 3 digit combinations as a list of strings l

from collections import defaultdict

d = defaultdict(set)
for s in l:
    a, b, c = s[0], s[1], s[2]
    d[a].add(b)
    d[a].add(c)
    d[b].add(c)

print(d)

# printing d and starting from the digit with the largest set of subsequent values, we see that
# the passcode "73162890" is the shortest password possible

# SOLUTION:
# 73162890

# ~~~~~~ PROBLEM 80 ~~~~~~~~

# Returns the step^(th) digit (0 - indexed) of the square root of the number num,
# where digits is the list of numbers s * 10 + i for 0 <= i <= 9
# where s = 10 ** (step - 1) * (the decimal digit expansion of the square root of num up to the (step - 1) ^th index).
def bin_search_sq(num, step, digits):
    left, right = 0, 9
    while left < right:
        mid = (left + right + 1) // 2
        if digits[mid] * digits[mid] > num * (10 ** (2 * step)):
            right = mid - 1
        else:
            left = mid
    return left

# Returns the sum of the first hundred digits of the decimal expansion of num
def first_hundred(num):
    total = 0
    step = 0
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    curr_str = ""
    for _ in range(100):
        x = bin_search_sq(num, step, digits)
        curr_str += str(x)
        total += x
        step += 1
        new_digs = []
        for i in range(10):
            new_digs.append(int(curr_str + str(i)))
        digits = new_digs
    return total

sqrs = set()
for i in range(1, 11):
    sqrs.add(i * i)

total = 0
for i in range(2, 101):
    if i not in sqrs:
        total += first_hundred(i)
print(total)
# SOLUTION:
# 40886
