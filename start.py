from calculation import Calculate
from file_work import WorkWithFile
from data_input import DataInput


year_list = DataInput().select_years()
result = Calculate().find_palindroms(year_list[0],year_list[1])
WorkWithFile().write_to_file(result)


