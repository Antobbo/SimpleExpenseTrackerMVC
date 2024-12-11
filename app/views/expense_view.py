from app.models.expense import Expense

class ExpenseView:

    def __init__(self, view_name="DefaultView"):
        self.view_name = view_name  # Adding an instance attribute

    EMPTY_VALUE_ERROR_MESSAGE = "Value cannot be empty"
    WRONG_TYPE_MESSAGE = "The value should be a number"
    WRONG_EXPENSE_CATEGORY = f"Must be from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}"

    def get_view_name(self):
        return self.view_name

    def get_data(self):
        print(f"Expense app tracker.")
        return self.get_user_input()

    def get_user_input(self):
        expense_name = input("Enter expense name: ")
        if not isinstance(expense_name, str) or expense_name.strip() == '':
            raise ValueError(self.EMPTY_VALUE_ERROR_MESSAGE)
        expense_cost = input("Enter how much you've spent (£): ")
        try:
            expense_cost = int(expense_cost)
        except ValueError:
            raise ValueError(self.WRONG_TYPE_MESSAGE)

        expense_category = input(f"Enter expense category from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}: ")
        try:
            expense_category = int(expense_category)
            if expense_category < next(iter(Expense.EXPENSE_CATEGORY)) or expense_category > len(Expense.EXPENSE_CATEGORY):
                raise TypeError(self.WRONG_EXPENSE_CATEGORY)
        except ValueError:
            raise ValueError(self.WRONG_TYPE_MESSAGE)

        return expense_name, float(expense_cost), int(expense_category)

    def display_total(self, total):
        print(f"{self.view_name} - You've spent a total of £{total}")

    def display_expense(self, expense):
        print(f"{self.view_name} - Added expense: {expense.name}, £{expense.price}, category {expense.category}")

    def display_remaining_allowance(self, remaining_allowance):
        print(f"{self.view_name} - You have left £{remaining_allowance}")

    def display_breakdown(self, breakdown):
        print(f"{self.view_name} - Breakdown of expenses:")
        for category, total in breakdown.items():
            print(f"Category {category}: £{total}")