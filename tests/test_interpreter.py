import unittest

from javascrypthon.parser import parser


class TestInterpreter(unittest.TestCase):

    def test_simple_arithmetic_evaluation(self):
        root = parser.parse('1234 + 324')
        root.eval()
