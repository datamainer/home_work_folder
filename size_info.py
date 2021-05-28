import os


def size_info():
    folders_size = {}
    main_path = 'my_project/'
    folders = os.listdir('my_project/')

    for folder in folders:
        folder_path = os.path.join(main_path, folder)
        folder_size = os.path.getsize(folder_path)
        folders_size.setdefault(folder, folder_size)

    print(folders_size)

size_info()