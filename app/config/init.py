from app.controllers.expense_controller import ExpenseController
from app.models.expense import Expense
from app.views.expense_view import ExpenseView


def main():
    #create view
    view = ExpenseView("Expense Tracker")

    #create empty model
    model = Expense("", 0, 0)

    #create the controller
    controller = ExpenseController(view, model)

    #update the model and add expense
    controller.add_expense()

    controller.show_total_expenditure()
    controller.show_remaining_allowance()
    controller.show_expenditure_breakdown()

if __name__ == "__main__":
    main()
