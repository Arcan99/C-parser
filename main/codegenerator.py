# Generate C-code from Easy C

from main.codeconverter import Converter
from main.filereader import File_reader

class Generator:
    
    def __init__(self, target_path: str, result_path: str) -> None:
        self.reader = File_reader(file_path=target_path)
        self.result_file = open(result_path, "w")
        self.converter = Converter()
        self.currentLine = self.reader.getNewTokens()
        
    def __del__(self):
        self.result_file.close()
        

    def convertFile(self):
        # wrapper text
        self.generateWrapperText()
        # includes
        # defines
        self.convertDefines()
        # structs
        self.convertUserStruct()
        # functions 
        self.convertFunction()
        # main
        self.convertMain()
        
    def saveResult(self, line: str, indent: int):
        print(indent*"\t" + line)                           # TODO: Remove print statment when no longer needed
        self.result_file.write(indent*"\t" + line + "\n")
        self.currentLine = self.reader.getNewTokens()
    
    ### Main Methods ###
    
    def generateWrapperText(self):
        # generate misc text at the top of the document
        pass
    
    def convertDefines(self):
        # User Definitions
        pass
    
    def convertUserStruct(self):
        # User Structure
        pass
    
    def convertFunction(self):
        # define name
        # body
        # end
        pass
    
    def convertMain(self):
        # start
        self.setConverterSentence()
        result = self.converter.start()
        if result is None:
            raise SyntaxError("Could not find start of main fumction\n")
        self.saveResult(result, 0)
        
        # body
        self.convertBody()
        
        # end
        self.setConverterSentence()
        result = self.converter.end()
        if result is None:
            raise SyntaxError("Could not find end of main fumction\n")
        self.saveResult(result, 0)
        pass

     ### Supporting Methods ###
     
    def convertBody(self):
        #differente types of body
        allowed_words = ["set"]
        while not self.currentLine == [] and self.currentLine[0] in allowed_words:
            self.setConverterSentence()
            result = self.converter.set()
            if result is None:
                raise SyntaxError("Keword in body is not valid\n")
            self.saveResult(result, 1)
    
    def setConverterSentence(self):
        self.converter.setCurrentSentence(self.currentLine)
    
    
    
            
            
        
        

if __name__ == "__main__":
    
    g = Generator("test_files/main1.txt", "test_results/main1.c")
    g.convertFile()