import os
import shutil


def move_file():
    os.mkdir('my_project/templates')

    mainapp_source_path = 'my_project/mainapp/templates'
    mainapp_destination_path = 'my_project/templates/mainapp'

    authapp_source_path = 'my_project/authapp/templates'
    authapp_destination_path = 'my_project/templates/authapp'

    mainapp_new_location = shutil.move(mainapp_source_path, mainapp_destination_path)
    authapp_new_location = shutil.move(authapp_source_path, authapp_destination_path)


move_file()



