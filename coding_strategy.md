# Python interview loop templates for arrays and strings

## The core question

### What is the candidate answer?

(what you’ll enumerate in brute force)

- Element (one index i or value x)
- Pair (two indices i, j)
- Range (two boundaries L, R for a contiguous subarray/substring)
- Split point (one index i separating left/right)
- Match across two lists (alignment between A and B)
- Subset (any combination of elements, include/skip each element)

Once you name the candidate, brute force becomes: enumerate candidates + check condition + keep best/return.

⸻

1 - Candidate = element (one loop)

Use when: max/min, count, transform, find first/last satisfying condition

```python
def solve(nums):
    best = None
    for x in nums:
        # update best / count / build output
        pass
    return best
```

Example problem: “Find the maximum value”

- Input: [3, -1, 7, 2]
- Output: 7
- Naive loop: scan once, keep best

Another common one: “Count how many are > 0”

- Input: [-2, 0, 4, 5]
- Output: 2

Common upgrades

- membership: seen = set()
- counting: from collections import Counter or counts = {}

⸻

2 - Candidate = pair (two loops)

Use when: “any two”, “two sum”, compare every pair

```python
def solve(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]  # or True
    return None  # or False
```

Example problem: “Two sum (existence)”

- Input: nums = [2, 7, 11, 15], target = 9
- Output: True (or indices [0,1] depending on version)
- Naive loop: try all (i, j) pairs

Another common one: “Find all pairs with difference k”

- Input: nums = [1, 5, 3, 4, 2], k = 2
- Output: [(1,3), (5,3), (4,2)] (format varies)

Upgrade: hash map (Two Sum template)

```python
def solve(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return None
```

⸻

3 - Candidate = range (L, R) contiguous subarray/substring

Use when: “subarray/substring”, “contiguous”, best/exists over a window

3A) Enumerate all ranges (O(n^2))

```python
def solve(nums):
    n = len(nums)
    for L in range(n):
        for R in range(L, n):
            sub = nums[L:R+1]
            # check sub or compute something
            pass
```

3B) Range sum brute force without 3rd loop (O(n^2))

```python
def solve(nums):
    n = len(nums)
    for L in range(n):
        total = 0
        for R in range(L, n):
            total += nums[R]  # sum(nums[L:R+1])
            # check/update with total
            pass
```

Example problem: “Maximum subarray sum”

- Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
- Output: 6 (subarray [4, -1, 2, 1])
- Naive loops: all L, R ranges, compute sum (third loop) or reuse running sum

Another common one: “Does any subarray sum to k?”

- Input: nums = [1, 2, 3], k = 5
- Output: True (subarray [2,3])

Upgrade 1: Prefix sums (range sums / subarray sum = k)

```python
def solve(nums, k):
    prefix = 0
    seen = {0: 1}  # prefix_sum -> count
    ans = 0
    for x in nums:
        prefix += x
        ans += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return ans
```

Upgrade 2: Sliding window (variable)
Use when constraint is based on counts/unique/at most k (not arbitrary negatives + sum constraints).

```python
def solve(nums):
    left = 0
    # state = ...
    best = 0
    for right, x in enumerate(nums):
        # add x to state

        while False:  # window invalid -> shrink
            # remove nums[left] from state
            left += 1

        best = max(best, right - left + 1)
    return best
```

⸻

4 - Candidate = split point i (before/after)

Use when: pivot index, partitioning, left vs right comparisons

Brute force split (slow but clear)

```python
def solve(nums):
    n = len(nums)
    for i in range(n):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1
```

Example problem: “Find pivot index”

- Input: [1, 7, 3, 6, 5, 6]
- Output: 3 (left sum 1+7+3=11, right sum 5+6=11)
- Naive loop: for each split i, compare sum of left vs sum of right

Another common one: “Best time to buy and sell stock (one transaction)”

- Input: [7, 1, 5, 3, 6, 4]
- Output: 5 (buy at 1, sell at 6)
- Split thinking: choose sell day, track min before it (or brute force all buy/sell)

Upgrade split (one pass)

```python
def solve(nums):
    total = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        right_sum = total - left_sum - x
        if left_sum == right_sum:
            return i
        left_sum += x
    return -1
```

⸻

5 - Candidate = match across two lists

Use when: intersection, merge, compare sorted lists

5A) Brute force match (O(n*m))

```python
def solve(A, B):
    out = []
    for x in A:
        for y in B:
            if x == y:
                out.append(x)
    return out
```

5B) Two pointers if sorted (O(n+m))

```python
def solve(A, B):
    i = j = 0
    out = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            out.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return out
```

5C) Set/Counter if unsorted

```python
from collections import Counter

def solve(A, B):
    cb = Counter(B)
    out = []
    for x in A:
        if cb[x] > 0:
            out.append(x)
            cb[x] -= 1
    return out
```

Example problem: “Intersection of two arrays”

