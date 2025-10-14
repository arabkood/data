def maskCard(card_number):
    if len(card_number) <= 4:
        return card_number

    masked_part = "#" * (len(card_number) - 4)
    visible_part = card_number[-4:]

    return masked_part + visible_part
