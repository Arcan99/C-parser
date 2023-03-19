import unittest
from main.codeconverter import Converter

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
        self.assertIsNone(self.c.start())
        
        self.c.setCurrentSentence(["start"])
        self.assertEqual(self.c.start(), "int main(int argc, char* argv) {")
        
    def test_end(self):
        self.assertIsNone(self.c.end())
        
        self.c.setCurrentSentence(["end"])
        self.assertEqual(self.c.end(), "return 0;\n}")
        
        self.c.setCurrentSentence(["end"])
        self.assertEqual(self.c.end(10), "return 10;\n}")
        
    def test_set(self):
        self.assertIsNone(self.c.set())
        
        self.c.setCurrentSentence(["set", "integer", "x", "to", "10"])
        self.assertEqual(self.c.set(), "int x = 10;")
        self.assertIsNone(self.c.set())
        
        self.c.setCurrentSentence(["set", "integer", "test_var", "to", "100"])
        self.assertEqual(self.c.set(), "int test_var = 100;")
        
        self.c.setCurrentSentence(["set", "int", "test_var", "to", "100"])
        self.assertIsNone(self.c.set())
        
        self.c.setCurrentSentence(["set", "int", "test_var", "to0", "100"])
        self.assertIsNone(self.c.set())