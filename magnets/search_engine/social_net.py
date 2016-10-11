def union(a, b):
    for element in a:
        if element not in b:
            b.append(element)
    return b


def add_new_elem_to_new(a, b, c):
    for element in a:
        if element not in b:
            c.append(element)
    return c
