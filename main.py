from interpret import interpret
from display import display
import readline
lists = {
    'default': [],
    'done': [],
    'skipped': []
}

selected_lists = ['default', 'default', 'done', 'skipped']

while True:
    display(selected_lists, lists)
    interpret(input('>>> '), selected_lists, lists)