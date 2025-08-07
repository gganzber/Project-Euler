# ~~~~~~ PROBLEM 91 ~~~~~~~~

# idea:
# set P = (0,0)
# loop over all pairs of points Q = (i, j), R = (k, s) for 0 <= i,j,k,s <= 50
# make sure P, Q, R aren't collinear (which would happen if i * n == k and j * n == s or k * n == i and s * n == j for some integer n >= 1)
# Also make sure Q, R aren't (0, 0)
# then add to total if for side lengths x, y, z we have x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2
# then divide total by 2, since we've double counted.

# Now, if Q = (i, j), the square of the side length PQ is i ** 2 + j ** 2
# and the square of the side length PR is k ** 2 + s ** 2
# Finally the square of the side length QR is (k - i) ** 2 + (s - j) ** 2

total = 0
for i in range(51):
    for j in range(51):
        # make sure (i,j) isn't (0,0)
        if i == 0 and j == 0:
            continue
        for k in range(51):
            for s in range(51):
                # make sure (k,s) isn't (0,0)
                if k == 0 and s == 0:
                    continue

                yes = True
                # make sure (0,0), (i,j) and (k,s) aren't collinear
                for x in range(51):
                    if (x * i == k and x * j == s) or (x * k == i and x * s == j):
                        yes = False
                        break

                if not yes:
                    continue
    
                a, b, c = i ** 2 + j ** 2, k ** 2 + s ** 2, (k - i) ** 2 + (s - j) ** 2

                # check to see if P,Q,R form a right angle triangle
                if (a + b == c) or (a + c == b) or (b + c == a):
                    total += 1

print(total)
# 28468

# SOLUTION:
# 28468 // 2 = 14234

# Note we can actually speed up the runtime when checking if P, Q, and R are collinear,
# at the expense of making the code less terse, as follows:
                
                # make sure (0,0), (i,j) and (k,s) aren't collinear
                #if i != 0:
                #    n = k // i
                #else:
                #    n = s // j
                #if i * n == k and j * n == s:
                #    yes = False
                #if k != 0:
                #    n = i // k
                #else:
                #    n = j // s
                #if k * n == i and s * n == j:
                #    yes = False

                #if not yes:
                #    continue

# ~~~~~~ PROBLEM 92 ~~~~~~~~

ones = set()
eightynines = set()
ones.add(1)
eightynines.add(89)

def chain(num):
    lst = [num]
    while num not in ones and num not in eightynines:
        total = 0
        while num > 0:
            total += (num % 10) ** 2
            num //= 10
        num = total
        lst.append(num)
    if num in ones:
        for elt in lst:
            ones.add(elt)
        return 0
    else:
        for elt in lst:
            eightynines.add(elt)
        return 1

total = 0

for i in range(1, 10 ** 7):
    total += chain(i)
print(total)

# SOLUTION:
# 8581146

# ~~~~~~ PROBLEM 95 ~~~~~~~~

# d[num] will equal the sum of all the proper divisors of num. We'll set d[1] = 1 as the only exception.
d = {}

for i in range(1, 10 ** 6 + 1):
    d[i] = 1

lst = [False] * (10 ** 6 + 1)
lst[0], lst[1] = True, True

for i in range(2, 10 ** 6 + 1):
    x = i + i
    while x < 10 ** 6 + 1:
        d[x] += i
        x += i

best_val = 0
best_num = 0

# If num forms an amicable chain, returns the length of that chain, else returns 0
def amicable(num):
    start = num
    seen = set()
    while num not in seen:
        if num > 10 ** 6:
            return 0
        seen.add(num)
        num = d[num]
        if num == start:
            return len(seen)
    return 0

for i in range(2, 10 ** 6):
    x = amicable(i)
    if x > best_val:
        best_val = x
        best_num = i

# best_num stores an integer which forms part of an amicable chain of maximal length described in the problem.
# By construction, since we are looping upward for i increasing, this must be the smallest such
# integer to form part of a chain of such length. Therefore the solution is:
print(best_num)

# SOLUTION:
# 14316

# ~~~~~~ PROBLEM 97 ~~~~~~~~

# Using the arithmetic properties of exponents and reducing
# mod 10 ** 10 after each calculation, since we are only
# interested in the last 10 digits of the given expression, gives:

x = (2 ** 100) % (10 ** 10)
y = (2 ** 57) % (10 ** 10)

ans = (x * y * 28433) % (10 ** 10)
for _ in range(78303):
    ans = (ans * x) % (10 ** 10)

ans = (ans + 1 % (10 ** 10))
print(ans)

# SOLUTION:
# 8739992577

# ~~~~~~ PROBLEM 99 ~~~~~~~~

# save the list of 1000 pairs as a list of tuples named lst

best = lst[0]
best_index = 0

# for positive integers a,b,c,d, a ** b < c ** d if and only if a < c ** (d/c)
# and for large numbers a, b, c, d, the second equation is much more efficient to compute

for i in range(1, 1000):
    a, b = best[0], best[1]
    c, d = lst[i][0], lst[i][1]
    if a < c ** (float(d) / float(b)):
        best = lst[i]
        best_index = i

# add one, since the solution is 1-indexed and lst is 0-indexed
print(best_index + 1)

# SOLUTION:
# 709
