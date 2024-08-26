def move(index: int, origin: list, destination: list) -> None:
    destination.append(origin.pop(index))

def complete(index: int, selected_lists: list, lists: dict) -> None:
    move(index, lists[selected_lists[0]], lists['done'])

def skip(index: int, selected_lists: list, lists: dict) -> None:
    move(index, lists[selected_lists[0]], lists['skipped'])

def add_task(task: str, selected_lists: list, lists: dict) -> None:
    lists[selected_lists[0]].append(task)    

def add_list(list_name: str, selected_lists: list, lists: dict) -> None:
    lists.update({list_name: []})
    change_list(list_name, selected_lists, lists)

def change_list(list_name: str, selected_lists: list, lists: dict) -> None:
    selected_lists[0] = list_name
    
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