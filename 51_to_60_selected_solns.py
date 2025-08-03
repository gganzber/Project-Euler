# ~~~~~~ PROBLEM 51 ~~~~~~~~

# Generate all primes with at most 7 digits
lst = [True] * (10 ** 7)
lst[0], lst[1] = False, False
for i in range(2, 10 ** 7):
    if lst[i] == True:
        x = i + i
        while x < 10 ** 7:
            lst[x] = False
            x += i
prims = []
for i in range(10 ** 7):
    if lst[i] == True:
        prims.append(i)

s = set(prims)
def replace_count(num):
    best = 0
    st = str(num)
    N = len(st)
    for x in range(1, 2 ** N):
        total = 0
        b = bin(x)[::-1]
        # the variable yes will be True if the number nums is part of the family of primes
        yes = False
        for i in range(10):
            l = list(st)
            for index, elt in enumerate(b):
                if elt == "b":
                    break
                elif elt == "1":
                    l[index] = str(i)
            if l[0] != "0" and int("".join(l)) in s:
                total += 1
            if int("".join(l)) == num:
                yes = True
        if yes:
            best = max(best, total)
    return best

for elt in prims:
    if replace_count(elt) == 8:
        print(elt)
        break
# SOLUTION:
# 121313

# ~~~~~~ PROBLEM 53 ~~~~~~~~

def rising_fact(a, b):
  prod = 1
  for i in range(b, a + 1):
    prod *= i
  return prod

def choose(n, k):
  if k == 0 or k == n:
    return 1
  return rising_fact(n, k + 1) // rising_fact(n - k, 1)

total = 0
for i in range(1, 101):
  for j in range(i + 1):
    if choose(i, j) > 1000000:
      total += 1
print(total)

# SOLUTION:
# 4075

# ~~~~~~ PROBLEM 54 ~~~~~~~~

from collections import Counter

card_rank = {}
for i in range(2, 10):
    card_rank[str(i)] = i
card_rank["T"] = 10
card_rank["J"] = 11
card_rank["Q"] = 12
card_rank["K"] = 13
card_rank["A"] = 14

def rank_hand(str):
    cards = "23456789TJQKA"
    suits = "CDHS"
    card_count = Counter()
    suits_count = Counter()
    c = []
    for elt in str:
        if elt in cards:
            card_count[elt] += 1
            c.append(elt)
        elif elt in suits:
            suits_count[elt] += 1

    c.sort(key = lambda x : card_rank[x])
    yes = True
    for i in range(4):
        if card_rank[c[i + 1]] - card_rank[c[i]] != 1:
            yes = False

    if len(suits_count) == 1:
        if c == ["T", "J", "Q", "K", "A"]:
            return 10
        else:
            if yes:
                return 9
            else:
                return 6   
    
    if sorted(list(card_count.values())) == [1, 4]:
        return 8

    if sorted(list(card_count.values())) == [2, 3]:
        return 7

    if yes:
        return 5 

    if sorted(list(card_count.values())) == [1, 1, 3]:
        return 4

    if sorted(list(card_count.values())) == [1, 2, 2]:
        return 3

    if sorted(list(card_count.values())) == [1, 1, 1, 2]:
        return 2
    
    return 1


from collections import Counter
def compare_hands(s1, s2):
    if rank_hand(s1) > rank_hand(s2):
        return 1
    elif rank_hand(s1) < rank_hand(s2):
        return 0
    else:
        cards = "23456789TJQKA"
        c1 = []
        c2 = []
        count1 = Counter()
        count2 = Counter()
        for elt in s1:
            if elt in cards:
                c1.append(elt)
                count1[elt] += 1
        for elt in s2:
            if elt in cards:
                c2.append(elt)
                count2[elt] += 1
        c1.sort(key = lambda x : (count1[x], card_rank[x]))
        c2.sort(key = lambda x : (count2[x], card_rank[x]))

        for i in range(5):
            if card_rank[c1[-i-1]] > card_rank[c2[-i-1]]:
                return 1
            elif card_rank[c1[-i-1]] < card_rank[c2[-i-1]]:
                return 0
        print("Error", s1, s2)

# Save the list of hands as a string lst. Then save the hands as a list of strings, new_lst
new_lst = []
curr = 0
for _ in range(1000):
    new_lst.append(lst[curr:curr + 29])
    curr += 30

total = 0
for s in new_lst:
    total += compare_hands(s[:15], s[15:])
print(total)

# SOLUTION:
# 376

# ~~~~~~ PROBLEM 55 ~~~~~~~~

def is_pal(num):
  s = str(num)
  N = len(s)
  for i in range(N // 2):
    if s[i] != s[-i-1]:
      return False
  return True

def lychrel(num):
  for _ in range(50):
    s = str(num)
    new = num + int(s[::-1])
    if is_pal(new):
      return False
    num = new
  return True

total = 0
for i in range(10000):
  if lychrel(i):
    total += 1
print(total)

# SOLUTION:
# 249

# ~~~~~~ PROBLEM 56 ~~~~~~~~

def dig_sum(num):
  s = str(num)
  total = 0
  for letter in s:
    total += int(letter)
  return total

best = 0
for a in range(1, 100):
  for b in range(1, 100):
    best = max(best, dig_sum(a ** b))
print(best)

# SOLUTION:
# 972

total = 0

# ~~~~~~ PROBLEM 57 ~~~~~~~~

for n in range(1, 1001):
    a, b = 1, 2

    for i in range(1, n):
        a, b = b, a + 2 * b
    
    a, b = a + b, b
    s1, s2 = str(a), str(b)
    if len(s1) > len(s2):
        total += 1
print(total)

# SOLUTION:
# 153

# ~~~~~~ PROBLEM 58 ~~~~~~~~

from math import sqrt
def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

total = 1
total_prims = 0
add = 3
incr = 2
while total == 1 or total_prims * 10 >= total:
    for i in range(4):
        if is_prim(add + i * incr):
            total_prims += 1
    total += 4
    add +=  4 * incr + 2
    incr += 2
print(incr - 1)

# SOLUTION:
# 26241

# ~~~~~~ PROBLEM 59 ~~~~~~~~

# save the list of integers given as lst

best = 0
best_triple = (0, 0, 0)

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            total = 0
            new_lst = lst[:]
            N = len(new_lst)
            for index in range(N):
                if index % 3 == 0:
                    new_lst[index] ^= i
                elif index % 3 == 1:
                    new_lst[index] ^= j
                else:
                    new_lst[index] ^= k
            # we count to see which key produces the most occurences of the word "the" in the decyrpted text
            for index in range(N - 2):
                if new_lst[index] == 116:
                    if new_lst[index + 1] == 104:
                        if new_lst[index + 2] == 101:
                            total += 1
                            
            if total > best:
                best = total
                best_triple = (i, j, k)
print(best_triple)

# Best triple is i = 101, j = 120, k = 112

ans = []

new = lst[:]
N = len(new)
for i in range(N):
    if i % 3 == 0:
        new[i] ^= 101
    elif i % 3 == 1:
        new[i] ^= 120
    else:
        new[i] ^= 112
# for elt in new:
#    ans.append(chr(elt))

# print("".join(ans))
# this verifies the key we found indeed decrypts the message

# the answer is therefore
print(sum(new))

# SOLUTION:
# 129448
