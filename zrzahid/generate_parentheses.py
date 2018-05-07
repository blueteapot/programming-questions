def generate_parentheses(lst, current_str, left, right):

    if left == 0 and right == 0:
        lst.append(current_str)
        return lst

    if right > 0:
        generate_parentheses(lst, current_str + ")", left, right - 1)
    if left > 0:
        generate_parentheses(lst, current_str + "(", left - 1, right + 1)

    return lst

print(generate_parentheses([], "", 5, 0))
