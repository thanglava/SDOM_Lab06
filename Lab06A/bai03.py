import tkinter as tk
from tkinter import ttk

class DataEntryForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Entry Form")
        self.geometry("500x400")

        # User Information Frame
        user_info_frame = tk.LabelFrame(self, text="User Information", padx=10, pady=10)
        user_info_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(user_info_frame, text="First Name").grid(row=0, column=0)
        self.first_name_input = tk.Entry(user_info_frame)
        self.first_name_input.grid(row=0, column=1)

        tk.Label(user_info_frame, text="Last Name").grid(row=0, column=2)
        self.last_name_input = tk.Entry(user_info_frame)
        self.last_name_input.grid(row=0, column=3)

        tk.Label(user_info_frame, text="Title").grid(row=0, column=4)
        self.title_input = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Mrs.", "Dr."])
        self.title_input.grid(row=0, column=5)

        tk.Label(user_info_frame, text="Age").grid(row=1, column=0)
        self.age_input = tk.Spinbox(user_info_frame, from_=0, to=100)
        self.age_input.grid(row=1, column=1)

        tk.Label(user_info_frame, text="Nationality").grid(row=1, column=2)
        self.nationality_input = tk.Entry(user_info_frame)
        self.nationality_input.grid(row=1, column=3)

        # Registration Status Frame
        registration_frame = tk.LabelFrame(self, text="Registration Status", padx=10, pady=10)
        registration_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.currently_registered = tk.Checkbutton(registration_frame, text="Currently Registered")
        self.currently_registered.grid(row=0, column=0)

        tk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1)
        self.completed_courses_input = tk.Spinbox(registration_frame, from_=0, to=50)
        self.completed_courses_input.grid(row=0, column=2)

        tk.Label(registration_frame, text="# Semesters").grid(row=0, column=3)
        self.semesters_input = tk.Spinbox(registration_frame, from_=0, to=10)
        self.semesters_input.grid(row=0, column=4)

        # Terms and Conditions Frame
        terms_frame = tk.LabelFrame(self, text="Terms & Conditions", padx=10, pady=10)
        terms_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.terms_checkbox = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.")
        self.terms_checkbox.pack()

        # Submit Button
        self.submit_button = tk.Button(self, text="Enter data", command=self.submit_data)
        self.submit_button.pack(pady=10)

    def submit_data(self):
        print("First Name:", self.first_name_input.get())
        print("Last Name:", self.last_name_input.get())
        print("Title:", self.title_input.get())
        print("Age:", self.age_input.get())
        print("Nationality:", self.nationality_input.get())
        print("Currently Registered:", self.currently_registered.var.get() if hasattr(self.currently_registered, 'var') else False)
        print("Completed Courses:", self.completed_courses_input.get())
        print("Semesters:", self.semesters_input.get())
        print("Accepted Terms:", self.terms_checkbox.var.get() if hasattr(self.terms_checkbox, 'var') else False)

if __name__ == "__main__":
    app = DataEntryForm()
    app.mainloop()