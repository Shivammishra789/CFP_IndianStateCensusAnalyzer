'''
@author: Shivam Mishra
@date: 23-12-21 2:02 AM
'''
import pytest

from state_code import CSVStates
from state_code_exception import StateCodeException


class TestIndianStateCode:

    @pytest.fixture
    def state(self):
        state = CSVStates()
        return state

    def test_check_number_of_records_matches(self, state):
        assert state.check_state_code_no_of_record_from_file() == 38

    def test_check_file_name_is_invalid(self, state):
        with pytest.raises(StateCodeException) as exception:
            state.check_state_code_file_name("indian_state_co.csv")
            assert exception.value.message == "Invalid file name"

    def test_check_file_extension_is_invalid(self, state):
        with pytest.raises(StateCodeException) as exception:
            state.check_state_code_file_extension("indian_state_code_data.txt")
            assert exception.value.message == "Invalid file extension"

    def test_check_delimeter_is_invalid(self, state):
        with pytest.raises(StateCodeException) as exception:
            state.check_state_code_delimeter(".")
            assert exception.value.message == "Invalid file delimeter"

    def test_check_file_header_is_invalid(self,state):
        with pytest.raises(StateCodeException) as exception:
            state.check_state_code_file_header("Andaman and Niobar Islands,35,AN")
        assert "Incorrect file header" == exception.value.message
