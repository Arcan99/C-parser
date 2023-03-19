import unittest
from main.tokenindex import Token_index

class test_converter(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    
    def test_getType(self):
        res = Token_index.getType("Not a type")
        self.assertIsNone(res)
        
        res = Token_index.getType("integer")
        self.assertEqual(res, "int")
        
        res = Token_index.getType("character")
        self.assertEqual(res, "char")
        
        res = Token_index.getType("String")
        self.assertEqual(res, "char*")
        
        
    def test_typeExists(self):
        res = Token_index.typeExists("Not a type")
        self.assertFalse(res)
        
        res = Token_index.typeExists("integer")
        self.assertTrue(res)
        
        res = Token_index.typeExists("character")
        self.assertTrue(res)
        
        res = Token_index.typeExists("String")
        self.assertTrue(res)
        