def move(index: int, origin: list, destination: list) -> None:
    try: destination.append(origin.pop(index))
    except: input('That action is not possible!\n')

def complete(index: int, selected_lists: list, lists: dict) -> None:
    move(index, lists[selected_lists[0]], lists['done'])

def skip(index: int, selected_lists: list, lists: dict) -> None:
    move(index, lists[selected_lists[0]], lists['skipped'])

def add_task(task: str, selected_lists: list, lists: dict) -> None:
    lists[selected_lists[0]].append(task)    

def add_list(list_name: str, selected_lists: list, lists: dict) -> None:
    if type(list_name) != str:
        input("Indices can't be used as list names!\n")
    elif list_name in lists:
        input("List already exists!\n")
    else:
        lists.update({list_name: []})
        selected_lists.insert(-2, list_name)
        change_list(list_name, selected_lists, lists)

def change_list(l, selected_lists: list, lists: dict) -> None:
    visible_lists = selected_lists[1:]
    if type(l) == str:
        if l in lists: selected_lists[0] = l
        else: input("List doesn't exist!\n")
    else:
        if -len(visible_lists) <= l < len(visible_lists):
            selected_lists[0] = visible_lists[l]
        else: input("List doesn't exist!\n")

    
def stop(additional: str, selected_lists: list, lists: dict):
    exit()

menu = {
       '.': complete, 
        '#': skip,
        '!': stop,
        '+': add_list,
        'add': add_task,
        '@': change_list
}