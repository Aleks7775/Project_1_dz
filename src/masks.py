import logging

logger = logging.getLogger("masks")

file_handler = logging.FileHandler("/home/aleksandr/PycharmProjects/PythonProject2/logs/masks_log.log", 'w')
file_formatter = logging.Formatter('%(asctime)s -  %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(mask_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    if isinstance(mask_card, str):
        if len(mask_card) == 16:
            str_mask_card = str(mask_card)
            card_mask = f"{str_mask_card[:4]} {str_mask_card[4:6] + '**'} **** {str_mask_card[12:]}"
            logger.info(f"Успешная маскировка банковской карты: {card_mask}")
            return card_mask
    error_message_msk = "некорректный номер карты"
    logger.error(error_message_msk)
    return error_message_msk


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if isinstance(mask_account, str):
        if len(mask_account) == 20:
            str_mask_account = str(mask_account)
            account_mask = f"**{str_mask_account[-4:]}"
            logger.info(f"Успешная маскировка банковского счета: {account_mask}")
            return account_mask
    error_message_acc = "некорректный номер счёта"
    logger.error(error_message_acc)
    return error_message_acc