- Input: A = [1, 2, 2, 3], B = [2, 2]
- Output: [2, 2] (or [2] if unique intersection version)
- Naive approach: for each element in A, search in B (two loops)
- Efficient: sort + two pointers, or hash counts

Another common one: “Merge two sorted lists”

- Input: A = [1, 3, 7], B = [2, 3, 10]
- Output: [1, 2, 3, 3, 7, 10]
- Two pointers: classic merge step

⸻

6 - Candidate = subset (any combination)

Use when: “any combination”, “subset”, “pick some elements”, “can we choose numbers to sum to…”, “partition”, “can form target”

Key distinction

- Contiguous language (“subarray”, “substring”, “window”, “consecutive”) → candidate is a range (L, R)
- Combination language (“any combination”, “pick any”, “subset”) → candidate is a subset (include/skip)

Quick sanity check (60 seconds)

Ask: “Can the valid solution skip elements?”
- If yes, a window/range approach is likely wrong.
- Make a tiny counterexample to prove it.

Example problem: “Array Addition / subset sum to target (exclude largest)”

- Input: [12, 1, 2, 5, 9]
- Target: 12
- Valid subset: 1 + 2 + 9 = 12 (skips 5)
- A contiguous window on the sorted list will miss this.

Brute force (include/skip recursion)

```python
# Outline only
# dfs(i, current_sum): at index i, either include nums[i] or skip it
# stop early if current_sum == target
```

Brute force (bitmask subsets)

```python
# Outline only
# for mask in range(2^n): sum elements where bit is set
```

Upgrade 1: DP of reachable sums (set)

```python
# Outline only
# reachable = {0}
# for x in nums: reachable |= {s + x for s in reachable}
```

Upgrade 2: prune when possible

- If all remaining numbers are non-negative: if current_sum > target, you can stop exploring that branch.
- If negatives exist: pruning is trickier; prefer dynamic programming (DP)-set or still do Depth First Search (DFS) without that prune.

Interview “pivot” line (use this when you realize you picked the wrong pattern)

- “My current approach assumes contiguity (a window). The prompt allows skipping elements, so I need a subset include/skip approach.”

⸻

Fast “upgrade picker” (what brute force is wasting time on)

- repeated membership checks → set / dict
- repeated range sums → prefix sums
- repeated contiguous scanning with a constraint → sliding window
- sorted structure / monotonic movement → two pointers
- in-place remove/filter/move → fast/slow pointer
- nesting / most recent open → stack

⸻

20-second solving routine

1. Read for keywords that imply contiguity vs combination
   - “subarray/substring/window/consecutive” → range candidate (L, R)
   - “any combination/subset/pick some” → subset candidate (include/skip)
2. Name the candidate (element / pair / range / split / match / subset)
3. Write the brute-force skeleton (even if slow)
4. Check with a tiny example and one counterexample that would break the wrong pattern
5. Identify repeated work (membership, sums, scanning)
6. Swap in the upgrade (set/map, prefix, window, pointers, DP set)
7. Edge cases: empty, 1 item, duplicates, negatives, no answer

## RBCES

Order it so you recognize first, then brute force.

R — Read and restate

- Say it in your own words.
- Identify input → output and what “valid” means.

B — Build a naive method (mechanical)
Use one of these “naive generators” (pick the first that fits):

1. Enumerate all possibilities

   - Pairs → nested loops over i, j
   - Triplets → 3 loops
   - Subarrays → loops over L, R
   - Subsequences → recursion/bitmask (usually too big but it’s still a baseline)
   - Subsets (“any combination”) → recursion include/skip or bitmask (baseline for subset-sum style problems)

2. Simulate the definition literally

   - “Do exactly what the problem statement says,” step-by-step.
   - Example: intersection → “for each in A, check if it appears in B”

3. Sort then compare

   - Sorting is a brute-force-ish “structure maker” that often gives you a correct approach even if not optimal.

If you can do any one of these, you have a brute force.

C — Check with a tiny example

- Run your naive idea on a 5-element example by hand.
- Catch mistakes before code.

E — Efficient upgrade
Now ask: “What repeated work did brute force do?”

- Rechecking membership → use a set/map
- Re-summing ranges → prefix sums
- Re-scanning overlaps → two pointers / sliding window

S — Sanity/edges

- empty, 1 item, duplicates, negatives, whitespace, no answer


⸻

When you’re stuck in an interview (no hints)

- Say the brute force out loud first (even if it’s slow). This buys time and shows structured thinking.
- If you can’t finish brute force, at least write the enumeration skeleton and talk through correctness.
- If your approach is failing, pivot early:
  - “This approach assumes X. A counterexample is Y. So I should use Z.”

Counterexample prompts you can use quickly

- “Can the solution skip elements?” (subset vs range)
- “What if duplicates exist?” (counts vs set)
- “What if negatives exist?” (sliding window pitfalls, pruning limits)
- “What if the answer is empty/no solution?”
