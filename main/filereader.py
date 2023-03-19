# reads text from file and converts it to llists of tokens

class File_reader:
    
    def __init__(self, file_path) -> None:
        self.file = open(file_path, "r")
        
    def __del__(self):
        self.file.close()
        
    def readNextLine(self):
        sentence = self.file.readline()
        if len(sentence) == 0:
            return None
        return sentence
        
    def getNewTokens(self) -> bool:
        while True:
            input = self.readNextLine()
            if input is None:
                return None
            input = input.split()
            if not input == []:
                break
        return input
        
    

    
if __name__ == "__main__":
    reader = File_reader("test_files/main1.txt")
    tokens = reader.getNewTokens()
    while tokens is not None:
        print(tokens)
        tokens = reader.getNewTokens()
        