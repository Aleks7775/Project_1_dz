def get_mask_card_number(mask_card: int) -> str:
    """Функция маскировки номера банковской карты"""
    str_mask_card = str(mask_card)
    return f"{str_mask_card[:4]} {str_mask_card[4:6] + '**'} **** {str_mask_card[12:]}"


def get_mask_account(mask_account: int) -> str:
    """Функция маскировки номера банковского счета"""
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"


card_number = int(input("Введите номер карты"))
print(get_mask_card_number(card_number))
account_number = int(input("Введите номер счета"))
print(get_mask_account(account_number))
