from ply import yacc
from javascrypthon.ast import JSPYBinOp, JSPYNumber, JSPYRoot, JSPYStatement


def p_program(p):
    """
    program : top_statements
    """
    statements = list()
    functions = list()

    for stmt in p[1]:
        if isinstance(stmt, JSPYStatement):
            statements.append(stmt)
        else:
            functions.append(stmt)

    p[0] = JSPYRoot(statements=statements, functions=functions)


def p_top_statements(p):
    """
    top_statements : top_statements top_statement
                   | empty
    """
    if len(p) == 2:
        p[0] = list()
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_top_statement(p):
    """
    top_statement : statement
                  | function_definition
    """
    p[0] = p[1]


def p_function_definition(p):
    """
    function_definition : empty
    """


def p_statement(p):
    """
    statement : expression_statement optional_semicolon
    """
    p[0] = JSPYStatement(node=p[1])


def p_optional_semicolon(p):
    """
    optional_semicolon : ';'
                       | empty
    """
    pass


def p_expression_statement(p):
    """
    expression_statement : expression
    """
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_simple_expression(p):
    """
    simple_expression : NUMBER
                      | parenthesized_expression
    """
    p[0] = JSPYNumber(p[1])


def p_parenthesized_expression(p):
    """
    parenthesized_expression : '(' expression ')'
    """
    p[0] = p[2]


def p_expression(p):
    """
    expression : assignment_expression
               | expression ',' assignment_expression
               | empty
    """
    p[0] = p[1]


def p_assignment_expression(p):
    """
    assignment_expression : conditional_expression
    """
    p[0] = p[1]


def p_conditional_expression(p):
    """
    conditional_expression : logical_or_expression
    """
    p[0] = p[1]


def p_logical_or_expression(p):
    """
    logical_or_expression : logical_and_expression
                          | logical_or_expression '|' logical_and_expression
    """
    p[0] = p[1]


def p_logical_and_expression(p):
    """
    logical_and_expression : bitwise_or_expression
                          | logical_and_expression '&' bitwise_or_expression
    """
    p[0] = p[1]


def p_bitwise_or_expression(p):
    """
    bitwise_or_expression : bitwise_and_expression
    """
    p[0] = p[1]


def p_bitwise_and_expression(p):
    """
    bitwise_and_expression : equality_expression
    """
    p[0] = p[1]


def p_equality_expression(p):
    """
    equality_expression : relational_expression
    """
    p[0] = p[1]


def p_relational_expression(p):
    """
    relational_expression : shift_expression
    """
    p[0] = p[1]


def p_shift_expression(p):
    """
    shift_expression : additive_expression
    """
    p[0] = p[1]


def p_additive_expression(p):
    """
    additive_expression : multiplicative_expression
                        | additive_expression PLUS multiplicative_expression
                        | additive_expression MINUS multiplicative_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        node = JSPYBinOp(p[2], p[1], p[3])
        p[0] = node


def p_multiplicative_expression(p):
    """
    multiplicative_expression : unary_expression
                              | multiplicative_expression MULTIPLY unary_expression
                              | multiplicative_expression DIVIDE unary_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        node = JSPYBinOp(p[2], p[1], p[3])
        p[0] = node


def p_unary_expression(p):
    """
    unary_expression : postfix_expression
    """
    p[0] = p[1]


def p_postfix_expression(p):
    """
    postfix_expression : left_side_expression
    """
    p[0] = p[1]


def p_left_side_expression(p):
    """
    left_side_expression : call_expression
    """
    p[0] = p[1]


def p_call_expression(p):
    """
    call_expression : primary_expression
    """
    p[0] = p[1]


def p_primary_expression(p):
    """
    primary_expression : simple_expression
    """
    p[0] = p[1]


parser = yacc.yacc(debug=1)
