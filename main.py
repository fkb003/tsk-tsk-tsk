tasks = [] # List to store tasks

while True:
    # Print tasks
    for i, task in enumerate(tasks):
        print(f'{i+1:3}. {task}')
    
    # Input new tasks, if empty, break loop.
    cmd = input('>>> ')
    if cmd: tasks.append(cmd)
    else: break