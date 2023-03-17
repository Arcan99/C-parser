# reads text from file and converts it to llists of tokens


class File_reader:
    
    def __init__(self, file_path) -> None:
        self.file = open(file_path, "r")
        self.text = []
        
    def __del__(self):
        self.file.close()
        
    def readNextLine(self):
        sentence = self.file.readline()
        if len(sentence) == 0:
            return None
        self.text.append(sentence)
        
    
      
if __name__ == "__main__":
    reader = File_reader("test_files/main1.txt")
    for i in range(6):
        reader.readNextLine()
    print(reader.text)