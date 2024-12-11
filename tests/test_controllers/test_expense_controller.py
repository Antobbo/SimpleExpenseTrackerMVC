import sys
import unittest
from io import StringIO
from unittest.mock import patch

from app.controllers.expense_controller import ExpenseController
from app.models.expense import Expense
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

        self.controller.add_expense()

        output = captured_output.getvalue().strip()
        expected_output = "DefaultV - Added expense: coffee, £3.0, category 1"
        self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main()