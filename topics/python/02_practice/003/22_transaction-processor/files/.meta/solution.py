def processTransactions(transactions):
    balances = {}

    for transaction in transactions:
        from_account = transaction["from"]
        to_account = transaction["to"]
        amount = transaction["amount"]

        if from_account is not None:
            balances[from_account] = balances.get(from_account, 0) - amount

        if to_account is not None:
            balances[to_account] = balances.get(to_account, 0) + amount

    return balances
