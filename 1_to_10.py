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

#~~~~~~ PROBLEM 4 ~~~~~~~~

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

#~~~~~~ PROBLEM 5 ~~~~~~~~

# We decompose 2, 3, ... , 20 into their prime factorizations. The solution will be
# the product of p ^ alpha, over all primes in the list, where alpha is the max power
# of the prime p among all the prime decompositions in the list

# 2 = 2 ^ 1             8 = 2 ^ 3             14 = 2 ^ 1 * 7 ^ 1      20 = 2 ^ 2 * 5 ^ 1
# 3 = 3 ^ 1             9 = 3 ^ 2             15 = 3 ^ 1 * 5 ^ 1
# 4 = 2 ^ 2             10 = 2 ^ 1 * 5 ^ 1    16 = 2 ^ 4
# 5 = 5 ^ 1             11 = 11 ^ 1           17 = 17 ^ 1
# 6 = 2 ^ 1 * 3 ^ 1     12 = 2 ^ 2 * 3 ^ 1    18 = 2 ^ 1 * 3 ^ 2
# 7 = 7 ^ 1             13 = 13 ^ 1           19 = 19 ^ 1

# this gives the LCM of the numbers 1, 2, ... , 20, which is the answer

(2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19

# SOLUTION:
# 232792560

#~~~~~~ PROBLEM 6 ~~~~~~~~

# Here we make use of the fact that (a_1 + a_2 + ... + a_n) ^ 2
# equals (a_1 ^ 2 + a_2 ^ 2 + ... + a_n ^ 2)
# plus the sum over terms 2 * a_i * a_j, where i < j

total = 0
for i in range(1, 101):
  for j in range(1, 101):
    if i != j:
      total += i * j
print(total)

# SOLUTION:
# 25164150

#~~~~~~ PROBLEM 7 ~~~~~~~~

from math import sqrt
def is_prim(num):
  num = abs(num)
  if num <= 1:
    return False
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

count = 0
i = 1
while count < 10001:
  i +‎ = 1
  if is_prim(i):
    count += 1
print(i)

# SOLUTION:
# 104743

#~~~~~~ PROBLEM 8 ~~~~~~~~

s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

N = len(s)
best = 0
for i in range(N - 13):
  prod = 1
  for j in range(13):
    prod *= int(s[i + j])
  best = max(best, prod)
print(best)

# SOLUTION:
# 23514624000

#~~~~~~ PROBLEM 9 ~~~~~~~~

from math import sqrt
for i in range(500):
  for j in range(i + 1, 500):
      x = i ** 2 + j ** 2
	    # check to see if x is a perfect square
      if int(sqrt(x)) ** 2 == x:
        k = int(sqrt(x))
        if i + j + k == 1000:
          print(i * j * k)

# SOLUTION:
# 31875000
# Note, the triple (i, j, k) giving the solution is (200, 375, 425)

#~~~~~~ PROBLEM 10 ~~~~~~~~

from math import sqrt
def is_prim(num):
  x = abs(num)
  if x <= 1:
    return False
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

total = 0
for i in range(2, 2000000):
  if is_prim(i):
    total += i
print(total)

# SOLUTION:
# 142913828922
