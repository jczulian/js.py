from javascrypthon.parser import parser


class JSPYInterpreter(object):

    def __init__(self):
        pass

    def interpret_js(self, code_string):
        ast_root = parser.parse(code_string)

        env = dict()

        for function in ast_root.functions_list:
            self.interpret_function(function, env)

        for statement in ast_root.statements_list:
            self.interpre_statement(statement, env)
