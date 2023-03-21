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
        result = []
        while True:
            input = self.readNextLine()
            if input is None:
                return None
            
            input = input.split('"')
            for i in range(len(input)):
                if i % 2:
                    result.append('"' + input[i] + '"')
                else:
                    for item in input[i].split():
                        result.append(item)  
            if not result == []:
                break
        return result
        
    

    
if __name__ == "__main__":
