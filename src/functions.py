def add_user(dictionary: dict):
    """
    Add new user
    :param dictionary:
    :return:dictionary
    """
    name = input('Enter name for abonent: ')
    phone = input('Enter phone number for abonent: ')
    if name in dictionary:
        print('Тhis abonent already exist: {} - {}'.format(name, dictionary[name]))
    else:
        dictionary[name] = phone
        print('New abonent "{}" created'.format(name))
    return dictionary


def delete_user(dictionary: dict):
    """
    Deleted user
    :param dictionary:
    :return: dictionary
    """
    name = input('Enter name for abonent: ')
    if name in dictionary:
        dictionary.pop(name)
        print('Abonent "{}" deleted'.format(name))
    else:
        print('Sorry, this abonent not exist')
    return dictionary


def update_user(dictionary: dict):
    """
    Update user number
    :param dictionary:
    :return: dictionary
    """
    name = input('Enter name for abonent: ')
    phone = input('Enter New phone number for abonent: ')
    if name in dictionary:
        dictionary[name] = phone
        print('Abonent "{}" updated'.format(name))
    else:
        print('Sorry, this abonent not exist')
    return dictionary


def search_user(dictionary: dict):
    """
    Search user (Name or number)
    :param dictionary:
    :return: dictionary
    """
    search_value = input('Enter name or phone number for abonent: ')
    name_in_dict = False
    for key, value in dictionary.items():
        if key.lower() == search_value.lower() or value == search_value:
            print(key, ' - ', value)
            name_in_dict = True
    if name_in_dict == False:
        print('Sorry, this abonent not exist')


def print_phonebook(dictionary: dict):
    """
    Print all phonebook
    :param dictionary:
    :return: None
    """
    for key, value in dictionary.items():
        print(key, ' - ', value)
