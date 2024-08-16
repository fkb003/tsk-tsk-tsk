tasks = [] # List to store tasks
done = [] # List to store completed tasks
skipped = [] # List to store skipped tasks

while True:
    # Print tasks
    for i, task in enumerate(tasks):
        print(f'{i+1:3}. {task}')
    
    # Input new tasks, if empty, break loop.
    cmd = input('>>> ')
    if not cmd: break
    elif cmd[0] == '.':
        # Pop task from tasks to done list
        done.append(tasks.pop(int(cmd[1:])-1))
    elif cmd[0] == '#':
        skipped.append(tasks.pop(int(cmd[1:])-1))
    else: tasks.append(cmd)