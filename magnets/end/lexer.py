# tokenize a string

tokens = ['if', 'fi', 'while', 'wend', 'fun', 'nuf']

keywords = (
    'READ', 'DATA', 'PRINT', 'GOTO', 'IF', 'THEN', 'FOR', 'NEXT', 'TO', 'WHILE',
    'END', 'DEF', 'GOSUB', 'DIM', 'REM', 'RETURN'
)


def get_filename():
    filename = raw_input("Enter a filename: ")
    assert isinstance(filename, object)
    return filename


def get_tokens():
    # type: () -> str
    for token in tokens:
        return token


def print_tokens():
    # type: () -> str
    for token in tokens:
        print token


def get_tokens_from_file(filename):
    for token in filename:
        return token
