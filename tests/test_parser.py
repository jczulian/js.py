import unittest
from javascrypthon.ast import JSPYRoot, JSPYNumber, JSPYBinOp, JSPYStatement

from javascrypthon.parser import parser


class TestParser(unittest.TestCase):
    def test_arithmetic_parsing(self):
        self.assertEqual(1, 1)
        root = parser.parse('1234 + 324')

        expected = JSPYRoot(
            statements=[
                JSPYStatement(
                    node=JSPYBinOp(
                        operator='+',
                        lhs=JSPYNumber(1234),
                        rhs=JSPYNumber(324),
                    )
                )
            ],
            functions=[]
        )

        self.assertEqual(root, expected)
