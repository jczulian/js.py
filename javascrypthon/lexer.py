import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'DOUBLE_EQUAL',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'SEMI_CO',
    'COLUMN',
    'NUMBER',
    'STRING',
    'IDENT'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_DOUBLE_EQUAL = r'=='
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_SEMI_CO = r';'
t_COLUMN = r','

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'true': 'BOOLEAN',
    'false': 'BOOLEAN'
}

tokens = tokens + tuple(reserved.values())


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value[1:-1])
    return t


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENT')    # Check for reserved words
    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()
