class WorkWithFile():
    def write_to_file(self,text):
        with open('output.txt', 'w') as f:
            f.write(text)

