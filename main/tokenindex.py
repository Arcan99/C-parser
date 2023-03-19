# Handle token translation

class Token_index:
    
    def getTypes() -> dict:
        return {
            "integer": "int",
            "character": "char",
            "String": "char*"
        }
        
    def getType(key: str):
        return Token_index.getTypes().get(key)
        
    def typeExists(type):
        return type in Token_index.getTypes().keys()
    

    
    
if __name__ == "__main__":
    print(Token_index.typeExists("integer"))
    print(Token_index.typeExists("qweqweqwe"))