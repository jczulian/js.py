class JSPYNode(object):
    pass


class JSPYRoot(JSPYNode):
    def __init__(self, statements, functions):
        self.functions_list = functions
        self.statements_list = statements

    def __eq__(self, other):
        return self.functions_list == other.functions_list \
            and self.statements_list == other.statements_list


class JSPYStatement(JSPYNode):

    def __init__(self, node):
        self.statement = node

    def __eq__(self, other):
        return self.statement == other.statement


class JSPYNumber(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class JSPYString(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class JSPYBinOp(JSPYNode):
    def __init__(self, operator, lhs, rhs):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, other):
        return self.operator == other.operator \
            and self.lhs == other.lhs \
            and self.rhs == other.rhs
