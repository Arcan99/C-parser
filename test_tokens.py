import unittest
import tokens as t

class test_tokens(unittest.TestCase):
    def setUp(self) -> None:
        self.token_list = t.Token()
        return super().setUp()
    
    def test_tokens(self):
        self.assertEqual(self.token_list.get("set"), "=")
        self.assertEqual(self.token_list.get("open_parentheses"), "(")
        self.assertEqual(self.token_list.get("close_parentheses"), ")")
        self.assertEqual(self.token_list.get("comma"), ",")
        self.assertEqual(self.token_list.get("dot"), ".")
        self.assertEqual(self.token_list.get("open_brackets"), "[")
        self.assertEqual(self.token_list.get("close_brackets"), "]")
        self.assertEqual(self.token_list.get("open_curly_brackets"), "{")
        self.assertEqual(self.token_list.get("close_curly_brackets"), "}")
        self.assertEqual(self.token_list.get("quote"), "\"")
        self.assertEqual(self.token_list.get("single_quote"), "\'")
        self.assertEqual(self.token_list.get("equals"), "==")
        self.assertEqual(self.token_list.get("not_equals"), "!=")
        self.assertEqual(self.token_list.get("greater_than"), ">")
        self.assertEqual(self.token_list.get("greater_than_or_equal"), ">=")
        self.assertEqual(self.token_list.get("less_than"), "<")
        self.assertEqual(self.token_list.get("less_than_or_equal"), "<=")
        self.assertEqual(self.token_list.get("question_mark"), "?")
        self.assertEqual(self.token_list.get("star"), "*")
        self.assertEqual(self.token_list.get("plus"), "+")
        self.assertEqual(self.token_list.get("minus"), "-")
        self.assertEqual(self.token_list.get("divide"), "/")
        self.assertEqual(self.token_list.get("pointer_arrow"), "->")
        
    def test_invalid_key(self):
        self.assertEqual(self.token_list.get("not_a_key"), None)
        self.assertEqual(self.token_list.get("setcomma"), None)

