from functions import *

phonebook = \
    {
        'Elvira': '8891',
        'Milla Jovovich': '9919',
        'Artur Pirozkov': '7761'
    }

while True:
    # start message for user (choice command for phonebook)
    print(
        '''
        Select what you want to do with phonebook:
        
                1. Add user
                2. Delete user
                3. Update user
                4. Search user
                5. Print phonebook
                0. Exit
        ''')

    # enter user command
    user_kod = input('Your choice?: ')

    # execution for user command
    if user_kod == '1':
        add_user(phonebook)
    elif user_kod == '2':
        delete_user(phonebook)
    elif user_kod == '3':
        update_user(phonebook)
    elif user_kod == '4':
        search_user(phonebook)
    elif user_kod == '5':
        print_phonebook(phonebook)
    else:
        print('By, my darling')
        break