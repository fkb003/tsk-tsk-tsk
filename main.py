from interpret import interpret

lists = {
    'default': [],
    'done': [],
    'skipped': []
}

selected_list = 'default'

while True:
    # Display tasks
    for i, task in enumerate(lists[selected_list]):
        print(f'{i+1:3}. {task}')

    interpret(input('>>> '), selected_list, lists)