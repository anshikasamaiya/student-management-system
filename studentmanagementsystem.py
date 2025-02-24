import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to MySQL database
def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host (usually localhost)
        user="root",  # Replace with your MySQL username
        password="24Anshik@",  # Replace with your MySQL password
        database="student_management"  # Ensure the database name matches your MySQL database
    )
    return conn


# Function to add a student to the database
def add_student():
    conn = connect_to_db()
    cursor = conn.cursor()

    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if name and age and grade:
        sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        values = (name, age, grade)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields")

    cursor.close()
    conn.close()


# Function to view all students
def view_students():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    student_list.delete(0, tk.END)  # Clear previous list

    if rows:
        for row in rows:
            student_list.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    else:
        student_list.insert(tk.END, "No students found.")

    cursor.close()
    conn.close()


# Function to delete a student
def delete_student():
    conn = connect_to_db()
    cursor = conn.cursor()

    selected_student = student_list.get(tk.ACTIVE)
    if not selected_student:
        messagebox.showerror("Error", "No student selected")
        return

    student_id = selected_student.split(",")[0].split(":")[1].strip()

    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete student ID {student_id}?")
    if confirm:
        sql = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully!")
        view_students()  # Refresh student list

    cursor.close()
    conn.close()


# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("Student Management System")

# Labels and Entry Widgets for Student Information
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Grade").grid(row=2, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1)

# Buttons for operations
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=3, column=0, columnspan=2)

view_button = tk.Button(root, text="View Students", command=view_students)
view_button.grid(row=4, column=0, columnspan=2)

delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.grid(row=5, column=0, columnspan=2)

# Listbox to display students
student_list = tk.Listbox(root, width=50, height=10)
student_list.grid(row=6, column=0, columnspan=2)

# Run the application
root.mainloop()

