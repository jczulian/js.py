import unittest

from javascrypthon.parser import parser


class TestParser(unittest.TestCase):
    def test_arithmetic_parsing(self):
        self.assertEqual(1, 1)
        bla = parser.parse('1234 + 324')
        print bla
