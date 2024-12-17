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

      self.model.name = name
      self.model.price = price
      self.model.category = category
      self.view.display_expense(self.model)
      self.model.add_expense_to_file(self.model)

    def show_total_expenditure(self):
        total = self.model.get_total_expenditure()
        self.view.display_total(total)

    def show_remaining_allowance(self):
        remaining_allowance = self.model.get_remaining_allowance()
        self.view.display_remaining_allowance(remaining_allowance)

    def show_expenditure_breakdown(self):
        breakdown = self.model.get_expenditure_breakdown()
        self.view.display_breakdown(breakdown)
