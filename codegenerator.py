# Generate C-code from Easy C

from codeconverter import Converter
from filereader import File_reader

class Generator:
    
    def __init__(self, file_path: str) -> None:
        self.reader = File_reader(file_path=file_path)
        self.converter = Converter()

    def convertFile(self, file_path: str):
        # wrapper text
        self.generateWrapperText()
        # includes
        # defines
        self.convertDefines(self)
        # structs
        self.convertUserStruct(self)
        # functions 
        self.convertFunction(self)
        # main
        self.convertMain(self)
        
    
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
        # body
        # end
        pass

     ### Supporting Methods ###
     
    def convertBody(self):
        #differente types of body
        pass
    
    
    
            
            
        
        

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
