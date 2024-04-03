import sys
input = sys.stdin.readline


def postfix_notation(case, i):
    stack = []
    logic_stack = []
    paranth_stack = []
    while i < len(case):
        if case[i] == '(':
            case[i + 1:] = postfix_notation(case, i + 1)
        elif case[i] == ')':
            stack += case[i+1:]
            break
        else:
            if case[i] in ['+', '-']:
                logic_stack.append(case[i])
            elif case[i] in ['/', '*']:
                paranth_stack.append(case[i])
            else:
                if paranth_stack:
                    stack.append(stack.pop() + case[i] + paranth_stack.pop())
                else:
                    stack.append(case[i])
        i += 1
    while logic_stack:
        stack = [(stack.pop(0) + stack.pop(0) + logic_stack.pop(0))] + stack

    return stack

case = list(input().strip())
print(*postfix_notation(case, 0))

