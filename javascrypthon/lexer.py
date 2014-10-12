import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()
