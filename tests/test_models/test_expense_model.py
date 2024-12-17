import unittest
from app.models.expense import Expense

class TestExpense(unittest.TestCase):
   
    def test_should_categories_have_expected_elements(self):
        self.assertIn("food", Expense.EXPENSE_CATEGORY[1])
        self.assertIn("home", Expense.EXPENSE_CATEGORY[2])
        self.assertIn("work", Expense.EXPENSE_CATEGORY[3])
        self.assertIn("fun", Expense.EXPENSE_CATEGORY[4])
        self.assertIn("misc", Expense.EXPENSE_CATEGORY[5])
        self.assertNotIn("Random", Expense.EXPENSE_CATEGORY[1])

    def test_should_length_expenses_category_be_as_expected(self):
        self.assertEqual(len(Expense.EXPENSE_CATEGORY), 5)

    def test_should_variable_have_right_values(self):
        #given
        name = "Coffee"
        category = "Food"
        price = 3.50

        #when
        current_expense = Expense(name, price, category)

        #then
        self.assertEqual(current_expense.category, category)
        self.assertEqual(current_expense.name, name)
        self.assertEqual(current_expense.price, price)

    def test_should_sum_generate_error_for_non_existent_file(self):
        # given
        name = "Coffee"
        category = "Food"
        price = 3.50

        # when
        current_expense = Expense(name, price, category)
        with self.assertRaises(FileNotFoundError) as context:
            # when
            current_expense.get_total_expenditure()
        # then
        self.assertIn(current_expense.FILE_NOT_FOUND_ERROR_MESSAGE, str(context.exception))

    def test_should_sum_generate_error_for_non_existent_file_when_calling_get_remaining_allowance(self):
        # given
        name = "Coffee"
        category = "Food"
        price = 3.50

        # when
        current_expense = Expense(name, price, category)
        with self.assertRaises(FileNotFoundError) as context:
            # when
            current_expense.get_remaining_allowance()
        # then
        self.assertIn(current_expense.FILE_NOT_FOUND_ERROR_MESSAGE, str(context.exception))

if __name__ == '__main__':
    unittest.main()