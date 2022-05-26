import UI

phonebook = []

def Adding():
    global phonebook
    phonebook.append(UI.entry())
    print(phonebook)

def Del():
    global phonebook
    phonebook.pop(UI.deleting())
    print(phonebook)

def export():
    global phonebook
    divider = UI.symbol()
    with open('My_phonebook.csv', 'w', encoding="utf-16") as file:
        for entry in phonebook:
            for i in range(len(entry)-1):
                file.write(f'{entry[i]}{divider}')
            file.write(f'{entry[-1]}')
            if divider == '\n': file.write(f'\n')
            file.write(f'\n')

def import_pb():
    global phonebook
    templist = []
    phonebook = []
    file = open('My_phonebook.csv', 'r', encoding="utf-16")
    for line in file:
        if ';' in line:
            phonebook.append(line.split(';'))
        elif line != '\n':
            templist.append(line)
        else: 
            phonebook.append(templist)
            templist = []
    file.close
    print(phonebook)
