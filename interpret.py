import action

def interpret(cmd: str, selected_lists: list, lists: dict) -> None: 
    """Call other functions and pass identified arguments"""
    if not cmd: pass
    elif cmd[0] in action.menu:
        operator = cmd[0]
        index_test = is_index(cmd[1:])
        if index_test[0]:
            operand = index_test[1]
        else:
            operand = cmd[1:]
        action.menu[operator](operand, selected_lists, lists)
    else:
        action.menu['add'](cmd, selected_lists, lists)

def is_index(s: str) -> tuple: 
    """Test if given string is a valid index"""
    if not s:
        return (False,)
    if s.isdigit():
        if int(s)>0:
            return (True, int(s)-1)
        else:
            return (True, int(s))
    if s[0]=='-' and s[1:].isdigit():
        return (True, int(s))
    return (False,)