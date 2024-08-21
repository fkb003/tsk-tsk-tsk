def move(index: int, origin: list, destination: list) -> None:
    destination.append(origin.pop(index))

def complete(index: int, selected_list: list, lists: dict) -> None:
    move(index, lists[selected_list], lists['done'])

def skip(index: int, selected_list: list, lists: dict) -> None:
    move(index, lists[selected_list], lists['skipped'])

def add(task: str, selected_list:str, lists: dict) -> None:
    lists[selected_list].append(task)    

def stop(additional: str, selected_list: list, lists: dict):
    exit()
menu = {
       '.': complete,
        '#': skip,
        '!': stop,
        'add': add,
}