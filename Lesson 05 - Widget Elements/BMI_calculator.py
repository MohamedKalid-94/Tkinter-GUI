from tkinter import *
from tkinter import messagebox

def calculate_metrics():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to m
        age = int(age_entry.get())
        gender = gender_var.get()

        # BMI
        bmi = weight / (height ** 2)

        # BMR
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

        # Fat %
        fat = (1.20 * bmi) + (0.23 * age) - (10.8 if gender == "Male" else 0) - 5.4

        messagebox.showinfo("Results",
                            f"BMI: {bmi:.2f}\nBMR: {bmr:.2f} calories/day\nFat %: {fat:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please check your values.")

# Root window
root = Tk()
root.title("BMI, BMR, Fat% Calculator")
root.geometry("350x300")

# Frame using .pack()
frame1 = Frame(root, pady=10)
frame1.pack()
Label(frame1, text="Enter Your Details", font=('Arial', 14)).pack()

# Frame using .grid()
frame2 = Frame(root, padx=10, pady=10)
frame2.pack()

Label(frame2, text="Weight (kg):").grid(row=0, column=0, sticky=W, pady=2)
weight_entry = Entry(frame2)
weight_entry.grid(row=0, column=1, pady=2)

Label(frame2, text="Height (cm):").grid(row=1, column=0, sticky=W, pady=2)
height_entry = Entry(frame2)
height_entry.grid(row=1, column=1, pady=2)

Label(frame2, text="Age:").grid(row=2, column=0, sticky=W, pady=2)
age_entry = Entry(frame2)
age_entry.grid(row=2, column=1, pady=2)

Label(frame2, text="Gender:").grid(row=3, column=0, sticky=W, pady=2)
gender_var = StringVar(value="Male")
Radiobutton(frame2, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky=W)
Radiobutton(frame2, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, sticky=W)

# Button using .place()
submit_btn = Button(root, text="Calculate", command=calculate_metrics)
submit_btn.place(x=140, y=250)

root.mainloop()
