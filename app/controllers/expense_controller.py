from app.models.expense import Expense


class ExpenseController:
    def __init__(self, view):
        self.view = view

    def get_view(self):
        return self.view

    def add_expense(self):
      name, price, category = self.view.get_user_input()
      expense = Expense(name, float(price), int(category))
      self.view.display_expense(expense)