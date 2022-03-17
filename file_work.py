class WorkWithFile():
    def write_to_file(self,text):
        '''
        Method to open file and write to it
        '''
        with open('output.txt', 'w') as f:
            f.write(text)

