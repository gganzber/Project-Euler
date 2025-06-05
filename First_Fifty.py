#~~~~~~ PROBLEM 1 ~~~~~~~~

total = 0
for i in range(1000):
  if (i % 3 == 0) or (i % 5 == 0):
    total += i
print(total)
# SOLUTION:
# 233168

#~~~~~~ PROBLEM 2 ~~~~~~~~

a, b, total = 1, 1, 0
while b < 4000000:
  if b % 2 == 0:
    total += b
  a, b = b, a + b
print(total)
# SOLUTION:
# 4613732

#~~~~~~ PROBLEM 3 ~~~~~~~~

from math import sqrt
def is_prim(num):
  num = abs(num)
  if num <= 1:
    return False
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

best = 0
for i in range(int(sqrt(600851475143)) + 1):
  if is_prim(i):
    if 600851475143 % i == 0:
      best = i
print(best)
# SOLUTION:
# 6857

~~~~~~ PROBLEM 4 ~~~~~~~~

def is_pal(num):
  s = str(num)
  N = len(s)
  for i in range(N // 2):
    if s[i] != s[-i-1]:
      return False
  return True

best = 0
for i in range(100, 1000):
  for j in range(100, 1000):
    if is_pal(i * j):
      best = max(best, i * j)
print(best)
# SOLUTION
# 906609

~~~~~~ PROBLEM 5 ~~~~~~~~

# We decompose 2, 3, ... , 20 into their prime factorizations. The solution will be
# the product p ^ alpha, over all primes in the list, where alpha is the max power
# of the prime p among all the prime decompositions in the list

# 2 = 2 ^ 1             8 = 2 ^ 3             14 = 2 ^ 1 * 7 ^ 1      20 = 2 ^ 2 * 5 ^ 1
# 3 = 3 ^ 1             9 = 3 ^ 3             15 = 3 ^ 1 * 5 ^ 1
# 4 = 2 ^ 2             10 = 2 ^ 1 * 5 ^ 1    16 = 2 ^ 4
# 5 = 5 ^ 1             11 = 11 ^ 1           17 = 17 ^ 1
# 6 = 2 ^ 1 * 3 ^ 1     12 = 2 ^ 2 * 3 ^ 1    18 = 2 ^ 1 * 3 ^ 2
# 7 = 7 ^ 1             13 = 13 ^ 1           19 = 19 ^ 1

# this gives the LCM of the numbers 1, 2, ... , 20, which is the answer

# SOLUTION:
(2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
