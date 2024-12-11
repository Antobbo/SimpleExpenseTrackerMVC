import sys
import unittest
from io import StringIO
from unittest.mock import patch

from app.models.expense import Expense
from app.views import expense_view
from app.views.expense_view import ExpenseView


class TestExpenseView(unittest.TestCase):

    def setUp(self):
        """Set up an instance of ExpenseView for testing."""
        self.expense_view = ExpenseView(view_name="Test View")

    #USER INPUT
    #given
    @patch('builtins.input', side_effect = ["coffee", 25, 1])
    def test_should_user_input_be_correct(self, mock_input):
        #when
        result = self.expense_view.get_user_input()
        #then
        self.assertEqual(result, ("coffee", 25, 1))

    #given
    @patch('builtins.input', side_effect = ["", 25, 1])
    def test_should_throw_error_if_expense_name_empty(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            self.expense_view.get_user_input()
        #then
        self.assertIn(self.expense_view.EMPTY_VALUE_ERROR_MESSAGE, str(context.exception))

    # given
    @patch('builtins.input', side_effect=["coffee", "dg", 1])
    def test_should_throw_error_if_expense_cost_not_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            self.expense_view.get_user_input()
        # then
        self.assertIn(self.expense_view.WRONG_TYPE_MESSAGE, str(context.exception))

        # given

    @patch('builtins.input', side_effect=["coffee", "", 1])
    def test_should_throw_error_if_expense_cost_empty_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            self.expense_view.get_user_input()
        # then
        self.assertIn(self.expense_view.WRONG_TYPE_MESSAGE, str(context.exception))

    #given
    @patch('builtins.input', side_effect=["coffee", 25, 6])
    def test_should_throw_error_if_expense_category_is_not_in_range(self, mock_input):
        with self.assertRaises(TypeError) as context:
            # when
            self.expense_view.get_user_input()
        # then
        self.assertIn(self.expense_view.WRONG_EXPENSE_CATEGORY, str(context.exception))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, 5])
    def test_should_input_all_be_correct(self, mock_input):
        # when
        result = self.expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 25, 5))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, "5"])
    def test_should_input_all_be_correct_with_expense_category_as_string(self, mock_input):
        # when
        result = self.expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 25, 5))

    # given
    @patch('builtins.input', side_effect=["coffee", "10", "4"])
    def test_should_input_all_be_correct_with_expense_cost_as_string(self, mock_input):
        # when
        result = self.expense_view.get_user_input()
        # then
        self.assertEqual(result, ("coffee", 10, 4))

    # given
    @patch('builtins.input', side_effect=["coffee", 25, "test"])
    def test_should_throw_error_when_expense_category_is_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            # when
            result = self.expense_view.get_user_input()
        # then
        self.assertIn(self.expense_view.WRONG_TYPE_MESSAGE, str(context.exception))

    def test_should_print_expected_expense_details(self):
        #given
        expense = Expense('burger', 10, 1)
        captured_output = StringIO()
        #redirect stdout
        sys.stdout = captured_output
        self.expense_view.display_expense(expense)
        self.assertEqual(captured_output.getvalue().strip(), "Test View - Added expense: burger, £10, category 1")

    def test_should_print_expense_breakdown_correctly(self):
        breakdown = {
            "Food": 50.0,
            "Transport": 30.5,
            "Entertainment": 20.0
        }
        expected_output = (
            "Test View - Breakdown of expenses:\n"
            "Category Food: £50.0\n"
            "Category Transport: £30.5\n"
            "Category Entertainment: £20.0"
        )

        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output
        self.expense_view.display_breakdown(breakdown)
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()