class JSPYNode(object):
    pass


class JSPYRoot(JSPYNode):
    def __init__(self, statements, functions):
        self.functions_list = functions
        self.statements_list = statements

    def __eq__(self, other):
        return self.functions_list == other.functions_list \
            and self.statements_list == other.statements_list

    def eval(self):
        for function in self.functions_list:
            function.eval()

        for statement in self.statements_list:
            statement.eval()


class JSPYStatement(JSPYNode):

    def __init__(self, node):
        self.statement = node

    def __eq__(self, other):
        return self.statement == other.statement

    def eval(self):
        value = self.statement.eval()
        print value


class JSPYNumber(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def eval(self):
        return self.value


class JSPYString(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def eval(self):
        return self.value


class JSPYBinOp(JSPYNode):
    def __init__(self, operator, lhs, rhs):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, other):
        return self.operator == other.operator \
            and self.lhs == other.lhs \
            and self.rhs == other.rhs

    def eval(self):
        lhs_value = self.lhs.eval()
        rhs_value = self.rhs.eval()

        if self.operator == '+':
            return lhs_value.__add__(rhs_value)
        elif self.operator == '-':
            return lhs_value.__sub__(rhs_value)
        elif self.operator == '*':
            return lhs_value.__mul__(rhs_value)
        elif self.operator == '/':
            return lhs_value.__div__(rhs_value)
