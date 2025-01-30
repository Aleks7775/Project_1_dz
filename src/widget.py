def mask_account_card(bank_prod):
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






def get_date():
    pass