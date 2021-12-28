'''
@author: Shivam Mishra
@date: 23-12-21 1:45 AM
'''

import csv
import pathlib

from state_code_exception import StateCodeException


class CSVStates:
    """"Contains varies method like check no of records in file, check file name, check file extension etc"""

    @staticmethod
    def check_state_code_no_of_record_from_file():
        """"Checks number of records in the file"""
        with open("E:\\pythonProject\\state_census\\indian_state_code.csv") as my_file:
            count = 0
            for i in my_file:
                count += 1
        return count

    @staticmethod
    def check_state_code_file_name(file_name):
        """"Checks for file name is invalid"""
        with open("E:\\pythonProject\\state_census\\indian_state_code.csv") as my_file:
            if my_file.name == file_name:
                print("Valid file name")
            else:
                raise StateCodeException("Invalid file name")

    @staticmethod
    def check_state_code_file_extension(file_name):
        """""Check for file extension is invalid"""
        if pathlib.Path(file_name).suffix == ".csv":
            print("Valid file extension")
        else:
            raise StateCodeException("Invalid file extension")

    @staticmethod
    def check_state_code_delimeter(file_name):
        '''

        :param file_name:
        :return:
        '''
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(file_name)
        if  dialect.delimiter == ',':
            print("Valid file delimeter")
        else:
            raise StateCodeException("Invalid file delimeter")

    @staticmethod
    def check_state_code_file_header(file_header):
        '''
        Check for file header is invalid
        :param file_header: indian_state_co.csv
        :return:
        '''
        with open("E:\\pythonProject\\state_census\\indian_state_code.csv") as my_file:
            for i in my_file:
                if i.__contains__(file_header):
                    return True
                else:
                    raise StateCodeException("Incorrect file header")
                break