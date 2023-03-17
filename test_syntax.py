import unittest
from codegenerator import Converter, Token_index

class test_converter(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Converter()
        return super().setUp()
    
    def test_setCurrentSentence(self):
        self.c.setCurrentSentence([])
        self.assertListEqual(self.c.tokens, [])
        
        self.c.setCurrentSentence(["token1", "token2"])
        self.assertListEqual(self.c.tokens, ["token1", "token2"])
        
        with self.assertRaises(TypeError):
            self.c.setCurrentSentence("Not a list")
        
        
    def test_getSentenceLenght(self):
        self.c.setCurrentSentence([])
        self.assertEqual(self.c.getSentenceLenght(), 0)
        
        self.c.setCurrentSentence(["token1", "token2"])
        self.assertEqual(self.c.getSentenceLenght(), 2)
        
    def test_getFirstToken(self):
        self.assertIsNone(self.c.getFirstToken())
        self.c.setCurrentSentence(["token1", "token2"])
        self.assertEqual(self.c.getFirstToken(), "token1")

    def test_match(self):
        self.assertFalse(self.c.match("token1"))
        self.c.setCurrentSentence(["token1", "token2"])
        self.assertTrue(self.c.match("token1"))
        self.assertFalse(self.c.match("token1"))
        self.assertTrue(self.c.match("token2"))
        self.assertFalse(self.c.match("token2"))
        
    def test_start(self):
        self.assertTrue(False)