import tkinter as tk
from datetime import date

def calculate_age():
    try:
        birth_year = int(entry_year.get())
        current_year = date.today().year
        age = current_year - birth_year
        label_result.config(text=f"Your age is {age} years", fg="green")
    except ValueError:
        label_result.config(text="Enter a valid year", fg="red")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")
root.config(bg="lightyellow")

tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="lightyellow").pack(pady=10)

tk.Label(root, text="Enter Birth Year:", bg="lightyellow").pack()
entry_year = tk.Entry(root)
entry_year.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue").pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), bg="lightyellow")
label_result.pack(pady=10)

root.mainloop()