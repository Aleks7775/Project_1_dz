def get_mask_card_number(mask_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    if isinstance(mask_card, str):
        if len(mask_card) == 16:
            str_mask_card = str(mask_card)
            return f"{str_mask_card[:4]} {str_mask_card[4:6] + '**'} **** {str_mask_card[12:]}"
    return "некорректный номер карты"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if isinstance(mask_account, str):
        if len(mask_account) == 20:
            str_mask_account = str(mask_account)
            return f"**{str_mask_account[-4:]}"
    return "некорректный номер счёта"
