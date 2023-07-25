# Using two pointers
# memory = O(1)
# time = O(n)


def maxProfit(prices):
    l, r = 0, 1
    maxProf = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProf = max(maxProf, profit)
        else:
            l = r
        r+=1
    
    return maxProf, "Buying: =", l, "Selling =", r

print(maxProfit([2, 5, 3, 7]))
