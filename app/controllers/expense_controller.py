from contextlib import nullcontext

from app.models.expense import Expense


class ExpenseController:
    def __init__(self, view):
        self.view = view

    def get_view(self):
        return self.view

    def add_expense(self):
      name, price, category = self.view.get_user_input()
      expense = Expense(name, float(price), int(category))
      #todo: call the model to save to file
      self.view.display_expense(expense)

    def show_total_expenditure(self):
        #todo: replace hardcoded value and call the model to get it
        total = 150.99
        self.view.display_total(total)

    def show_expenditure_breakdown(self):
        #todo: replace hardcoded value and call the model to get it
        breakdown = nullcontext
        self.view.display_breakdown(breakdown)
