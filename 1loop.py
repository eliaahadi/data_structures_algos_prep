'''
“Count how many are > 0”

- Input: [-2, 0, 4, 5]
- Output: 2
'''

def oneloop_findabovezero(inarray: list):
    countabovezero = 0

    print(inarray)
    # loop over array elements

    for i in range(len(inarray)):
        #if condition for element above zero
        print(i)
        if (inarray[i] > 0):
            #add to count
            countabovezero += 1

    return countabovezero


def sock_pairs(inarray: list):
    """Return the number of unique sock pairs.

    Each sock can be used at most once. Example:
    [3,3,2,1,1,1] -> 2 (one pair of 3s, one pair of 1s)

    Implementation uses sorting + a single scan (no sets/dicts).
    """
    arr = sorted(inarray)
    pairs_num = 0
    i = 0

    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            pairs_num += 1
            i += 2  # consume both socks in the pair
        else:
            i += 1  # move forward and keep looking


    '''
    sets way

    counts = {}

    for color in inarray:
        counts[color] = counts.get(color, 0) + 1
        
        if counts[color] == 2:
            pairs_num += 1
            counts[color] = 0
    '''
    return pairs_num

def tests():
    # print('oneloop ', oneloop_findabovezero([-2, 0, 4, 5]))
    assert(oneloop_findabovezero([-2, 0, 4, 5]) == 2)
    assert sock_pairs([3,3,2,1,1,1]) == 2
    assert sock_pairs([3,3,2,1,1,3,5,4,2]) == 3


if __name__ == "__main__":
    tests()