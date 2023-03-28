import unittest
from unittest.mock import _patch

from main.codegenerator import Generator

class test_generator(unittest.TestCase):
    def setUp(self) -> None:
        self.tokens = ["token1", "token2", "token3"]
        return super().setUp()
    
    def test_setConverterSentence(self):
        g = Generator("test_files/test_cases/main1.txt", "test_files/test_results/main0test.c")
        g.currentLine = []
        g.setConverterSentence()
        self.assertListEqual(g.converter.tokens, [])
        
        g.currentLine = self.tokens
        g.setConverterSentence()
        self.assertListEqual(g.converter.tokens, self.tokens)
        
        g.currentLine = []
        g.setConverterSentence()
        self.assertListEqual(g.converter.tokens, [])
        
    def saveResultMock(self, line, indent):
        self.g.currentLine = ["end"]
        
        
    def run_convertBody(self):
        g = Generator("test_files/test_cases/testBody.txt", "test_files/test_results/convertBody_test.c")
        g.currentLine = ["set", "integer", "x", "to", "5"]
        g.setConverterSentence()
        g.convertBody()
     
    def test_convertBody(self):
        self.run_convertBody()
        f = open("test_files/test_results/convertBody_test.c", "r")
        t = open("test_files/test_targets/testBody_target.c", "r")
        
        target_line = t.readline()
        generated_line = f.readline()
        while not target_line == "":
            self.assertEqual(generated_line, target_line)
            target_line = t.readline()
            generated_line = f.readline()
            
        f.close()
            
            
    def run_convertMain(self):
        g = Generator("test_files/test_cases/testMain.txt", "test_files/test_results/convertMain_test.c")
        g.convertMain()
        
    def test_convertMain(self):
        self.run_convertMain()
        f = open("test_files/test_results/convertMain_test.c", "r")
        t = open("test_files/test_targets/testMain_target.c", "r")
        
        target_line = t.readline()
        generated_line = f.readline()
        while not target_line == "":
            self.assertEqual(generated_line, target_line)
            target_line = t.readline()
            generated_line = f.readline()
            
        f.close()