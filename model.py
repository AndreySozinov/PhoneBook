import UI

phonebook = []

def Adding():
    global phonebook
    phonebook.append(UI.entry())
    print(phonebook)

def Del()
    global phonebook
    phonebook.pop(UI.deleting())
    print(phonebook)

def export():
    global phonebook
    divider = UI.symbol()
    with open('My_phonebook.csv', 'w') as file:
        for entry in phonebook:
            for element in entry:
                file.write(f'{element}{divider}\n')

def import_pb():
    global phonebook
    file = open('My_phonebook.csv', 'r')
    for line in file:
        phonebook.append(line)
    file.close
    