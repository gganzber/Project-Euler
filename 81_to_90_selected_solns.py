# ~~~~~~ PROBLEM 81 ~~~~~~~~

# Save the 80 x 80 grid of numbers as a list of lists called grid.
# We solve the problem using dynamic programming as follows.

has_cache = [[False] * 80 for _ in range(80)]
cache = [[None] * 80 for _ in range(80)]

def walk(i, j):
    if i >= 80 or j >= 80:
        return 10 ** 20
    if i == 79 and j == 79:
        return grid[i][j]

    if has_cache[i][j]:
        return cache[i][j]
    has_cache[i][j] = True
    cache[i][j] = grid[i][j] + min(walk(i + 1, j), walk(i, j + 1))
    return cache[i][j]

print(walk(0, 0))

# SOLUTION:
# 427337

# ~~~~~~ PROBLEM 82 ~~~~~~~~

# save the 80 x 80 list of lists of integers as grid
from collections import deque

# best[i][j] will store the minimal value path sum from some node indexed k,0 the grid to the node indexed i,j
best = [[10 ** 20] * 80 for _ in range(80)]
for i in range(80):
    best[i][0] = grid[i][0]
directions = [(1,0), (0,1), (-1,0)]

q = deque()
for i in range(80):
    q.append((i, 0, grid[i][0]))

while len(q) > 0:
    x, y, curr = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 80 and 0 <= ny < 80:
            if curr + grid[nx][ny] < best[nx][ny]:
                best[nx][ny] = curr + grid[nx][ny]
                q.append((nx, ny, curr + grid[nx][ny]))
              
# the solution is the minimal value path sum from some node indexed k,0 to another node indexed i,79
best_soln = 10 ** 20
for i in range(80):
    best_soln = min(best_soln, best[i][79])
print(best_soln)

# SOLUTION:
# 260324

# ~~~~~~ PROBLEM 83 ~~~~~~~~

# save the 80 x 80 list of lists of integers as grid from collections import deque
# best[i][j] will store the minimal value path sum from the node indexed 0,0 the grid to the node indexed i,j

best = [[10 ** 20] * 80 for _ in range(80)]
best[0][0] = grid[0][0]
directions = [(1,0), (0,1), (-1,0), (0,-1)]

q = deque()
q.append((0, 0, grid[0][0]))

while len(q) > 0:
    x, y, curr = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 80 and 0 <= ny < 80:
            if curr + grid[nx][ny] < best[nx][ny]:
                best[nx][ny] = curr + grid[nx][ny]
                q.append((nx, ny, curr + grid[nx][ny]))
              
# the solution is the minimal value path sum from the node indexed 0,0 to the node indexed 79,79
print(best[79][79])

# SOLUTION:
# 425185

# ~~~~~~ PROBLEM 85 ~~~~~~~~

# counts the number of subrectangles of a rectangle with side lengths
# positive integers m and n
def count_rects(m, n):
    total = 0
    for i in range(m):
        for j in range(n):
            total += (m - i) * (n - j)
    return total

best = 2 * (10 ** 6)
best_coords = (0, 0)

for i in range(2000):
    for j in range(2000):
        # to improve run-time, we discard pairs which can't be optimal
        if i * j > 3000:
            continue
        else:
            if abs(2000000 - count_rects(i, j)) < best:
                best = abs(2000000 - count_rects(i, j))
                best_coords = (i, j)
print(best_coords)

# SOLUTION:
# 36 * 77 = 2772

# ~~~~~~ PROBLEM 87 ~~~~~~~~

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
    if not lst[i]:
        prims.append(i)

sqrs = []
cubes = []
quads = []

for elt in prims:
    a, b, c, lim = elt ** 2, elt ** 3, elt ** 4, 5 * (10 ** 7)
    if a > lim:
        break
    sqrs.append(a)
    if b <= lim:
        cubes.append(b)
    if c <= lim:
        quads.append(c)

s = set()
lim = 5 * (10 ** 7)

for a in sqrs:
    for b in cubes:
        for c in quads:
            if a + b + c <= lim:
                s.add(a + b + c)
print(len(s))

# SOLUTION:
# 1097343

# ~~~~~~ PROBLEM 89 ~~~~~~~~

# First save the given list of strings of Roman numerals as a list of strings lst.

# Counts the length of the optimal way of writing the integer num in Roman numerals
def int_to_roman_len(num):
    total = 0
    # For the purposes of this problem, MMMM is the optimal way of writing 4000, not bold IV.
    if num >= 4000:
        total += 2
    while num > 0:
        x = num % 10
        if x == 9:
            total += 2
        elif x >= 5:
            total += x % 5 + 1
        elif x == 4:
            total += 2
        else:
            total += x
        num //= 10
    return total

# Takes a given string, (perhaps sub-optimally) written in Roman numerals, and converts it into its corresponding integer
def roman_str_to_num(s):
    total = 0
    d = {"M" : 1000, "D": 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    N = len(s)
    index = 0
    while index < N:
        if index < N - 1:
            if s[index] == "C" and s[index + 1] == "M":
                total += 900
                index += 2
                continue
            elif s[index] == "C" and s[index + 1] == "D":
                total += 400
                index += 2
                continue
            elif s[index] == "X" and s[index + 1] == "C":
                total += 90
                index += 2
                continue
            elif s[index] == "X" and s[index + 1] == "L":
                total += 40
                index += 2
                continue
            elif s[index] == "I" and s[index + 1] == "X":
                total += 9
                index += 2
                continue
            elif s[index] == "I" and s[index + 1] == "V":
                total += 4
                index += 2
                continue
            else:
                total += d[s[index]]
                index += 1
        else:
            total += d[s[index]]
            index += 1
            
    return total

count = 0
# count the number of letters saved by writing each elt in lst in its optimal Roman numeral form
for elt in lst:
    N = len(elt)
    num = roman_str_to_num(elt)
    count += N - int_to_roman_len(num)
print(count)

# SOLUTION:
# 743
