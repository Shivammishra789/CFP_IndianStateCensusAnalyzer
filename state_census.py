'''
@author: Shivam Mishra
@date: 21-12-21 9:49 PM
'''
import csv
import pathlib

from state_census_exception import StateCensusException


class StateCensusAnalyser:
    """"Contains varies method like check no of records in file, check file name, check file extension etc"""

    @staticmethod
    def check_no_of_record_from_file():
        """"Checks number of records in the file"""
        with open("indian_census_data.csv") as my_file:
            count = 0
            for i in my_file:
                count += 1
        return count

    @staticmethod
    def check_file_name(file_name):
        """"Checks for file name is invalid"""
        with open("indian_census_data.csv") as my_file:
            if my_file.name == file_name:
                print("Valid file name")
            else:
                raise StateCensusException("Invalid file name")

    @staticmethod
    def check_file_extension(file_name):
        """""Check for file extension is invalid"""
        if pathlib.Path(file_name).suffix == ".csv":
            print("Valid file extension")
        else:
            raise StateCensusException("Invalid file extension")

    @staticmethod
    def check_delimeter(file_name):
        """"Check for file delimeter is invalid"""
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(file_name)
        if  dialect.delimiter == ',':
            print("Valid file delimeter")
        else:
            raise StateCensusException("Invalid file delimeter")

    @staticmethod
    def check_file_header(file_header):
        """"Check for file header is invalid"""
        with open("indian_census_data.csv") as my_file:
            for i in my_file:
                if i.__contains__(file_header):
                    return True
                else:
                    raise StateCensusException("Incorrect file header")
                break
