def filter_by_state(transactions, state='EXECUTED'):
    """
    Фильтрует список транзакций по состоянию.

    :param transactions: список словарей с транзакциями
    :param state: состояние для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список транзакций
    """
    return [transaction for transaction in transactions if transaction['state'] == state]


def sort_by_date(transactions, descending=True):
    """
    Сортирует список транзакций по дате.

    :param transactions: список словарей с транзакциями
    :param descending: флаг сортировки (по умолчанию True — убывание)
    :return: отсортированный список транзакций
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)
