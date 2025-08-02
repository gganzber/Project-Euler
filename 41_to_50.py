# ~~~~~~ PROBLEM 41 ~~~~~~~~

from itertools import permutations
from math import sqrt
def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

best = 0
str = "123456789"
for i in range(10):
    for elt in permutations(str[: i + 1]):
        x = int("".join(elt))
        if is_prim(x):
            best = max(best, x)
print(best)

# SOLUTION:
# 7652413

# ~~~~~~ PROBLEM 42 ~~~~~~~~

# save list of strings of words as words_list
max_len = 0
for elt in words_list:
   max_len = max(max_len, len(elt))
# max length of a word in words_list is 14. Since the largest value of a capital letter
# in the alphabet comes from "Z" = 90, we need only check amongst triangle words
# no larger than 14 * 90 = 1260
curr = 1
triangles = set()
while (curr * (curr + 1)) // 2 <= 1260:
    triangles.add((curr * (curr + 1)) // 2)
    curr += 1

def name_score(name):
    score = 0
    for elt in name:
        score += ord(elt) - 64
    return score

total = 0

for elt in words_list:
    if name_score(elt) in triangles:
        total += 1

print(total)

# SOLUTION:
# 162

# ~~~~~~ PROBLEM 43 ~~~~~~~~

from itertools import permutations

total = 0

for elt in permutations("0123456789"):
    s = "".join(elt)
    if int(s[7:10]) % 17 == 0:
        if int(s[6:9]) % 13 == 0:
            if int(s[5:8]) % 11 == 0:
                if int(s[4:7]) % 7 == 0:
                    if int(s[3:6]) % 5 == 0:
                        if int(s[2:5]) % 3 == 0:
                            if int(s[1:4]) % 2 == 0:
                                total += int(s)
print(total)

# SOLUTION:
# 16695334890

# ~~~~~~ PROBLEM 44 ~~~~~~~~

pents = [1]
add = 4
best = 10 ** 20

for i in range(10 ** 7):
    pents.append(pents[-1] + add)
    add += 3

pents_set = set(pents)

# since running an O(n ** 2) is too slow over all 10 ** 7 + 1 entries in pents, we first run:
for i in range(10 ** 4):
    for j in range(i + 1, 10 ** 4):
        x = pents[j] - pents[i]
        if x in pents_set:
            if pents[j] + pents[i] in pents_set:
                if x < best:
                    best = x

print(best)
# This gives us a best difference of 5482660
# Now, since the sequence of numbers in pents is monotonically increasing, and the differences
# of subsequent terms can be easily proven to be monotonically increasing, we need only check differences
# up to the 10 ** 7th pentagonal number, since pents[10 ** 7 - 1] - pents[10 ** 7 - 2] = 29999998 > 5482660

# since pents[10 ** 4] - pents[10 ** 4 - 200] = 5940500 > 5482660, we need only check differences
# between terms separated by 200 indices, moving up from index 10 ** 4

for i in range(10 ** 4, 10 ** 7):
    for j in range(i, min(i + 200, 10 ** 7)):
        x = pents[j] - pents[i]
        if x in pents_set:
            if pents[j] + pents[i] in pents_set:
                if x < best:
                    best = x
print(best)

# SOLUTION:
# 5482660


# ~~~~~~ PROBLEM 45 ~~~~~~~~

pentagonals = set()
hexagonals = set()

def tri(num):
    return (num * (num + 1)) // 2
def pent(num):
    return (num * (3 * num - 1)) // 2
def hex(num):
    return num * (2 * num - 1)

curr = 1
index = 1
while curr not in pentagonals or curr not in hexagonals:
    pentagonals.add(pent(index))
    hexagonals.add(hex(index))
    index += 1
    curr = tri(index)
    if curr == 40755:
        index += 1
        curr = tri(index)
print(curr)

# SOLUTION:
# 1533776805

# ~~~~~~ PROBLEM 46 ~~~~~~~~

# Label the non-prime indices below 10 ^ 6 as True
lst = [False] * (10 ** 6)
lst[0], lst[1] = True, True
for i in range(2, 10 ** 6):
  if lst[i] == False:
    x = i
    while x + i < 10 ** 6:
        x += i
        lst[x] = True
sqrs = set()
i = 1
while i * i < 10 ** 6:
    sqrs.add(i * i)
    i += 1
prims = []
for i in range(10 ** 6):
    if lst[i] == False:
        prims.append(i)

from math import sqrt
def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# we only define this for odd composite numbers
def goldbach(num):
    for elt in prims:
        if elt > num:
            return False
        if (num - elt) // 2 in sqrs:
            return True
    return False

curr = 9
while goldbach(curr):
    curr += 2
    while is_prim(curr):
        curr += 2
print(curr)

# SOLUTION:
# 5777


# ~~~~~~ PROBLEM 47 ~~~~~~~~

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

def four_prims(num):
    count = 0
    for elt in prims:
        if elt > num:
            return count == 4
        if num % elt == 0:
            count += 1
    return count == 4

curr = 1
while not(four_prims(curr) and four_prims(curr + 1) and four_prims(curr + 2) and four_prims(curr + 3)):
    curr += 1
print(curr)

# SOLUTION:
# 134043

# ~~~~~~ PROBLEM 48 ~~~~~~~~

total = 0
for i in range(1, 1001):
    total += i ** i
s = str(total)
print(s[-10:])

# SOLUTION:
# 9110846700

# ~~~~~~ PROBLEM 49 ~~~~~~~~

from math import sqrt
def is_prim(num):
  num = abs(num)
  if num <= 1:
    return False
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True


from collections import defaultdict
lst = []
d = defaultdict(list)

for i in range(1000, 10000):
  if is_prim(i):
    l = sorted(str(i))
    d["".join(l)].append(i)
for elt in d:
  if len(d[elt]) >= 3:
    N = len(d[elt])
    ls = d[elt]
    for i in range(N - 2):
      for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
          if ls[j] - ls[i] == ls[k] - ls[j]:
            print(ls[i], ls[j], ls[k])

# prints 1487 4817 8147
# SOLUTION:
# 		   2969 6299 9629


# ~~~~~~ PROBLEM 50 ~~~~~~~~

l = []
# making use of the fact we know there is already a sum of 21 consecutive primes equaling 953
# so the best consecutive sum will have more than 21 terms, meaning the largest term in that
# sum can be at most 1000000 / 21 < 50000
for i in range(2,50000):
  if is_prim(i):
    l.append(i)

best_len = 0
best_prim = 0

N = len(l)
for i in range(N):
  x = l[i]
  index = i + 1
  while (index < N) and (x + l[index] < 1000000):
    x += l[index]
    index += 1
    if is_prim(x):
      if index - i > best_len:
        best_len = index - i
        best_prim = x
print(best_prim)

# SOLUTION:
# 997651
