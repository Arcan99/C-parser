import unittest
from main.filereader import File_reader

class test_reader(unittest.TestCase):
    def setUp(self) -> None:
        self.r = File_reader("test_files/main1.txt")
        return super().setUp()
    
    def test_readNextLine(self):
        line = self.r.readNextLine()
        self.assertEqual(line, "\n")
        
        line = self.r.readNextLine()
        self.assertEqual(line, "start\n")
        
        line = self.r.readNextLine()
        self.assertEqual(line, "    set integer x to 5\n")
        
        line = self.r.readNextLine()
        self.assertEqual(line, "    set character c to 'c'\n")
        
        line = self.r.readNextLine()
        self.assertEqual(line, '    set String s to "Hello"\n')
        
        line = self.r.readNextLine()
        self.assertEqual(line, "end\n")
        
        line = self.r.readNextLine()
        self.assertEqual(line, None)
        
    def test_getNewTokens(self):
        tokens = self.r.getNewTokens()
        self.assertListEqual(tokens, ["start"])
        
        tokens = self.r.getNewTokens()
        self.assertListEqual(tokens, ['set', 'integer', 'x', 'to', '5'])
        
        tokens = self.r.getNewTokens()
        self.assertListEqual(tokens, ['set', 'character', 'c', 'to', "'c'"])
        
        tokens = self.r.getNewTokens()
        self.assertListEqual(tokens, ['set', 'String', 's', 'to', '"Hello"'])
        
        tokens = self.r.getNewTokens()
        self.assertListEqual(tokens, ['end'])
        
        tokens = self.r.getNewTokens()
        self.assertIsNone(tokens)