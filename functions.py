def get_tasklist(filepath ='tasklist.txt'):
    """this function opens the addressed file"""
    with open(filepath, 'r') as file:
        tasklist_local = file.readlines()
    return tasklist_local


def write_tasklist(tasks_storing, filepath = "tasklist.txt"):
    with open(filepath, 'w') as file:
        file.writelines(tasks_storing)