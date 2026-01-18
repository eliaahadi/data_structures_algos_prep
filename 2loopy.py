'''
“Find all pairs with absolute difference k”

Input: nums = [1, 5, 3, 4, 2], k = 2
Output: [(1,3), (5,3), (4,2)] (format varies)
'''

def twoloop_allpairs_diff_k(inarray: list, diff_k: int):
    allpairs = []
    # 1st loop over inarray element
    for i in range(len(inarray)):
        print('1stloop i ', i, '1stloop element ', inarray[i])
        # 2nd loop over next inarray element
        for j in range(i+1, len(inarray)):
            print('2ndloop j ', j, '2ndloop element ', inarray[j])
            # Use absolute difference so we catch both (a-b==k) and (b-a==k)
            if abs(inarray[i] - inarray[j]) == diff_k:
                print('matching cond ', inarray[i], inarray[j], diff_k)
                # add matching pair to allpairs
                allpairs.append((inarray[i], inarray[j])) 

    print('allpairs ', allpairs)
    return allpairs


def twoloop_allpairs_diff_k_hashmap(inarray: list, diff_k: int):
    """Return all pairs (a, b) that appear in the array with i < j and |a-b| == diff_k.

    Matches the same pair-ordering as the 2-loop brute force: (inarray[i], inarray[j]).
    """
    if diff_k < 0:
        # Absolute difference can't be negative
        return []

    allpairs = []
    counts = {}  # value -> how many times we've seen it so far (indices < current)

    for x in inarray:
        if diff_k == 0:
            # Pairs of equal elements
            # dictionary.get(keyname, value)
            if counts.get(x, 0) > 0:
                print('diffk = 0', x, 'counts ' ,counts.get(x, 0), 'diffk ' , diff_k, allpairs, counts)
                # For each previous occurrence, we can form a pair (x, x)
                # use extend instead of append since there may be more than 1 element
                allpairs.extend([(x, x)] * counts[x])
        else:
            # Need previous values y such that |x - y| == diff_k
            # That means y == x - diff_k OR y == x + diff_k
            lo = x - diff_k
            hi = x + diff_k
            print('counts loop ', x, lo, hi, counts, counts.get(x,0))
            if counts.get(lo, 0) > 0:
                print('loop lo', x, counts)
                allpairs.extend([(lo, x)] * counts[lo])
            if counts.get(hi, 0) > 0:
                print('loop hi ', x, counts)
                allpairs.extend([(hi, x)] * counts[hi])
            

        counts[x] = counts.get(x, 0) + 1
        '''
        1st loop in [1, 5, 3, 4, 2]
        x = 1
        diff_k = 2
        lo = 2-1 = 1
        hi = 2+1 = 3
        counts.get(1,0) = 0
        counts.get(1,0) = 0
        '''

    print('allpairs ', allpairs)
    return allpairs


'''
1st loop
i = 0
x = 1
seen = {}
need = 1
seen[1] = 0
seen = {1:0}

2nd loop
i = 1
x = 5
seen = {1: 0}
need = 3
seen[5] = 1
seen = {1:0, 5:1} 
'''









def tests():
    # assert twoloop_allpairs_diff_k([1, 5, 3, 4, 2], 2) == [(1, 3), (5, 3), (4, 2)]
    # assert twoloop_allpairs_diff_k_hashmap([1, 5, 1], 0) == [(1, 1)]
    # assert twoloop_allpairs_diff_k_hashmap([1, 5, 2], 1) == [(1, 2)]
    assert twoloop_allpairs_diff_k_hashmap([1, 5, 3, 4, 2], 2) == [(1, 3), (5, 3), (4, 2)]


if __name__ == '__main__':
    tests()