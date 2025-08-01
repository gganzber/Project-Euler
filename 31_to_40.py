# ~~~~~~ PROBLEM 31 ~~~~~~~~

l2 = [2 * x for x in range(101)]
l3 = [5 * x for x in range(41)]
l4 = [10 * x for x in range(21)]
l5 = [20 * x for x in range(11)]
l6 = [50 * x for x in range(5)]
l7 = [0, 100, 200]

# we start with a total of 1, because there is one unique way to make $2, including a $2 bill.
total = 1

# Making $2 in change with the given bills and coins is equivalent to making any amount less than #or equal to $2 in change and making up the rest with pennies.
# Using this observation, we reduce the time complexity of the task by a multiple of 200
# which is the size of l1 = [x for x in range(201)]

for x2 in l2:
    for x3 in l3:
        for x4 in l4:
            for x5 in l5:
                for x6 in l6:
                    for x7 in l7:
				                # the below sum represents making a number less than or equal to 200 in change using
				                # x2 dollars worth of 2 cent coins, x3 dollars worth of 5 cent coins, etc.
                        if x2 + x3 + x4 + x5 + x6 + x7 <= 200:
                            total += 1
print(total)

# SOLUTION:
# 73682

# ~~~~~~ PROBLEM 32 ~~~~~~~~

used = set()
total = 0
for i in range(1000):
    for j in range(i + 1, 10000):
        x = i * j
        a = str(i) + str(j) + str(x)
        if len(a) != 9 or x in used:
            continue
        if "".join(sorted(a)) == "123456789":
            total += x
            used.add(x)
print(total)

# SOLUTION:
# 45228

# ~~~~~~ PROBLEM 33 ~~~~~~~~

