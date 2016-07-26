""" Kyoubukai
"""


def print_lines_from_file(filename=None):
    # type: (Union) -> str

    f = open(filename, 'r')

    for line in f:
        print line,


print_lines_from_file('test')


def print_bytes_from_file(filename=None, size=None):
    f = open(filename, 'r')
    byte = f.read(size)
    print byte


print_bytes_from_file('test2', 2)
