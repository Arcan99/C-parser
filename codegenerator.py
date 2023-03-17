# Generate C-code from Easy C

from codeconverter import Converter

class Generator:

    def temp(self):
        print("TODO")
        
        

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
