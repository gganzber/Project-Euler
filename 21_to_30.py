# ~~~~~~ PROBLEM 21 ~~~~~~~~

def proper_divs(num):
  total = 0
  for i in range(1, num // 2 + 1):
    if num % i == 0:
      total += i
  return total

total = 0
for i in range(10000):
  if proper_divs(proper_divs(i)) == i:
    if proper_divs(i) != i:
      total += i
print(total)

# SOLUTION:
# 31626

# ~~~~~~ PROBLEM 22 ~~~~~~~~

# Store the list of strings of names as lst

lst.sort()
total = 0

def name_score(name):
    score = 0
    for elt in name:
        score += ord(elt) - 64
    return score

N = len(lst)
for i in range(N):
    total += name_score(lst[i]) * (i + 1)
print(total)

# SOLUTION:
# 871198282

# ~~~~~~ PROBLEM 23 ~~~~~~~~

# Returns True if num is an abundant number, False otherwise
def abundant(num):
    total = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            total += i
    return total > num

# The set of all abundant numbers below 28124
s = set()
for i in range(12, 28124):
    if abundant(i):
        s.add(i)

# We mark an index i < 28124 True if it can be expressed as the sum of two abundant numbers
writeable = [False] * 28124
for a in s:
    for b in s:
        if a + b < 28124:
            writeable[a + b] = True

# Sum all numbers less than 28124 that cannot be expressed as the sum of two abundant numbers
total = 0
for i in range(28124):
    if writeable[i] == False:
        total += i
print(total)

# SOLUTION:
# 4179871

# ~~~~~~ PROBLEM 24 ~~~~~~~~

# The factorial of a number num >= 0
def fact(num):
    prod = 1
    for i in range(2, num + 1):
        prod *= i
    return prod

# We use the idea that there are 10 * 9! permutations of the digits 0, 1, ... ,9
# 9! starting with the digit 0, 9! starting with the digit 1, etc.

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ans = []

start = 10 ** 6 - 1
for i in range(9, -1, -1):
    res = start // fact(i) 
    ans.append(digits[res])
    digits.remove(digits[res])
    start -= res * fact(i)
print("".join(ans))

# SOLUTION:
# 2783915460

# ~~~~~~ PROBLEM 25 ~~~~~~~~

index = 1
a, b = 0, 1
while len(str(b)) < 1000:
  a, b, index = b, a + b, index + 1
print(index)

# SOLUTION:
# 4782

# ~~~~~~ PROBLEM 26 ~~~~~~~~

best = 1
best_val = 1
def cycle(num):
    seen = set()
    seen.add(1)
    remainder = 1
    for _ in range(num + 1):
        while remainder < num:
            remainder *= 10
        if remainder in seen or remainder % num == 0:
            return len(seen)
        seen.add(remainder)
        remainder = remainder - (remainder // num) * num

for i in range(2, 1000):
    x = cycle(i)
    if x > best:
        best = x
        best_val = i
print(best_val)

# SOLUTION:
# 983

# ~~~~~~ PROBLEM 27 ~~~~~~~~

from math import sqrt
def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def score(a, b):
    total = 0
    num = 0
    while is_prim(num ** 2 + a * num + b):
        total, num = total + 1, num + 1
    return total

best = 0
best_pair = [-2000, -2000]
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        x = score(a, b)
        if x > best:
            best = x
            best_pair = [a, b]
print(best_pair[0] * best_pair[1])

# SOLUTION:
# -59231

# ~~~~~~ PROBLEM 28 ~~~~~~~~

total = 1
add = 3
incr = 2
while incr < 1001:
    for i in range(4):
        total += add + i * incr
    add +=  4 * incr + 2
    incr += 2
print(total)

# SOLUTION:
# 669171001

# ~~~~~~ PROBLEM 29 ~~~~~~~~

s = set()
for i in range(2, 101):
    for j in range(2, 101):
        s.add(i ** j)
print(len(s))

# SOLUTION:
# 9183

# ~~~~~~ PROBLEM 30 ~~~~~~~~

# Checks if a number num equals the sum of the fifth powers of its digits

def fifth_sum_digs(num):
    s = str(num)
    total = 0
    for elt in s:
        total += int(elt) ** 5
    return num == total

# We only need to check up to 10 ** 6 because for any number with 7 or more digits
# the maximum sum of fifth powers of digits arises if all the digits are 9
# and 9 ** 5 = 59049, and 59049 * n < 10 ** (n - 1) for all n >= 7 (easily proven by induction),
# so no number larger than 10 ** 6 can equal the sum of the fifth powers of its digits.

total = 0
for i in range(2, 1000000):
    if fifth_sum_digs(i):
        total += i
print(total)

# SOLUTION:
# 443839
