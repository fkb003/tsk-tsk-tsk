def move(index: int, origin: list, destination: list) -> None:
    destination.append(origin.pop(index))

def complete(index: int, selected_list: list, lists: dict) -> None:
    move(index, lists[selected_list[0]], lists['done'])

def skip(index: int, selected_list: list, lists: dict) -> None:
    move(index, lists[selected_list[0]], lists['skipped'])

def add_task(task: str, selected_list: list, lists: dict) -> None:
    lists[selected_list[0]].append(task)    

def add_list(list_name: str, selected_list: list, lists: dict) -> None:
    lists.update({list_name: []})
    change_list(list_name, selected_list, lists)

def change_list(list_name: str, selected_list: list, lists: dict) -> None:
    selected_list[0] = list_name
    
def stop(additional: str, selected_list: list, lists: dict):
    exit()
menu = {
       '.': complete,
        '#': skip,
        '!': stop,
        '+': add_list,
        'add': add_task,
        '@': change_list
}