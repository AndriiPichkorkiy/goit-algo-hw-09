def find_coins_greedy(amount: int) -> dict[int, int]:
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        while coin <= amount:
            amount -= coin
            if coin not in result:
                result[coin] = 1
            else:
                result[coin] += 1
    return result


print(find_coins_greedy(113))
# Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}
