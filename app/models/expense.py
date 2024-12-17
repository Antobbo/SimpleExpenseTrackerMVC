import csv

import pandas as pd

class Expense:
    FILE_NOT_FOUND_ERROR_MESSAGE = "The file wasn't found"
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

    def get_total_expenditure(self):
        try:
            df = pd.read_csv(self.PATH_TO_FILE, header=None)
        except FileNotFoundError:
            raise FileNotFoundError(self.FILE_NOT_FOUND_ERROR_MESSAGE)
        else:
            return df[1].sum()

    def get_remaining_allowance(self):
        return self.MONTHLY_BUDGET - self.get_total_expenditure()

    def get_expenditure_breakdown(self):
        df = pd.read_csv(self.PATH_TO_FILE, header=None, names=['Expense', 'Price', 'Category'])
        return df.groupby('Category')['Price'].sum()