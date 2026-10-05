prices = [10,1,5,6,7,1]

def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def main():
    print(maxProfit(prices))
if __name__ == "__main__":
    main()  
