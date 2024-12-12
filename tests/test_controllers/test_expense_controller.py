import sys
import unittest
from io import StringIO
from unittest.mock import patch, Mock

from app.controllers.expense_controller import ExpenseController
from app.views.expense_view import ExpenseView

class TestExpenseController(unittest.TestCase):

    def test_should_controller_have_valid_model_and_view(self):
        #given
        view = ExpenseView("DefaultV")
        self.controller = ExpenseController(view)

        #when
        view_from_controller = self.controller.get_view()

        #then
        self.assertEqual(view.get_view_name(), view_from_controller.get_view_name(), "The view name should match")

    @patch('builtins.input', side_effect=["coffee", 3.0, 1])
    def test_should_display_expense_correctly(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        self.controller = ExpenseController(view)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        #when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: coffee, £3.0, category 1"

        #then
        self.assertIn(expected_output, output)

    @patch('builtins.input', side_effect=["water", 250.99, 2])
    def test_should_display_expense_correctly_float_num(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        self.controller = ExpenseController(view)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        #when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: water, £250.99, category 2"

        #then
        self.assertIn(expected_output, output)

    @patch('builtins.input', side_effect=["water", "250.99", "2"])
    def test_should_display_expense_correctly_using_strings(self, mock_input):
        # given
        view = ExpenseView("DefaultV")
        self.controller = ExpenseController(view)
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output

        # when
        self.controller.add_expense()
        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: water, £250.99, category 2"

        # then
        self.assertIn(expected_output, output)


    def test_should_controller_call_show_total_expenditure(self):
        # given
        mock_view = Mock(spec=ExpenseView)
        self.controller = ExpenseController(mock_view)

        # when
        self.controller.show_total_expenditure()

        # then
        mock_view.display_total.assert_called_once()

    def test_should_controller_call_show_expenditure_breakdown(self):
        # given
        mock_view = Mock(spec=ExpenseView)
        self.controller = ExpenseController(mock_view)

        # when
        self.controller.show_expenditure_breakdown()

        # then
        mock_view.display_breakdown.assert_called_once()



if __name__ == '__main__':
    unittest.main()