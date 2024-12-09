from app.models.expense import Expense

EMPTY_VALUE_ERROR_MESSAGE = "Value cannot be empty"
WRONG_TYPE_MESSAGE = "The value should be a number"
WRONG_EXPENSE_CATEGORY = f"Must be from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}"

def get_data():
    print(f"Expense app tracker.")
    user_input = get_user_input()


def get_user_input():
    expense_name = input("Enter expense name: ")
    if not isinstance(expense_name, str) or expense_name.strip() == '':
        raise ValueError(EMPTY_VALUE_ERROR_MESSAGE)
    expense_cost = input("Enter how much you've spent (£): ")
    try:
        expense_cost = int(expense_cost)
    except ValueError:
        raise ValueError(WRONG_TYPE_MESSAGE)

    expense_category = input(f"Enter expense category from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}: ")
    return expense_name, float(expense_cost), int(expense_category)