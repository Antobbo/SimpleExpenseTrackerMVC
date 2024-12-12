import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch, Mock

import pandas as pd

from app.controllers.expense_controller import ExpenseController
from app.models.expense import Expense
from app.views.expense_view import ExpenseView

class TestExpenseController(unittest.TestCase):

    def test_should_controller_have_valid_model_and_view(self):
        #given
        view = ExpenseView("DefaultV")
        model = Expense("coffee", 25, 1)
        self.controller = ExpenseController(view, model)

        #when
        view_from_controller = self.controller.get_view()
        model_from_controller = self.controller.get_model()

        #then
        self.assertEqual(view.get_view_name(), view_from_controller.get_view_name(), "The view name should match")
        self.assertEqual(model.get_name(), model_from_controller.get_name(), "Name of expense should match")
        self.assertEqual(model.get_category(), model_from_controller.get_category(), "Category should match")
        self.assertEqual(model.get_price(), model_from_controller.get_price(), "Price should match")

    @patch('builtins.input', side_effect=["coffee", 3.0, 1])
    def test_should_display_expense_correctly(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        model = Expense("coffee", 3.0, 1)
        self.controller = ExpenseController(view, model)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        #when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: coffee, £3.0, category 1"

        #then
        self.assertIn(expected_output, output)
        self.delete_file(Expense.PATH_TO_FILE)

    @patch('builtins.input', side_effect=["water", 250.99, 2])
    def test_should_display_expense_correctly_float_num(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        model = Expense("water", 250.99, 2)
        self.controller = ExpenseController(view, model)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        #when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: water, £250.99, category 2"

        #then
        self.assertIn(expected_output, output)
        self.delete_file(Expense.PATH_TO_FILE)

    @patch('builtins.input', side_effect=["water", "250.99", "2"])
    def test_should_display_expense_correctly_using_strings(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        model = Expense("water", "250.99", "2")
        self.controller = ExpenseController(view, model)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        # when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: water, £250.99, category 2"

        # then
        self.assertIn(expected_output, output)
        self.delete_file(Expense.PATH_TO_FILE)


    def test_should_controller_call_show_total_expenditure(self):
        # given
        mock_view = Mock(spec=ExpenseView)
        mock_model = Mock(spec=Expense)
        self.controller = ExpenseController(mock_view, mock_model)

        # when
        self.controller.show_total_expenditure()

        # then
        mock_view.display_total.assert_called_once()

    def test_should_controller_call_show_expenditure_breakdown(self):
        # given
        mock_view = Mock(spec=ExpenseView)
        mock_model = Mock(spec=Expense)
        self.controller = ExpenseController(mock_view, mock_model)

        # when
        self.controller.show_expenditure_breakdown()

        # then
        mock_view.display_breakdown.assert_called_once()

    #Testing the file addition
    @patch('builtins.input', side_effect=["water", "250.99", "2"])
    def test_should_create_file(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        model = Expense("water", "250.99", "2")
        self.controller = ExpenseController(view, model)

        # when
        self.controller.add_expense()

        # then
        self.assertTrue(os.path.isfile(Expense.PATH_TO_FILE))
        self.delete_file(Expense.PATH_TO_FILE)

    @patch('builtins.input', side_effect=["water", "250.99", "2"])
    def test_should_add_expense_to_file(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        model = Expense("water", "250.99", "2")
        self.controller = ExpenseController(view, model)

        # when
        self.controller.add_expense()

        # then
        df = pd.read_csv(Expense.PATH_TO_FILE, header=None)
        rows = len(df)
        self.assertEqual(rows, 1, "Row number should be 1")
        col_list = df[0].tolist()
        self.assertTrue('water' in col_list)
        self.delete_file(Expense.PATH_TO_FILE)

    @staticmethod
    def delete_file(file_name):
        # Clean up by removing the file after the test
        if os.path.isfile(file_name):
            os.remove(file_name)

if __name__ == '__main__':
    unittest.main()