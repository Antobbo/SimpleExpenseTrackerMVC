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

    #given
    @patch('builtins.input', side_effect=["coffee", 25, 6])
    def test_should_throw_error_if_expense_category_is_not_in_range(self, mock_input):
        with self.assertRaises(TypeError) as context:
            # when
            expense_view.get_user_input()
        # then
        self.assertIn(expense_view.WRONG_EXPENSE_CATEGORY, str(context.exception))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, 5])
    def test_should_input_all_be_correct(self, mock_input):
        # when
        result = expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 25, 5))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, "5"])
    def test_should_input_all_be_correct_with_expense_category_as_string(self, mock_input):
        # when
        result = expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 25, 5))

    # given
    @patch('builtins.input', side_effect=["coffee", "10", "4"])
    def test_should_input_all_be_correct_with_expense_cost_as_string(self, mock_input):
        # when
        result = expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 10, 4))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, "test"])
    def test_should_throw_error_when_expense_category_is_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            result = expense_view.get_user_input()
        # then
        self.assertIn(expense_view.WRONG_TYPE_MESSAGE, str(context.exception))

if __name__ == '__main__':
    unittest.main()