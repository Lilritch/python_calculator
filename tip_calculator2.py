#tip calculator
import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        food_amount = float(food_entry.get())
        tip_percentage = float(tip_entry.get()) / 100
        num_people = int(people_entry.get())

        if num_people <= 0:
            raise ValueError("Number of people must be greater than 0.")
        
        tip_amount = food_amount * tip_percentage 
        total = food_amount + tip_percentage
        per_person = total / num_people

        result_label.config(text=f'Total: ${total:.2f}\nPer Person: ${per_person:.2f}')
    except ValueError as e:
        messagebox.showerror("Input Error", f"Please enter a valid numbers.\n{e}")   

#create the main window
root =tk.Tk()
root.title("Tip Calculator")

#create and place the widgets
tk.Label(root, text= "Food Amount $:").grid(row=0 , column=0, padx=10, pady=5, sticky='e')
food_entry = tk.Entry(root)
food_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tip Percentage %:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
tip_entry = tk.Entry(root)
tip_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Number of people.").grid(row=2, column=0, padx=10, pady=5, sticky='e')
people_entry = tk.Entry(root)
people_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate_total).grid(row=2, column=0, padx=10, pady=5, sticky='e')
result_label =tk.Label(root, text="", font=('Helvetica',12, 'bold'))
result_label.grid(row=4, column=0, columnspan=2, padx=1, pady=10)

#set focus on the first entry field
food_entry.focus_set()

#startbthe Tkinter main loop
root.mainloop()

# # Run the application
# root.mainloop()




        