import unittest
from javascrypthon.ast import JSPYException

from javascrypthon.parser import parser


class TestInterpreter(unittest.TestCase):

    def test_simple_arithmetic_evaluation(self):
        root = parser.parse('12 + 34')
        self.assertEqual(46, root.eval())

    def test_just_a_string(self):
        root = parser.parse('"Hello world!"')
        self.assertEqual("Hello world!", root.eval())

    def test_array_literal(self):
        pass

    def test_object_literal(self):
        pass

    def test_assignment(self):
        root = parser.parse("var x = 12 + 23")
        root.eval()
        self.assertIsNotNone(root.env.get('x', None), 'x should have been recorded in the env')
        self.assertEqual(35, root.env['x'])

    def test_using_assigned_variable(self):
        root = parser.parse("var x = 12; var y = x + 3")
        root.eval()

    def test_unbound_variable(self):
        root = parser.parse("var x = y + 2")
        self.assertRaises(JSPYException, root.eval, *[])

    def test_function_declaration(self):
        pass

    def test_function_call(self):
        pass

    def test_closure(self):
        pass

    def test_json(self):
        pass
