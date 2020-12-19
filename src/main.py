from functions import *
import pickle
import os


# check exist file phonebook.pickle
check_file = os.path.exists('phonebook.pickle')
if check_file is True:
    with open('phonebook.pickle', 'rb') as phonebook_from_file:  # load phonebook from file
        phonebook = pickle.load(phonebook_from_file)
else:
    phonebook = {}

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

    user_kod = input('Your choice?: ')  # enter user command

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
        with open('phonebook.pickle', 'wb') as phonebook_from_file:
            pickle.dump(phonebook, phonebook_from_file)
        print('By, my darling')
        break
