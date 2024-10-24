def find_min_coins(amount: int) -> dict[int, int]:
    coins = [50, 25, 10, 5, 2, 1]

    # Масив для збереження мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 монет не потрібно

    # Динамічне програмування для пошуку мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Пошук, які монети використовувались
    result = {}
    current_amount = amount
    while current_amount > 0:
        for coin in coins:
            if current_amount >= coin and min_coins[current_amount] == min_coins[current_amount - coin] + 1:
                if coin not in result:
                    result[coin] = 1
                else:
                    result[coin] += 1
                current_amount -= coin
                break

    return result


print(find_min_coins(113))
# Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}
