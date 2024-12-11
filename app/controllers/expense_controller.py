
class ExpenseController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def get_model(self):
        return self.model

    def get_view(self):
        return self.view

    #def get_expense(self):
      #pass