import unittest

from javascrypthon import lexer


class TestLexer(unittest.TestCase):

    def test_number(self):
        lexer.lexer.input('123')
        tok = lexer.lexer.next()
        self.assertEqual(tok.type, 'NUMBER')
        self.assertEqual(tok.value, 123)

    def test_simple_binary_op(self):
        lexer.lexer.input('123 + 568')

        token1 = lexer.lexer.token()
        self.assertEqual(token1.type, 'NUMBER')
        self.assertEqual(token1.value, 123)

        token2 = lexer.lexer.token()
        self.assertEqual(token2.type, 'PLUS')
        self.assertEqual(token2.value, '+')

        token3 = lexer.lexer.token()
        self.assertEqual(token3.type, 'NUMBER')
        self.assertEqual(token3.value, 568)

    def test_simple_string(self):
        lexer.lexer.input('"coucou la string."')

        token = lexer.lexer.token()
        self.assertEqual(token.type, 'STRING')
        self.assertEqual(token.value, "coucou la string.")

