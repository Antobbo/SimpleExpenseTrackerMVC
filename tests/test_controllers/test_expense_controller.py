import unittest

from app.controllers.expense_controller import ExpenseController
from app.models.expense import Expense
from app.views.expense_view import ExpenseView

class TestExpenseController(unittest.TestCase):

    def test_should_controller_have_valid_model_and_view(self):
        #given
        view = ExpenseView("DefaultV")
        model = Expense('burger', 10, 1)
        self.controller = ExpenseController(view, model)

        #when
        model_from_controller = self.controller.get_model()
        view_from_controller = self.controller.get_view()

        #then
        self.assertEqual(model.get_name(), model_from_controller.get_name(), "The names should be the same")
        self.assertEqual(model.get_price(), model_from_controller.get_price(), "The prices should be the same")
        self.assertEqual(model.get_category(), model_from_controller.get_category(), "The categories should be the same")
        self.assertEqual(view.get_view_name(), view_from_controller.get_view_name(), "The view name should match")


if __name__ == '__main__':
    unittest.main()