def curious(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    if s1[0] == s2[0] and s1[1] == s2[1]:
        return False
    if s1[1] == "0" and s2[1] == "0":
        return False
    if s1[0] != s2[0] and s1[0] != s2[0] and s1[1] != s2[0] and s1[1] != s2[1]:
        return False
    if s1[0] == s2[0]:
        return num2 * int(s1[1]) == num1 * int(s2[1])
    elif s1[0] == s2[1]:
        return num2 * int(s1[1]) == num1 * int(s2[0])
    elif s1[1] == s2[0]:
        return num2 * int(s1[0]) == num1 * int(s2[1])
    else:
        # if s1[1] == s2[1]:
        return num2 * int(s1[0]) == num1 * int(s2[0])

ans = []
for i in range(10, 101):
    for j in range(i + 1, 101):
        if curious(i, j):
            ans.append((i, j))
print(ans)

[(16, 64), (19, 95), (26, 65), (49, 98)]

# in lowest terms this gives the product
# (1 / 4) * (1 / 5) * (2 / 5) * (1 / 2) = 1 / 100
# so the answer is the denominator, 100.

# SOLUTION:
# 100

# ~~~~~~ PROBLEM 34 ~~~~~~~~

# The factorial of a number num >= 0
def fact(num):
    prod = 1
    for i in range(2, num + 1):
        prod *= i
    return prod

# Note we only have to check up to 3 * (10 ** 6), since for any number with 7 digits, the maximal
# sum of the factorial of its digits arises if all the digits are 9. Now 7 * 9! = 2540160, so the sum of
# the factorial of the digits of a 7 - digit number can never exceed 3000000.
# A simple induction proof shows that 9! * n < 10 ** (n - 1) for all n >= 8, so the sum of the factorials
# of the digits of any n-digit number can never equal the number itself, for n >= 8.

total = 0
for i in range(3, 3000000):
    count = 0
    s = str(i)
    for elt in s:
        count += fact(int(elt))
    if count == i:
        total += i
print(total)

# SOLUTION:
# 40730

# ~~~~~~ PROBLEM 35 ~~~~~~~~

# Label the non-prime indices below 10 ^ 6 as True
lst = [False] * (10 ** 6)
lst[0], lst[1] = True, True
for i in range(2, 10 ** 6):
  if lst[i] == False:
    x = i
    while x + i < 10 ** 6:
        x += i
        lst[x] = True

total = 0
for i in range(2, 1000000):
    s = str(i)
    N = len(s)
    yes = True
    for j in range(N):
        if lst[int(s[j:] + s[:j])] == True:
            yes = False
            break
    if yes:
        total += 1
print(total)

# SOLUTION:
# 55

# ~~~~~~ PROBLEM 36 ~~~~~~~~

# Return true if and only if a string s is a palindrome
def pal(s):
    N = len(s)
    for i in range(N // 2):
        if s[i] != s[-i-1]:
            return False
    return True

total = 0
for i in range(1, 10 ** 6):
    if pal(str(i)):
        if pal(bin(i)[2:]):
            total += i
print(total)

# SOLUTION:
# 872187

# ~~~~~~ PROBLEM 37 ~~~~~~~~

# Label the non-prime indices below 10 ^ 6 as True
lst = [False] * (10 ** 6)
lst[0], lst[1] = True, True
for i in range(2, 10 ** 6):
  if lst[i] == False:
    x = i
    while x + i < 10 ** 6:
        x += i
        lst[x] = True

def trunc(num):
    s = str(num)
    N = len(s)
    yes = True
    for j in range(N):
        if lst[int(s[j:])] == True:
            yes = False
            break
        if lst[int(s[:j + 1])] == True:
            yes = False
            break
    return yes

total = 0
count = 0
for i in range(11, 10 ** 6):
    if trunc(i):
        total += i
        count += 1
        if count == 11:
            break
print(total)

# SOLUTION:
# 748317

# ~~~~~~ PROBLEM 38 ~~~~~~~~

def pan(num):
    s1 = str(num)
    s2 = str(2 * num)
    if len(s1 + s2) == 9:
        if "".join(sorted(s1 + s2)) == "123456789":
            return int(s1 + s2)
    s3 = str(3 * num)
    if len(s1 + s2 + s3) == 9:
        if "".join(sorted(s1 + s2 + s3)) == "123456789":
            return int(s1 + s2 + s3)
    s4 = str(4 * num)
    if len(s1 + s2 + s3 + s4) == 9:
        if "".join(sorted(s1 + s2 + s3 + s4)) == "123456789":
            return int(s1 + s2 + s3 + s4)
    s5 = str(5 * num)
    if len(s1 + s2 + s3 + s4 + s5) == 9:
        if "".join(sorted(s1 + s2 + s3 + s4 + s5)) == "123456789":
            return int(s1 + s2 + s3 + s4 + s5)
    return 0

best = 0
# We only need to check up to 50000, since x * 2 has >= 6 digits for any x >= 50000
# so the concatenation of x with x * 2 has greater than 10 digits
for i in range(1, 50000):
    x = pan(i)
    if x > best:
        best = x
print(best)

# SOLUTION:
# 932718654

# ~~~~~~ PROBLEM 39 ~~~~~~~~

from math import sqrt
ans = [0] * 1001
sqrs = set()
i = 1
while i * i < 1000000:
    sqrs.add(i * i)
    i += 1
for i in range(1001):
    for j in range(i, 1001):
        k = i ** 2 + j ** 2
        if k in sqrs:
            if i + j + int(sqrt(k)) <= 1000:
                ans[i + j + int(sqrt(k))] += 1
M = max(ans)
for i in range(1001):
    if ans[i] == M:
        print(i)

# SOLUTION:
# 840

# ~~~~~~ PROBLEM 40 ~~~~~~~~

curr = 1
lst = []
# digs represents the number of digits in the fraction part by concatenating the numbers 1 to curr - 1.
digs = 0
while digs < 1000000:
    s = str(curr)
    lst.append(s)
    digs += len(s)
    curr += 1
w = "".join(lst)
x = int(w[0]) * int(w[9]) * int(w[99]) * int(w[999]) * int(w[9999]) * int(w[99999]) * int(w[999999])
print(x)

# SOLUTION:
# 210
