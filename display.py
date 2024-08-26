import os

def display(selected_lists: list, lists: dict) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal_size = min(120, os.get_terminal_size().columns)
    visible_lists = selected_lists[1:]
    max_length = 0
    max_width = (terminal_size//len(visible_lists))-3
    for l in visible_lists:
        length = len(lists[l])
        if length > max_length:
            max_length = length
        width = len(l)
        if width > max_width:
            max_width = width
    
    dash_length = (len(visible_lists) * (max_width+3))+1
    print('-' * dash_length)
    formatted_headers = [f'{header:^{max_width}}' for header in visible_lists]
    print(f"| {' | '.join(formatted_headers)} |")
    print('-' * dash_length)
    if max_length == 0:
        print(f"|{'No tasks available. Add some.':^{dash_length-2}}|")
    for i in range(max_length):
        column = []
        for l in visible_lists:
            if i+1 <= len(lists[l]):
                column.append(f'{i+1:3}. {lists[l][i][:max_width-5]:{max_width-5}}')
            else:
                column.append(' ' * max_width)
        print(f"| {' | '.join(column)} |")
    print('-' * dash_length)