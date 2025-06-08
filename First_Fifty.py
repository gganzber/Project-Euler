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

#~~~~~~ PROBLEM 11 ~~~~~~~~

lst = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95], [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57], [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40], [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36], [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16], [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

best = 0
for i in range(20):
  for j in range(20):
    a, b, c, d = 0, 0, 0, 0
    if i < 17:
      a = lst[i][j] * lst[i + 1][j] * lst[i + 2][j] * lst[i + 3][j]
    if j < 17:
      b = lst[i][j] * lst[i][j + 1] * lst[i][j + 2] * lst[i][j + 3]
    if i < 17 and j < 17:
      c = lst[i][j] * lst[i + 1][j + 1] * lst[i + 2][j + 2] * lst[i + 3][j + 3]
    if i < 17 and j > 2:
      d = lst[i][j] * lst[i + 1][j - 1] * lst[i + 2][j - 2] * lst[i + 3][j - 3]
    best = max(best, a, b, c, d)
print(best)

#SOLUTION:
#70600674
