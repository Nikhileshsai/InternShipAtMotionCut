#Expense Tracker
import tkinter as tk
from tkinter import ttk, messagebox
import json
import pandas as pd
import matplotlib.pyplot as plt
#Functions
# Load JSON data
def load_data(file_name='expenses.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
# Save JSON data
def save_data(data, file_name='expenses.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
# Add expense
def add_expense():
    date = entry_date.get()
    amount = entry_amount.get()
    category = entry_category.get()   
    if not date or not amount or not category:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return
    expenses.append({'date': date, 'amount': amount, 'category': category})
    save_data(expenses)
    update_table()
    entry_date.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_category.delete(0, tk.END)
# Update table
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for expense in expenses:
        tree.insert('', tk.END, values=(expense['date'], expense['amount'], expense['category']))
# Plot total expenses over time
def plot_expenses_over_time():
    df = pd.DataFrame(expenses)
    if df.empty:
        messagebox.showwarning("No Data", "No expense data to plot!")
        return
    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['amount'], marker='o')
    plt.title('Total Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.show()
# Plot expenses by category
def plot_expenses_by_category():
    df = pd.DataFrame(expenses)
    if df.empty:
        messagebox.showwarning("No Data", "No expense data to plot!")
        return
    category_totals = df.groupby('category')['amount'].sum()
    plt.figure(figsize=(10, 6))
    category_totals.plot(kind='bar')
    plt.title('Total Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.show()
# Plot expenses distribution
def plot_expenses_distribution():
    df = pd.DataFrame(expenses)
    if df.empty:
        messagebox.showwarning("No Data", "No expense data to plot!")
        return
    category_totals = df.groupby('category')['amount'].sum()
    plt.figure(figsize=(8, 8))
    category_totals.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expenses Distribution by Category')
    plt.ylabel('')
    plt.show()
# Load expenses data
expenses = load_data()
#User Interface
# Main window
root = tk.Tk()
root.title("Expense Tracker")
# Input frame
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_date = ttk.Entry(input_frame, width=20)
entry_date.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(input_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
entry_amount = ttk.Entry(input_frame, width=20)
entry_amount.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
entry_category = ttk.Entry(input_frame, width=20)
entry_category.grid(row=2, column=1, padx=5, pady=5)
ttk.Button(input_frame, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2, pady=10)
# Create treeview for displaying expenses
columns = ('date', 'amount', 'category')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('date', text='Date')
tree.heading('amount', text='Amount')
tree.heading('category', text='Category')
tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
# Create buttons for plotting
plot_frame = ttk.Frame(root, padding="10")
plot_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
ttk.Button(plot_frame, text="Plot Expenses Over Time", command=plot_expenses_over_time).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(plot_frame, text="Plot Expenses by Category", command=plot_expenses_by_category).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(plot_frame, text="Plot Expenses Distribution", command=plot_expenses_distribution).grid(row=0, column=2, padx=5, pady=5)
# Update the table with current data
update_table()
# Start the Tkinter main loop
root.mainloop()