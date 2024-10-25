def greedy_coin_change(amount):
    # Зоосны төрөлүүдийг буурах дарааллаар жагсаана
    coins = [25, 10, 5, 1]
    coin_count = {}  # Хэдэн ширхэг зоос хэрэглэснийг хадгалах dictionary

    for coin in coins:
        # тухайн зоосоор хэдэн ширхэг хэрэглэх вэ
        count = amount // coin
        if count > 0:
            coin_count[coin] = count
        amount %= coin  # Үлдсэн дүнг тооцно

    return coin_count

# Жишээ дүн: 83₮
amount = 83
result = greedy_coin_change(amount)

# Үр дүнг хэвлэх
for coin, count in result.items():
    print(f"{coin}₮ зоос: {count} ширхэг")
