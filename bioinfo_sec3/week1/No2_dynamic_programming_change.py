
#money = 40
money = 219986
#coins = [50, 25, 20, 10, 5, 1]
coins = [19,17,12,8,5,3,1]

def dp_change(money, coins):
    min_number_coins = [0]
    for m in range(1, money+1):
        min_number_coins.append(10000000)
        for i in coins:
            if m >= i:
                if min_number_coins[m-i] + 1 < min_number_coins[m]:
                    min_number_coins[m] = min_number_coins[m-i] + 1
    
    return min_number_coins[money] 


print(dp_change(money, coins))

