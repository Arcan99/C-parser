import unittest
import mock
from unittest.mock import MagicMock

from main.codegenerator import Generator

class test_generator(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Generator("test_files/main1.txt", "test_results/main1test.c")
        self.tokens = ["token1", "token2", "token3"]
        return super().setUp()
    
    def test_setConverterSentence(self):
        self.g.currentLine = []
        self.g.setConverterSentence()
        self.assertListEqual(self.g.converter.tokens, [])
        
        self.g.currentLine = self.tokens
        self.g.setConverterSentence()
        self.assertListEqual(self.g.converter.tokens, self.tokens)
        
        self.g.currentLine = []
        self.g.setConverterSentence()
        self.assertListEqual(self.g.converter.tokens, [])
        
    def saveResultMock(self, line, indent):
        self.g.currentLine = ["end"]
        
     
    def test_convertBody(self):
        with mock.patch.object(Generator, 'saveResult', new=self.saveResultMock) as mock_save:
            self.g.currentLine = ["set", "integer", "x", "to", "5"]
            self.g.setConverterSentence()
            self.g.convertBody()
            mock_save.assert_called_with("int x = 5;", 1)
            