from contextlib import nullcontext

from app.models.expense import Expense


class ExpenseController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def get_view(self):
        return self.view

    def get_model(self):
        return self.model

    def add_expense(self):
      name, price, category = self.view.get_user_input()

      #self.model.name = name
      #self.model.price = price
     # self.model.category = category

      self.view.display_expense(self.model)
      self.model.add_expense_to_file(self.model)


    def show_total_expenditure(self):
        #todo: replace hardcoded value and call the model to get it
        total = 150.99
        self.view.display_total(total)

    def show_expenditure_breakdown(self):
        #todo: replace hardcoded value and call the model to get it
        breakdown = nullcontext
        self.view.display_breakdown(breakdown)
