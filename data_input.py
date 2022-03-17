class DataInput:

    def select_years(self):
        '''
        Select the beginning and last years for search
        '''
        while True:
            select_by_own = input("Default selected time period 1900-2040. Do you want to enter your own? (Y/N) ")
            if select_by_own.upper() == "Y" or select_by_own.upper() == "N":
                break
            else:
                continue

        if select_by_own.upper() == "Y":
            startYear = self.input_year("start year from 1900 to 5000")
            endYear = self.input_year("last year not more than 5000", startYear)
        elif select_by_own.upper() == "N":
            startYear = 1900
            endYear = 2040

        return startYear,endYear

    def input_year(self, identify_year, startYear=0):
        '''
        Control user input of year value
        '''
        while True:
            try:
                year = int(input("Please enter " + identify_year + ": "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                if year < startYear:
                    print("Last year should be higher than start")
                    continue
                elif year < 1900 or year > 5000:
                    print("The value doesn`t match the sequence.")
                    continue
                break
        return year