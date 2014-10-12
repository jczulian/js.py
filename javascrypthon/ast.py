class JSPYNode(object):
    pass


class JSPYNumber(JSPYNode):
    def __init__(self, value):
        self.value = value


class JSPYString(JSPYNode):
    def __init__(self, value):
        self.value = value


class JSPYBinOp(JSPYNode):
    def __init__(self, operator, lhs, rhs):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs
