from functions import *

phonebook = read_file()  # check the file phonebook.txt or create new dict

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
    '''
    )

    user_kod = input('\t Your choice?: ')  # enter user command
    print()  # print bool string

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
        write_file(phonebook)
        print('By, my darling')
        break
