import model


while(True):
    print('ADD - добавить запись\nDELETE - удалить запись\nEXPORT - экспортировать справочник\n\
IMPORT - импортировать справочник')
    startword = input().lower()


    if startword == "add":
        model.Adding()

    if startword == "delete":
        model.Del()

    if startword == "export":
        model.export()

    if startword == "import":
        model.import.pb()