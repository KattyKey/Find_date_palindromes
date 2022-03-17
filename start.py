from calculation import Calculate
from file_work import WorkWithFile
from data_input import DataInput

'''
Define year frame in which program will wirk
Find palindroms in chosen period
Write the result to file
'''
year_list = DataInput().select_years()
result = Calculate().find_palindroms(year_list[0],year_list[1])
WorkWithFile().write_to_file(result)


