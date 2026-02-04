'''
 “Intersection of two arrays”

Input: A = [1, 2, 2, 3], B = [2, 2]
Output: [2, 2] (or [2] if unique intersection version)
Naive approach: for each element in A, search in B (two loops)
Efficient: sort + two pointers, or hash counts
'''

def intersection_2lists(inarrayA:list, inarrayB: list):

    out = []

    # Track which elements in B have already been matched/used
    usedB = [False] * len(inarrayB)

    # 1st loop over list A
    for x in inarrayA:
        # 2nd loop over list B
        for j, y in enumerate(inarrayB):
            # Only match an unused B element
            if not usedB[j] and x == y:
                out.append(x)
                usedB[j] = True  # consume this B element so it can't match again
                break  # move to next x after first match

    return out


from collections import Counter
import heapq

def merge_2lists_sort(inarrayA: list, inarrayB: list):
    """Merge by concatenating then sorting (works for unsorted inputs)."""
    return sorted(inarrayA + inarrayB)


def merge_2lists_two_pointers(inarrayA: list, inarrayB: list):
    """Merge two already-sorted lists using two pointers (classic merge step).

    Time: O(n+m), Space: O(n+m)
    """
    i = j = 0
    out = []

    while i < len(inarrayA) and j < len(inarrayB):
        if inarrayA[i] <= inarrayB[j]:
            out.append(inarrayA[i])
            i += 1
        else:
            out.append(inarrayB[j])
            j += 1

    # Append leftovers
    out.extend(inarrayA[i:])
    out.extend(inarrayB[j:])
    return out


def merge_2lists_heapq(inarrayA: list, inarrayB: list):
    """Merge two already-sorted lists using heapq.merge."""
    return list(heapq.merge(inarrayA, inarrayB))


def merge_2lists_counter(inarrayA: list, inarrayB: list):
    """Merge using Counter (multiset union) and then expanding sorted keys.

    Works even if inputs are unsorted, but requires elements to be sortable.
    """
    counts = Counter(inarrayA) + Counter(inarrayB)
    out = []
    for value in sorted(counts.keys()):
        out.extend([value] * counts[value])
    return out

def merge_2lists_1loop(inarrayA: list, inarrayB: list):
    mergelistA = inarrayB

    for i,x in enumerate(inarrayA):
        mergelistA.append(x)
        print('mergelistA, ', mergelistA, i, x)

    merge = sorted(mergelistA)
    print('mergelist ', mergelistA, merge)

    return merge


def tests():

    assert intersection_2lists([1, 2, 2, 3], [2, 2]) == [2,2]
    assert intersection_2lists([2, 2, 2], [2, 2]) == [2, 2]
    assert intersection_2lists([1, 3], [2, 2]) == []

    assert merge_2lists_sort([1, 3, 7], [2, 3, 10]) == [1, 2, 3, 3, 7, 10]
    assert merge_2lists_two_pointers([1, 3, 7], [2, 3, 10]) == [1, 2, 3, 3, 7, 10]
    assert merge_2lists_heapq([1, 3, 7], [2, 3, 10]) == [1, 2, 3, 3, 7, 10]
    assert merge_2lists_counter([1, 3, 7], [2, 3, 10]) == [1, 2, 3, 3, 7, 10]
    assert merge_2lists_1loop([1, 3, 7], [2, 3, 10]) == [1, 2, 3, 3, 7, 10]

if __name__ == '__main__':
    tests()