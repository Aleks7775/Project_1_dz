def mask_account_card(bank_prod):
    """Функция маскировки номера и счета в банке"""
    if "Счет" in bank_prod:
        return f"Счет **{(bank_prod[-4:])}"
    else:
        name_card = []
        num_card = []
        for i in bank_prod:
            if i.isdigit():
                num_card.append(i)
            else: name_card.append(i)
        return f"{"".join(name_card)} {"".join(num_card[:4])} {"".join(num_card[4:6]) + '**'} **** {"".join(num_card[12:])}"






def get_date(data):
    """Функция которая принимает на вход строку с датой и возвращает её в правильном формате """
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


"""Проверка функций"""
num_c = mask_account_card("Visa Platinum 8990922113665229")
bank_account = mask_account_card("Счет 73654108430135874305")
print(num_c)
print(bank_account)
data_ = get_date("2024-05-11T02:26:18.671407")
print(data_)