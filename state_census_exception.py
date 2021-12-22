'''
@author: Shivam Mishra
@date: 22-12-21 1:21 AM
@desc: StateCensusException class
'''


class StateCensusException(Exception):

    def __init__(self,message):
        self.message= message

    def __str__(self):
        return self.message