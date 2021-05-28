import os


def create_project():
    folder_name = ['settings', 'mainapp', 'authapp']
    settings_file_name = ['__init__.py', 'dev.py', 'prod.py']
    mainapp_file_name = ['__init__.py', 'models.py', 'views.py']
    authapp_file_name = ['__init__.py', 'models.py', 'views.py']
    templates_file_name = ['base.html', 'index.html']

    os.mkdir('my_project')
    main_folder = 'my_project/'
    folder_index = 0

    for name in folder_name:
        os.mkdir('my_project/' + name)

    for name in settings_file_name:
        open(name, 'w')
        os.replace(name, main_folder + folder_name[folder_index] + '/' + name)

    folder_index += 1

    for name in mainapp_file_name:
        open(name, 'w')
        os.replace(name, main_folder + folder_name[folder_index] + '/' + name)

    folder_index += 1

    for name in authapp_file_name:
        open(name, 'w')
        os.replace(name, main_folder + folder_name[folder_index] + '/' + name)

    os.mkdir('my_project/mainapp/templates')
    os.mkdir('my_project/authapp/templates')

    for name in templates_file_name:
        open(name, 'w')
        os.replace(name, main_folder + folder_name[1] + '/templates/' + name)

        open(name, 'w')
        os.replace(name, main_folder + folder_name[2] + '/templates/' + name)


create_project()

