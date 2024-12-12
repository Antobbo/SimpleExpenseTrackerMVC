import csv


class Expense:
    MONTHLY_BUDGET = 2000
    PATH_TO_FILE = "expenses.csv"
    EXPENSE_CATEGORY = {
     1: "food",
     2: "home",
     3: "work",
     4: "fun",
     5: "misc"   
    }

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def add_expense_to_file(self, expense):
        expense_to_add = [
            [expense.name, expense.price, expense.category]
        ]
        with open(self.PATH_TO_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expense_to_add)