# Handle token translation

class Token_index:
    def getTypes() -> dict:
        return {
            "integer": "int",
            "character": "char",
            "String": "char*"
        }
        
    def typeExists(tpye: str):
        return type in Token_index.getTypes()
    
    def getType(key: str):
        return Token_index.getTypes().get(key)