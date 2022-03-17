import datetime

class Calculate:
    def find_palindroms(self, start_year,last_year):
        start_date = datetime.datetime.strptime("01.01."+ str(start_year), "%d.%m.%Y")
        last_date = datetime.datetime.strptime("31.12."+str(last_year), "%d.%m.%Y")
        palindrome_dates =""

        while start_date <= last_date:
            formatted_date = start_date.strftime("%d.%m.%y")
            if self.is_palindrome(formatted_date):
                palindrome_dates+=formatted_date+'\n'
            start_date+= datetime.timedelta(days=1)
        if palindrome_dates == "":
            palindrome_dates ="There is no palindroms in selected period"

        return palindrome_dates

    def is_palindrome(self,string):
        reversed_string = string[::-1]
        if string == reversed_string:
            return True
        else:
            return False
