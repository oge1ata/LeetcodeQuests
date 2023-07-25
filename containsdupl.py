#brute time = nsqr, meory will be constant
#sort time = nlogn memory = constant
# Using a hashmap!time = n, space = n

def containdupl (nums) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    
    return False


print(containdupl([1, 2, 5, 7, 6, 3]))