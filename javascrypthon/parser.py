from ply import yacc
from javascrypthon.ast import JSPYBinOp, JSPYNumber, JSPYRoot, JSPYStatement, JSPYString, JSPYAssignment, JSPYVariable, \
    JSPYFunction, JSPYFunctionCall, JSPYIf, JSPYEqualityTest

from javascrypthon.lexer import tokens


def p_program(p):
    """
    program : top_statements
    """
    statements = list()
    functions = dict()

    for stmt in p[1]:
        if isinstance(stmt, JSPYStatement):
            statements.append(stmt)
        else:
            func = stmt
            functions[func.name] = func

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
    function_definition : named_function
    """
    p[0] = p[1]


def p_named_function(p):
    """
    named_function : FUNCTION IDENT formal_parameters_and_body
    """
    parameters, body = p[3]
    name = p[2]
    function = JSPYFunction(name=name, parameters=parameters, body=body)

    p[0] = function


def p_formal_parameters_and_body(p):
    """
    formal_parameters_and_body : LPAREN formal_parameters RPAREN LCURLY top_statements RCURLY
    """
    p[0] = [p[2], p[5]]


def p_formal_parameters(p):
    """
    formal_parameters : empty
                      | formal_parameters_prefix
    """
    if p.slice[1].type == 'empty':
        p[0] = []
    else:
        p[0] = p[1]


def p_formal_parameters_prefix(p):
    """
    formal_parameters_prefix : formal_parameter
                             | formal_parameters_prefix COLUMN formal_parameter
    """
    # TODO make sure that parameter names are unique among themselves
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_formal_parameter(p):
    """
    formal_parameter : IDENT
    """
    p[0] = p[1]


def p_statement(p):
    """
    statement : if_statement
              | expression_statement optional_semicolon
              | variable_definition optional_semicolon
              | block
    """
    p[0] = JSPYStatement(node=p[1])


def p_optional_semicolon(p):
    """
    optional_semicolon : SEMI_CO
                       | empty
    """
    pass


def p_empty_statement(p):
    """
    empty_statement : SEMI_CO
    """
    pass


def p_block(p):
    """
    block : LCURLY block_statements RCURLY
    """
    p[0] = p[2]


def p_block_statements(p):
    """
    block_statements : empty
                     | block_statements_prefix
    """
    p[0] = p[1]


def p_block_statements_prefix(p):
    """
    block_statements_prefix : statement
                            | block_statements_prefix statement

    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_if_statement(p):
    """
    if_statement : IF parenthesized_expression statement
                 | IF parenthesized_expression statement ELSE statement
    """
    if len(p) == 4:
        p[0] = JSPYIf(test=p[2], consequent=p[3])
    else:
        p[0] = JSPYIf(test=p[2], consequent=p[3], alternative=p[4])


def p_variable_definition(p):
    """
    variable_definition : VAR IDENT variable_initializer
    """
    p[0] = JSPYAssignment(var_name=p[2], var_value_node=p[3])


def p_variable_initialiser(p):
    """
    variable_initializer : EQUAL assignment_expression
                         | empty
    """
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[2]


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
    simple_expression : IDENT
                      | NUMBER
                      | STRING
                      | parenthesized_expression
    """
    if p.slice[1].type == 'IDENT':
        p[0] = JSPYVariable(p[1])
    elif p.slice[1].type == 'NUMBER':
        p[0] = JSPYNumber(p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = JSPYString(p[1])
    else:
        raise Exception('Unknown simple expression encountered.')


def p_parenthesized_expression(p):
    """
    parenthesized_expression : LPAREN expression RPAREN
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
                        | equality_expression DOUBLE_EQUAL relational_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = JSPYEqualityTest(lhs=p[1], equality_type=p[2], rhs=p[3])


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
                    | call_expression arguments
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = JSPYFunctionCall(name=p[1], bound_parameters=p[2])


def p_arguments(p):
    """
    arguments : LPAREN arguments_list RPAREN
    """
    p[0] = p[2]


def p_arguments_list(p):
    """
    arguments_list : assignment_expression
                   | arguments_list COLUMN assignment_expression
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_primary_expression(p):
    """
    primary_expression : simple_expression
    """
    p[0] = p[1]


parser = yacc.yacc(debug=1)
