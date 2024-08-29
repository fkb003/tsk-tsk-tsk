import os

def display(selected_lists: list, lists: dict) -> None:
    clear_screen()
    terminal_size = min(120, os.get_terminal_size().columns)
    visible_lists = selected_lists[1:]
    max_length = 0
    max_width = int((terminal_size/len(visible_lists))-3.5)
    for l in visible_lists:
        length = len(lists[l])
        if length > max_length:
            max_length = length
    
    dash_length = (len(visible_lists) * (max_width+3))+1
    print('-' * dash_length)
    print_headers(selected_lists, max_width)
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

def print_headers(selected_lists: list, header_width: int) -> None:

    visible_lists = selected_lists[1:]

    # Centering individual headers
    centered_headers = [f'{header:^{header_width}}' for header in visible_lists]

    # ANSI escape codes
    UNDERLINED = '\033[4m'
    RESET = '\033[0m'

    # Styling header of selected list
    original = selected_lists[0]
    styled = f'{UNDERLINED + original + RESET}'
    pos = visible_lists.index(original)

    # Injecting the styled header
    centered_headers[pos] = centered_headers[pos].replace(original, styled)

    # Printing formatted headers
    formatted_headers = f"| {' | '.join(centered_headers)} |"
    print(formatted_headers)