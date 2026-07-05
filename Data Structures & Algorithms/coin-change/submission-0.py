class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        no_coins = [-1 for i in range(amount + 1)]
        no_coins[0] = 0
        for i in range(1, amount + 1):
            minim = 2**31

            for j in range(len(coins)):
                if coins[j] <= i and no_coins[i-coins[j]] != -1 and no_coins[i-coins[j]] < minim:
                    minim = no_coins[i-coins[j]]
            if minim < 2**31:
                no_coins[i] = minim + 1

            #no_coins[i] = min(no_coins[i-coins[j]] for j in range(len(coins)) if coins[j] <= i)

        return no_coins[amount]
    

          
