def p_program(p):
    """
    program : top_statement
    """


def p_top_statement(p):
    """
    top_statement : statement
    """


def p_statement(p):
    """
    statement : expression_statement optional_semicolon
    """


def p_optional_semicolon(p):
    """
    optional_semicolon : ';'
                       | empty
    """


def p_expression_statement(p):
    """
    expression_statement : expression
    :param p:
    :return:
    """


def p_empty(p):
    """
    empty :
    """
    pass


def p_simple_expression(p):
    """
    simple_expression : Number
                      | parenthesized_expression
    """


def p_parenthesized_expression(p):
    """
    parenthesized_expression : '(' expression ')'
    """


def p_expression(p):
    """
    expression : assignment_expression
               | expression ',' assignment_expression
               | empty
    :param p:
    :return:
    """


def p_assignment_expression(p):
    """
    assignment_expression : conditional_expression
    """


def p_conditional_expression(p):
    """
    conditional_expression : logical_or_expression
    """


def p_logical_or_expression(p):
    """
    logical_or_expression : logical_and_expression
                          | logical_or_expression '||' logical_and_expression
    """


def p_logical_and_expression(p):
    """
    logical_and_expression : bitwise_or_expression
                          | logical_and_expression '&&' bitwise_and_expression
    """


def p_bitwise_and_expression(p):
    """
    bitwise_and_expression : equality_expression
    """


def p_equality_expression(p):
    """
    equality_expression : relational_expression
    """


def p_relational_expression(p):
    """
    relational_expression : shift_expression
    """


def p_shift_expression(p):
    """
    shift_expression : additive_expression
    """


def p_additive_expression(p):
    """
    additive_expression : multiplicative_expression
                        | additive_expression '+' multiplicative_expression
                        | additive_expression '-' multiplicative_expression
    """


def p_multiplicative_expression(p):
    """
    multiplicative_expression : unary_expression
                              | multiplicative_expression '*' unary_expression
                              | multiplicative_expression '/' unary_expression
    """


def p_unary_expression(p):
    """
    unary_expression : postfix_expression
    """


def p_postfix_expression(p):
    """
    postfix_expression : left_side_expression
    """


def p_left_side_expression(p):
    """
    left_side_expression : call_expression
    """


def p_call_expression(p):
    """
    call_expression : primary_expression
    """


def p_primary_expression(p):
    """
    primary_expression : simple_expression
    """
