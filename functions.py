def readfile(filepath):
    """ Read a text file and return the list of tasks."""
    try:
        with open(filepath) as workingFile_local:
            taskDatabase_local = workingFile_local.readlines()
        return taskDatabase_local
    except FileNotFoundError:
        return ""


def writefile(write_local, filepath, append=False):
    """Write the task in the text file database."""
    mode = 'a' if append else 'w'
    with open(filepath, mode) as workingFile_local:
        if isinstance(write_local, list):
            workingFile_local.write('\n'.join(write_local))
        else:
            workingFile_local.write(write_local)


if __name__ == "__main__":  # __name__ variable that is always the name of file running
    """ This section of code will only run if functions.py is run directly, not if imported """
    print("functions.py has been executed successfully")

# Databases
# for data, filename in zip(database,filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(data)


# from functions import taskRead, taskWrite


# Use this method if you have a lot of functions that you are importing
# import functions
# this will make it so that you must reference a method to use the functions
# functions.taskRead()
# functions.taskWrite()

# gui.FileBrowse("Choose)
# gui.FolderBrowse("Choose")
# gui.Input()