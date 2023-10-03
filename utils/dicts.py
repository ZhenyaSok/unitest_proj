import collections


def get_val(collection, key, default="git"):
    collection = {}
    """

    :param key: ключ
    :param collection: словарь
    :type default: значение по умолчанию
    """
    if len(collection) == 0:
        return default
    if key == None:
        return default

    for key in collections.keys():
        return collection[key]

    return default
