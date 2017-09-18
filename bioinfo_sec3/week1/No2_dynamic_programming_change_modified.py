
#money = 40
money = 340
#coins = [50, 25, 20, 10, 5, 1]
coins = [19,17,12,8,5,3,1]

def dp_change(money, coins):
    min_number_coins = [0]
    for m in range(1, max(coins)+1):
        min_number_coins.append(1000)
        for i in coins:
            if m >= i:
                if min_number_coins[m-i] + 1 < min_number_coins[m]:
                    min_number_coins[m] = min_number_coins[m-i] + 1
    
    print(min_number_coins)

    if money <= max(coins):
        min_num = min_number_coins[money]
    else:
        min_num = (money // max(coins)) + min_number_coins[(money % max(coins))]
        for i in coins:
            if money % i == 0:
                if (money // i) < min_num:
                    min_num = (money // i)

    return min_num
    #print(min_number_coins)
    #return min_number_coins[money] 


print(dp_change(money, coins))

