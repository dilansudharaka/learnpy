def max_profit(prices: list[int]) -> int:
    max_profit:int = 0
    buy:int = prices[0]

    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
           
        elif prices[i] - buy > max_profit:
            max_profit = prices[i] - buy

    return max_profit

print(max_profit([7,6,4,3,1]))
            