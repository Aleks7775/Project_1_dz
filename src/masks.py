def get_mask_card_number(mask_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    str_mask_card = str(mask_card)
    return f"{str_mask_card[:4]} {str_mask_card[4:6] + '**'} **** {str_mask_card[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"
