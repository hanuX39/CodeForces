def balanced(str):
    l = []
    lefty = '({['
    righty = ')}]'
    for char in str:
        if char in lefty:
            l.append(char)
        elif char in righty:
            if len(l) == 0:
                return False
            elif righty.index(char) != lefty.index(l.pop()):
                return False
    return len(l) == 0


print(balanced('[{(}]'))