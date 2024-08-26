import os

def display(selected_lists: list, lists: dict) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    max_length = 0
    max_width = 25
    for l in selected_lists:
        length = len(lists[l])
        if length > max_length:
            max_length = length
        width = len(l)
        if width > max_width:
            max_width = width
    
    dash_length = (len(selected_lists) * (max_width+3))+1
    print('-' * dash_length)
    formatted_headers = [f'{header:^{max_width}}' for header in selected_lists]
    print(f"| {' | '.join(formatted_headers)} |")
    print('-' * dash_length)
    for i in range(max_length):
        column = []
        for l in selected_lists:
            if i+1 <= len(lists[l]):
                column.append(f'{i+1:3}. {lists[l][i][:max_width-5]:{max_width-5}}')
            else:
                column.append(' ' * max_width)
        print(f"| {' | '.join(column)} |")
    print('-' * dash_length)