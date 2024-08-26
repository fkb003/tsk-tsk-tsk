from interpret import interpret
from display import display
lists = {
    'default': [],
    'done': [],
    'skipped': []
}

selected_lists = ['default', 'done', 'skipped']

while True:
    display(selected_lists, lists)
    interpret(input('>>> '), selected_lists, lists)