tasks = [] # List to store tasks
done = [] # List to store completed tasks
skipped = [] # List to store skipped tasks

def act(cmd):
    if not cmd: exit()
    elif cmd[0] == '.':
        # Pop task from tasks to done list
        done.append(tasks.pop(int(cmd[1:])-1))
    elif cmd[0] == '#':
        skipped.append(tasks.pop(int(cmd[1:])-1))
    else: tasks.append(cmd)

while True:
    # Display tasks
    for i, task in enumerate(tasks):
        print(f'{i+1:3}. {task}')

    # Take commands and process them
    command = input('>>> ')
    act(command)