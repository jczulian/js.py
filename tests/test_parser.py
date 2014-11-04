import unittest
from javascrypthon.ast import JSPYRoot, JSPYNumber, JSPYBinOp, JSPYStatement, JSPYString, JSPYVariable, JSPYFunction

from javascrypthon.parser import parser


class TestParser(unittest.TestCase):
    def test_arithmetic_parsing(self):
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

    def test_string_parsing(self):
        root = parser.parse('"coucou je suis une string."')

        expected = JSPYRoot(
            statements=[
                JSPYStatement(
                    node=JSPYString(value="coucou je suis une string.")
                )
            ],
            functions=[]
        )

        self.assertEqual(root, expected)

    def test_function_declaration_parsing(self):
        root = parser.parse("function func(x, y) { x + y }")

        expected = JSPYRoot(
            statements=[
            ],
            functions=[
                JSPYFunction(
                    name='func',
                    parameters=['x', 'y'],
                    body=JSPYStatement(
                        JSPYBinOp(
                            lhs=JSPYVariable(name='x'),
                            rhs=JSPYVariable(name='y'),
                            operator='+'
                        )
                    )
                )
            ]
        )

