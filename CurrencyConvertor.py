import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Variables for currency conversion
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Fetch available currencies
        self.currencies = self.fetch_currencies()

        # GUI components
        ttk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        ttk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        ttk.Combobox(root, values=self.currencies, textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        ttk.Combobox(root, values=self.currencies, textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(root, text="Convert", command=self.convert_currency).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        ttk.Label(root, textvariable=self.result_var).grid(row=4, column=1, padx=10, pady=10)

    def fetch_currencies(self):
        # Fetch available currencies using forex-python
        c = CurrencyRates()
        currencies = c.get_rates("").keys()
        return list(currencies)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Use forex-python to get the exchange rate
            c = CurrencyRates()
            exchange_rate = c.get_rate(from_currency, to_currency)

            # Perform the currency conversion
            result = amount * exchange_rate
            self.result_var.set(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            self.result_var.set("Error: Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
