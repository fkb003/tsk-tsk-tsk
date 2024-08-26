import os

def display(selected_list: list, lists: dict) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, task in enumerate(lists[selected_list[0]]):
        print(f'{i+1:3}. {task}')