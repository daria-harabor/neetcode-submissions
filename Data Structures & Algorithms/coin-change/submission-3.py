class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        no_coins = [-1 for i in range(amount + 1)]
        no_coins[0] = 0
        for i in range(1, amount + 1):
            minim = float('inf')

            for c in coins:
                if c <= i and no_coins[i-c] != -1 and no_coins[i-c] < minim:
                    minim = no_coins[i-c]
            if minim < float('inf'):
                no_coins[i] = minim + 1

        return no_coins[amount]
    

          
