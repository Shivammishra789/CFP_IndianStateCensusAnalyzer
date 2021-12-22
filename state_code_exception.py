'''
@author: Shivam Mishra
@date: 23-12-21 1:52 AM
@desc: StateCodeException class
'''


class StateCodeException(Exception):

    def __init__(self,message):
        self.message= message

    def __str__(self):
        return self.message