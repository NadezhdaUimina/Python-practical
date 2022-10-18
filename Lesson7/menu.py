def menu(): # меню
    print('Команды для работы с телефонным справочником:\n'
        '1 - Вывести данные из файла в консоль\n'
        '2 - Добавить данные в телефонный справочник\n'
        '3 - Поиск контакта по фамилии\n')
    team = int(input('Введите команду: '))
    if team < 1 or team > 3: team = int(input('Неверно введены данные, введите команду: '))
    if team == 1:
        print('Вывести данные:\n'
        '1 - Выести данные из Phone_book.csv в консоль\n'
        '2 - Выести данные из Phone_book.txt в консоль\n'
        '3 - вывести данные из вех файлов в фаил Phone_book_all.csv\n')
        print_file = int(input('Введите команду: '))
        if print_file < 1 or print_file > 3: team = int(input('Неверно введены данные, введите команду: '))
        if print_file == 1: return 'print_csv'
        elif print_file == 2: return 'print_txt'
        elif print_file == 3: return 'print_all'
    elif team == 2:
        print('Добавить данные в существующий телефонный справочник\n'
        '1 - Phone_book.csv\n'
        '2 - Phone_book.txt\n')
        record_file = int(input('Введите команду: '))
        if record_file < 1 or record_file > 2: team = int(input('Неверно введены данные, введите команду: '))
        return 'record_csv' if record_file == 1 else 'record_txt'
    elif team == 3:
        return 'search'

