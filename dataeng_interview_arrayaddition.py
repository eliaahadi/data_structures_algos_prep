'''
In: [4, 6, 23, 10, 1, 3]
Out: True b/c 4 + 6 + 10 + 3 = 23 (exclude largest #)
any combination
 
Input: [5,7,16,1,2]
Output: false b/c largest value is 15
'''
 
 
def ArrayAddition_myself(arr):
 
  # find largest num in arr and store in var (call large)
  # large = 0
  sorted_array = sorted(arr)
  largest_num = sorted_array[-1]
  pool = sorted_array[:-1]
  print('input --- ', arr)
  print('large is ', largest_num, pool)
 
 
  reachable = {0}

  # iterate over sorted array without largest num (pool)
  for x in pool:
      # create new set to track items seen
      new_reachable = set(reachable)
      print(' \n \n1st loop x ', x, '\n')

      # loop over existing reachable set
      for y in reachable:
        print('  2nd loop y ', y, '\n')
        # sum values in pool + reachable
        new_sum = x + y
        print('new reachable ', new_reachable)
        print('new sum ', new_sum)

        # if largest num = sum
        if largest_num == new_sum:
            return True
        # add new sum to new set
        new_reachable.add(new_sum)
      
      # update existing reachable set with new set
      reachable = new_reachable
      print('updated reachable ', reachable)

  
  # print('new sort arr is ', sorted_array)
  # sortarr = sorted_array[:-1] 
  # print('update sort arr is ', sortarr)
  # loop over array with for first element (L)
  # for L in range(len(sorted_array)):
 
    # loop over array with second element (R) and track total
    # for R in range(L, len(sortarr)):
    # total = 0
 
    #   # loop k element inside L,R window and update total
    #   for k in range(L, R+1):
    #     total += sortarr[k]
        # print('element ', sortarr[k])
    #     if total == largest_num:
    #       return True
    #     # print('sorted arr INCREMENT element ', sortarr[k])
    #     print('TOTAL in loop ', total, largest_num)
 
 
 
    
 
 
  # for i in range(len(sortarr)-1):
  #     # if i is equal to large, ignore that num
 
 
  # print('total ', total)
  return False
 

'''
Array Addition

Given an array of integers, return True if any combination of numbers in the array
(excluding the largest number) can sum to the largest number. Otherwise return False.

Examples:
In:  [4, 6, 23, 10, 1, 3]
Out: True  because 4 + 6 + 10 + 3 = 23 (exclude largest)

In:  [5, 7, 16, 1, 2]
Out: False because largest is 16, and the other numbers sum to 15

Note:
- This is a SUBSET problem (pick any elements), not a contiguous subarray/window problem.
'''


def ArrayAddition_backtrack(arr):
    """Backtracking / DFS over include/exclude choices.

    Time: O(2^n) worst-case
    Space: O(n) recursion stack

    Works for any integers (including negatives). If all pool values are non-negative,
    we can safely prune when current_sum > target.
    """
    if not arr:
        return False

    sorted_array = sorted(arr)
    target = sorted_array[-1]
    pool = sorted_array[:-1]

    all_nonneg = all(x >= 0 for x in pool)

    def dfs(i, current_sum):
        if current_sum == target:
            return True
        if i == len(pool):
            return False
        if all_nonneg and current_sum > target:
            return False

        # Choice 1: include pool[i]
        if dfs(i + 1, current_sum + pool[i]):
            return True

        # Choice 2: skip pool[i]
        return dfs(i + 1, current_sum)

    return dfs(0, 0)


def ArrayAddition_bitmask(arr):
    """Iterative brute force by enumerating all subsets (bitmask).

    Time: O(n * 2^n)
    Space: O(1) extra

    This is a clear "no recursion" brute force.
    """
    if not arr:
        return False

    sorted_array = sorted(arr)
    target = sorted_array[-1]
    pool = sorted_array[:-1]

    n = len(pool)
    # Enumerate every subset using bits 0..n-1
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += pool[i]
        if total == target:
            return True

    return False


def ArrayAddition_dp_set(arr):
    """DP using a set of reachable sums.

    Idea:
      reachable = all sums we can make so far.
      For each x in pool: new sums are {s + x for s in reachable}.

    Time: O(n * S) where S is number of distinct reachable sums
    Space: O(S)

    Works with negatives too.
    """
    if not arr:
        return False

    sorted_array = sorted(arr)
    target = sorted_array[-1]
    pool = sorted_array[:-1]

    reachable = {0}
    for x in pool:
        new_reachable = set(reachable)
        for s in reachable:
            ns = s + x
            if ns == target:
                return True
            new_reachable.add(ns)
        reachable = new_reachable

    return target in reachable


def ArrayAddition(arr):
    """Default implementation."""
    return ArrayAddition_backtrack(arr)


def tests():
    
    assert ArrayAddition_myself([4, 6, 20, 10]) == True
    # assert ArrayAddition_myself([4, 6, 23, 10, 1, 3]) == True
    assert ArrayAddition([4, 6, 23, 10, 1, 3]) is True
    assert ArrayAddition([5, 7, 16, 1, 2]) is False

    # Additional quick sanity checks
    assert ArrayAddition([1, 2, 3, 6]) is True      # 1+2+3=6
    assert ArrayAddition([1, 2, 4, 8]) is False
    assert ArrayAddition([0, 0, 0, 0]) is True      # 0 can be made by empty subset or zeros
    # assert ArrayAddition([-1, -2, -3, -6]) is True  # -1 + -2 + -3 = -6



    # Cross-check the three methods on the same inputs
    cases = [
        [4, 6, 23, 10, 1, 3],
        [5, 7, 16, 1, 2],
        [1, 2, 3, 6],
        [1, 2, 4, 8],
        [0, 0, 0, 0],
        [-1, -2, -3, -6],
    ]

    for arr in cases:
        a = ArrayAddition_backtrack(arr)
        b = ArrayAddition_bitmask(arr)
        c = ArrayAddition_dp_set(arr)
        assert a == b == c, f"Mismatch for {arr}: backtrack={a}, bitmask={b}, dp={c}"


if __name__ == "__main__":
  tests()