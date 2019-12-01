class ICPMSReader:

    def __init__(self, file_path):
        self.buffer = open(file_path, 'r').read()
        self.lines  = self.buffer.split("\n")
        self.header = self.readheader()

    def readheader(self):
        header = self.lines[0]
        return header.split(';')

    def readline(self, line):
        current_line = self.lines[line].split(';')

        line_content = {}

        for i in range(0, len(self.header)):
            line_content[self.header[i]] = current_line[i]
            
        return line_content

    def searchIDOffset(self, identificator):
        identificator = identificator.lower()
        end_pos = start_pos = 0

        for i in range(0, len(self.lines)):
            if identificator in self.lines[i].lower():
                start_pos = i
                break
        
        for i in range(start_pos + 1, len(self.lines)):
            if ";;;;;;;;;;;;;;;" in self.lines[i]:
                end_pos = i
                break

        return [start_pos, end_pos]

    def searchByID(self, identificator):
        start_pos, end_pos = self.searchIDOffset(identificator)

        result = {}

        for i in range(start_pos + 1, end_pos):
            line = self.readline(i)
            result[line['Run']] = line

        return result
        

    def listIdentificator(self):
        identificators = []

        for line in self.lines:
            if " " in line and ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;" in line:
                identificators.append(line[2:].split(';')[0])

        return identificators