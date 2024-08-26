from interpret import interpret
from display import display
lists = {
    'default': [],
    'done': [],
    'skipped': []
}

selected_list = ['default']

while True:
    display(selected_list, lists)
    interpret(input('>>> '), selected_list, lists)