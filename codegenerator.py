# Generate C-code from Easy C


# Main key words
# start
# end
# Set
# print


class Generator:

    def temp(self):
        print("TODO")
    
     
    
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
    
    
class Converter:
    
    def __init__(self) -> None:
        self.tokens = []
    
    def setCurrentSentence(self, new_tokens: list):
        if type(new_tokens) == list:
            self.tokens = new_tokens
        else:
            raise TypeError("new_token is not of type list")
    
    def getSentenceLenght(self):
        return len(self.tokens)
    
    def getFirstToken(self):
        if self.getSentenceLenght() > 0:
            return self.tokens[0]
        else:
            return None
        
    def match(self, target: str):
        if self.getFirstToken() == target:
            self.tokens.pop(0)
            return True
        else: 
            return False
    
    def start(self) -> str:
        if self.match("start"):
            return "int main(int argc, char* argv) {"
        else:
            return None
    
    def end(self, result=0):
        if self.match("end"):
            return f"return {result};\n" + "}"
        else:
            return None
    
    def set(self):
        result = ""
        if not self.match("set"):
            return None
        variable_tpye = self.getFirstToken()
        for t in Token_index.getTypes():
            if self.match(t):
                result = f"{result}{Token_index.getType(variable_tpye)}"
                break
        else:
            return None
        result = f"{result} {self.getFirstToken()}"
        if not  self.match(self.getFirstToken()): # TODO: Check if variable exists
            return None
        if not  self.match("to"):
            return None
        result = f"{result} = {self.getFirstToken()};"   #TODO: Check is value is of corect type
        if not self.match(self.getFirstToken()):
            return None
        return result
    
if __name__ == "__main__":
    
    converter = Converter()
    converter.setCurrentSentence(["start"])
    temp = converter.start()
    if temp is not None:
        print(temp)
    
    converter.setCurrentSentence(["set", "integer", "x", "to", "10"])
    temp = converter.set()
    if temp is not None:
        print("\t" + temp)
    
    converter.setCurrentSentence(["end"])
    temp = converter.end()
    if temp is not None:
        print("\t" + temp)
