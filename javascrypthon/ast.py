from copy import copy


class JSPYNode(object):
    pass


class JSPYRoot(JSPYNode):
    def __init__(self, statements, functions):
        self.functions_dict = functions
        self.statements_list = statements
        self.env = dict()

    def __eq__(self, other):
        return self.functions_dict == other.functions_dict \
            and self.statements_list == other.statements_list

    def eval(self):

        self.env.update(self.functions_dict)

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


class JSPYBoolean(JSPYNode):
    def __init__(self, value):
        if value == 'true':
            self.value = True
        else:
            self.value = False

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

    def __eq__(self, other):
        return self.name == other.name
        
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
        return self.name == other.name and \
        self.parameters == other.parameters and \
        self.body == other.body


class JSPYFunctionCall(JSPYNode):
    def __init__(self, name, bound_parameters):
        self.name = name
        self.bound_parameters = bound_parameters

    def __eq__(self, other):
        return self.name == other.name and \
            self.bound_parameters == other.bound_parameters

    def eval(self, env):
        if self.name.name in env:
            func = env[self.name.name]
        else:
            raise Exception('Function used before being declared: ' + self.name.name)

        bound_parameters = copy(self.bound_parameters)
        for param in func.parameters:
            # here I don't really want to pop the bound_parameters
            # what I really need to do is to progress in bound_parameters
            # at the same time that I go through func.parameters
            # there must be a better way to do that.
            value = bound_parameters.pop()
            env[param] = value.eval(env)

        for stmt in func.body:
            result = stmt.eval(env)

        return result


class JSPYIf(JSPYNode):
    def __init__(self, test, consequent, alternative=None):
        self.test = test
        self.consequent = consequent
        self.alternative = alternative

    def __eq__(self, other):
        return self.test == self.test and \
            self.consequent == other.consequent and \
            self.alternative == other.alternative

    def eval(self, env):
        if self.test.eval(env):
            return self.consequent.eval(env)
        elif self.alternative:
            return self.alternative.eval(env)
        else:
            # This is the case when there is only an 'if' without an 'else'
            # and at the same time the 'if' didn't evaluate to True in such
            # case we define that the 'if' expression value is None
            return None


class JSPYBlock(JSPYNode):
    def __init__(self, block):
        self.block = block

    def __eq__(self, other):
        return self.block == other.block

    def eval(self, env):
        for node in self.block:
            value = node.eval(env)

        return value


class JSPYEqualityTest(JSPYNode):
    def __init__(self, lhs, equality_type, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.equality_type = equality_type

    def __eq__(self, other):
        return self.lhs == other.lhs and \
            self.rhs == other.rhs and \
            self.equality_type == other.equality_type

    def eval(self, env):
        lhs_value = self.lhs.eval(env)
        rhs_value = self.rhs.eval(env)

        #TODO use the equality_test to determine which type of equality should be used
        return lhs_value == rhs_value
