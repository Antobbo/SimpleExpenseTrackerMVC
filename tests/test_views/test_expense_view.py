import unittest
from unittest.mock import patch

from app.views import expense_view


class TestExpenseView(unittest.TestCase):

    #USER INPUT
    #given
    @patch('builtins.input', side_effect = ["coffee", 25, 1])
    def test_should_user_input_be_correct(self, mock_input):
        #when
        result = expense_view.get_user_input()
        #then
        self.assertEqual(result, ("coffee", 25, 1))

    #given
    @patch('builtins.input', side_effect = ["", 25, 1])
    def test_should_throw_error_if_expense_name_empty(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            expense_view.get_user_input()
        #then
        self.assertIn(expense_view.EMPTY_VALUE_ERROR_MESSAGE, str(context.exception))

    # given
    @patch('builtins.input', side_effect=["coffee", "dg", 1])
    def test_should_throw_error_if_expense_cost_not_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            expense_view.get_user_input()
        # then
        self.assertIn(expense_view.WRONG_TYPE_MESSAGE, str(context.exception))

        # given

    @patch('builtins.input', side_effect=["coffee", "", 1])
    def test_should_throw_error_if_expense_cost_empty_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            expense_view.get_user_input()
        # then
        self.assertIn(expense_view.WRONG_TYPE_MESSAGE, str(context.exception))


if __name__ == '__main__':
    unittest.main()