def find_missing_number_0(string: str) -> int:
    """
    :param string: string with nine numbers from 0 to 9, one is missing
    :return: missing number
    """
    presence = {i: i for i in range(10)}
    for number in string:
        presence.pop(int(number))

    return list(presence.items())[0][0]


def find_missing_number(string: str) -> int:
    """
    :param string: string with nine numbers from 0 to 9, one is missing
    :return: missing number
    """
    return int(list(set('0123456789') - set(string))[0])
