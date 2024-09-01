import os

def display(selected_lists: list, lists: dict) -> None:
    clear_screen()
    terminal_size = os.get_terminal_size().columns
    visible_lists = selected_lists[1:]
    if not lists['done']:
        visible_lists.pop(-2)
        if selected_lists[0] == 'done': selected_lists[0] = 'default'
    if not lists['skipped']:
        visible_lists.pop(-1)
        if selected_lists[0] == 'skipped': selected_lists[0] = 'default'
    max_length = 0
    max_width = min(80, int((terminal_size/len(visible_lists))-3.5))
    for l in visible_lists:
        length = len(lists[l])
        if length > max_length:
            max_length = length
    
    dash_length = (len(visible_lists) * (max_width+3))+1
    print('-' * dash_length)
    print_headers(selected_lists[0], visible_lists,  max_width)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_headers(selected_list: str, visible_lists: list, header_width: int) -> None:

    # Centering individual headers
    centered_headers = [f'{header:^{header_width}}' for header in visible_lists]

    # ANSI escape codes
    UNDERLINED = '\033[4m'
    RESET = '\033[0m'

    # Styling header of selected list
    styled = f'{UNDERLINED + selected_list + RESET}'
    pos = visible_lists.index(selected_list)

    # Injecting the styled header
    centered_headers[pos] = centered_headers[pos].replace(selected_list, styled)

    # Printing formatted headers
    formatted_headers = f"| {' | '.join(centered_headers)} |"
    print(formatted_headers)
