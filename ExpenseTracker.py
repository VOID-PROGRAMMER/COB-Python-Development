import tkinter as tk
from tkinter import ttk
from datetime import datetime

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.label_1 = ttk.Label(root, text="Python Development Phase-1 Task 2")
        

        # Create a list to store expenses
        self.expenses = []

        # Create GUI components
        self.label_category = ttk.Label(root, text="Category:")
        self.entry_category = ttk.Entry(root)

        self.label_amount = ttk.Label(root, text="Amount:")
        self.entry_amount = ttk.Entry(root)

        self.label_description = ttk.Label(root, text="Description:")
        self.entry_description = ttk.Entry(root)

        self.button_add_expense = ttk.Button(root, text="Add Expense", command=self.add_expense)
        self.button_generate_report = ttk.Button(root, text="Generate Monthly Report", command=self.generate_monthly_report)

        # Layout the components
        self.label_1.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.label_category.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.entry_category.grid(row=1, column=1, padx=10, pady=10)

        self.label_amount.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.entry_amount.grid(row=2, column=1, padx=10, pady=10)

        self.label_description.grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.entry_description.grid(row=3, column=1, padx=10, pady=10)

        self.button_add_expense.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_generate_report.grid(row=5, column=0, columnspan=2, pady=10)

    def add_expense(self):
        category = self.entry_category.get()
        amount = float(self.entry_amount.get())
        description = self.entry_description.get()

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        expense = {'Date': date, 'Category': category, 'Amount': amount, 'Description': description}
        self.expenses.append(expense)

        # Clear the entry fields after adding an expense
        self.entry_category.delete(0, 'end')
        self.entry_amount.delete(0, 'end')
        self.entry_description.delete(0, 'end')

        print("Expense added successfully!")

    def generate_monthly_report(self):
        month = datetime.now().month
        year = datetime.now().year

        total_expenses = sum(expense['Amount'] for expense in self.expenses if datetime.strptime(expense['Date'], '%Y-%m-%d %H:%M:%S').month == month and datetime.strptime(expense['Date'], '%Y-%m-%d %H:%M:%S').year == year)

        report_text = f"\nMonthly Report for {datetime(year, month, 1).strftime('%B %Y')}:\n"
        report_text += f"Total Expenses: ${total_expenses:.2f}\n"

        # Display the report in a new window
        report_window = tk.Toplevel(self.root)
        report_window.title("Monthly Report")
        report_label = ttk.Label(report_window, text=report_text)
        report_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()









