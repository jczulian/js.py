class JSPYNode(object):
    pass


class JSPYRoot(JSPYNode):
    def __init__(self, statements, functions):
        self.functions_list = functions
        self.statements_list = statements
        self.env = dict()

    def __eq__(self, other):
        return self.functions_list == other.functions_list \
            and self.statements_list == other.statements_list

    def eval(self):
        for function in self.functions_list:
            function.eval(self.env)

        last_stmt_value = None
        for statement in self.statements_list:
            last_stmt_value = statement.eval(self.env)

        return last_stmt_value


class JSPYStatement(JSPYNode):

    def __init__(self, node):
        self.statement = node

    def __eq__(self, other):
        return self.statement == other.statement

    def eval(self, env):
        value = self.statement.eval(env)
        return value


class JSPYNumber(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def eval(self, env):
        return self.value


class JSPYString(JSPYNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def eval(self, env):
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

    def eval(self, env):
        lhs_value = self.lhs.eval(env)
        rhs_value = self.rhs.eval(env)

        # idealy here we should instead do a lookup on the environment to find
        # the arithmetic function we are looking for
        if self.operator == '+':
            return lhs_value.__add__(rhs_value)
        elif self.operator == '-':
            return lhs_value.__sub__(rhs_value)
        elif self.operator == '*':
            return lhs_value.__mul__(rhs_value)
        elif self.operator == '/':
            return lhs_value.__div__(rhs_value)


class JSPYUndefined(JSPYNode):
    def eval(self, env):
        return self


class JSPYAssignment(JSPYNode):
    def __init__(self, var_name, var_value_node):
        self.var_name = var_name
        self.var_value_node = var_value_node

    def eval(self, env):
        env[self.var_name] = self.var_value_node.eval(env)


class JSPYException(Exception):
    pass


class JSPYVariable(JSPYNode):
    def __init__(self, name):
        self.name = name
        
    def eval(self, env):
        if env.has_key(self.name):
            return env[self.name]
        else:
            raise JSPYException('Unbound variable: %s' % self.name)


class JSPYFunction(JSPYNode):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __eq__(self, other):
        self.name == other.name and \
        self.arguments == other.arguments and \
        self.body == other.body

