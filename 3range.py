'''
3 - Candidate = range (L, R) contiguous subarray/substring

Use when: “subarray/substring”, “contiguous”, best/exists over a window
 “Maximum subarray sum”

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6 (subarray [4, -1, 2, 1])
Naive loops: all L, R ranges, compute sum (third loop) or reuse running sum
'''


def range_subpart_bruteforce_3loops(inarray: list):
    """Maximum subarray (range) using the most literal brute force.

    Enumerate every candidate range (L, R) and compute its sum with a 3rd loop.
    Time: O(n^3), Space: O(1) extra

    Returns: (best_subarray_list, best_sum)
    """
    if not inarray:
        return ([], 0)

    best_sum = float('-inf')
    best_sub = []

    n = len(inarray)
    for L in range(n):
        for R in range(L, n):
            total = 0
            for k in range(L, R + 1):
                total += inarray[k]
            if total > best_sum:
                best_sum = total
                best_sub = inarray[L:R + 1]

    return (best_sub, best_sum)


def range_subpart_2loops_running_sum(inarray: list):
    """Maximum subarray using 2 loops and a running sum.

    For each L, expand R and keep the running sum of inarray[L:R].
    Time: O(n^2), Space: O(1) extra

    Returns: (best_subarray_list, best_sum)
    """
    if not inarray:
        return ([], 0)

    best_sum = float('-inf')
    best_L = 0
    best_R = 0

    n = len(inarray)
    for L in range(n):
        total = 0
        for R in range(L, n):
            total += inarray[R]
            if total > best_sum:
                best_sum = total
                best_L = L
                best_R = R

    return (inarray[best_L:best_R + 1], best_sum)


def range_subpart_kadane(inarray: list):
    """Maximum subarray using Kadane's algorithm (single pass).

    Idea: At each index i, either extend the previous best-ending-here sum,
    or start fresh at i if that is better.

    Time: O(n), Space: O(1) extra

    Returns: (best_subarray_list, best_sum)
    """
    if not inarray:
        return ([], 0)

    best_sum = inarray[0]
    best_start = 0
    best_end = 0

    current_sum = inarray[0]
    current_start = 0

    for i in range(1, len(inarray)):
        x = inarray[i]

        # Decide: extend the current range, or start a new range at i
        if current_sum + x < x:
            current_sum = x
            current_start = i
        else:
            current_sum += x

        # Update global best (use > not >= to keep the first best range on ties)
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i

    return (inarray[best_start:best_end + 1], best_sum)


def range_subpart_sum(inarray: list, target: int):
    n = len(inarray)
    for L in range(n):
        for R in range(L,n):
            total = 0
            for k in range(L, R+1):
                total += inarray[k]
                if total == target:
                    return True
                
    return False



def tests():
    sublist_sum_cases = [
        ([5], ([5], 5)),
        ([-5], ([-5], -5)),
        ([0], ([0], 0)),
        ([1, 2], ([1, 2], 3)),
        ([2, -1], ([2], 2)),
        ([-1, 2], ([2], 2)),
        ([-2, -1], ([-1], -1)),
        ([1, -2, 3], ([3], 3)),
        ([2, -1, 2], ([2, -1, 2], 3)),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], ([4, -1, 2, 1], 6)),
    ]

    fns = [
        range_subpart_bruteforce_3loops,
        range_subpart_2loops_running_sum,
        range_subpart_kadane,

    ]

    for arr, expected in sublist_sum_cases:
        for fn in fns:
            got = fn(arr)
            assert got == expected, f"{fn.__name__}({arr}) => {got}, expected {expected}"

    # -------------------------------
    # Tests for range_subpart_sum
    # Function returns: True/False
    # -------------------------------
    sum_target_cases = [
        # basic positives
        ([1, 2, 3], 5, True),    # [2,3]
        ([1, 2, 3], 6, True),    # [1,2,3]
        ([1, 2, 3], 7, False),

        # includes negatives
        ([-1, 2, 1], 2, True),   # [2]
        ([-1, 2, 1], 3, True),   # [2,1]
        ([-1, 2, 1], 0, False),

        # zeros
        ([0, 0, 0], 0, True),
        ([0, 0, 0], 1, False),

        # edge cases
        ([], 0, False),
        ([5], 5, True),
        ([5], 0, False),
    ]

    for arr, target, expected in sum_target_cases:
        got = range_subpart_sum(arr, target)
        assert got == expected, f"range_subpart_sum({arr}, {target}) => {got}, expected {expected}"

if __name__ == '__main__':
    tests()