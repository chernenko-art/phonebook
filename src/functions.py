import os

def add_user(dictionary: dict):
    """
    Add new user
    :param dictionary:
    :return:dictionary
    """
    name = input('Enter name for abonent: ')
    phone = input('Enter phone number for abonent: ')
    if name in dictionary:
        print('This abonent already exist: {} - {}'.format(name, dictionary[name]))
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


def read_file():
    """
    read from file phonebook.txt
    :return: phonebook
    """
    check_file = os.path.exists('phonebook.txt')
    if check_file is True:
        with open('phonebook.txt', 'r') as phonebook_from_file:  # load phonebook from file
            lines = phonebook_from_file.readlines()
            lines_list = [line for line in lines] 
            name_list, phone_list = lines_list
            return dict(zip(name_list.split(), phone_list.split()))
    else:
        return dict()


def write_file(dictionary: dict):
    """
    write in file phonebook.txt
    :param dictionary:
    :return: None
    """
    with open('phonebook.txt', 'w') as writing_from_file:
        name_list = []
        number_list = []
        for key, value in dictionary.items():
            name_list.append(key)
            number_list.append(value)
        print(' '.join(name_list), file=writing_from_file)
        print(' '.join(number_list), file=writing_from_file)
