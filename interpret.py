import action

def interpret(cmd: str, selected_lists: list, lists: dict) -> None: 
    """Call other functions and pass identified arguments"""
    if cmd[0] in action.menu:
        operator = cmd[0]
        if is_index(cmd[1:]):
            operand = int(cmd[1:])
            if operand > 0: operand -= 1
        else:
            operand = cmd[1:]
        action.menu[operator](operand, selected_lists, lists)
    else:
        action.menu['add'](cmd, selected_lists, lists)

def is_index(s: str) -> bool: 
    """Test if given string is a valid index"""
    if not s:
        return False
    if s.isdigit():
        return True
    if s[0]=='-' and s[1:].isdigit():
        return True
    return False