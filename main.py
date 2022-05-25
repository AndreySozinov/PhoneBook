import model


while(True):
    print('ADD - добавить запись\nDELETE - удалить запись\nEXPORT - экспортировать справочник\n\
IMPORT - импортировать справочник')
    startword = input().lower()


    if startword == "add":
        model.Adding()

    elif startword == "delete":
        model.Del()

    elif startword == "export":
        model.export()

    elif startword == "import":
        model.import_pb()

    else: print("Повнимательнее, пожалуйста.")