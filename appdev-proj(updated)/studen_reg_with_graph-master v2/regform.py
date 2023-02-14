from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from regformdb import Database
import matplotlib.pyplot as plt

db = Database("student.db")
root = Tk()
root.title("Junior High School Olympics Registration")
root.geometry('1150x800')
root.config(bg="#f0c59f")

student_number = StringVar()
first_name = StringVar()
last_name = StringVar()
middle_name = StringVar()
gender = StringVar()
yearlevel = StringVar(value="0")
sport = StringVar(value="0")


# Entries Frame
entries_frame = Frame(root, bg="#f0c59f")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Junior High School Olympics Registration", font=(
    "Calibri", 18, "bold"), bg="#EDCDBB", fg="black")
title.grid(row=0, columnspan=3, padx=10, pady=20, sticky="w")

lblNumber = Label(entries_frame, text="Student Number:",
                  font=("Calibri", 16), bg="#EDCDBB", fg="black")
lblNumber.grid(row=1, column=0, padx=10, pady=10, sticky="w")

txtNumber = Entry(entries_frame, textvariable=student_number,
                  font=("Calibri", 16), width=20)
txtNumber.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Student Name:",
                font=("Calibri", 16), bg="#EDCDBB", fg="black")
lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")

txt_last_name = Entry(entries_frame, textvariable=last_name,
                      font=("Calibri", 16), width=15)
# inserts string value, pseudo-placeholder
txt_last_name.insert(0, 'Enter Last Name')
txt_last_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")


txt_first_name = Entry(
    entries_frame, textvariable=first_name, font=("Calibri", 16), width=15)
# inserts string value, pseudo-placeholder
txt_first_name.insert(0, 'Enter First Name')
txt_first_name.grid(row=2, column=2, padx=10, pady=10, sticky="w")


txt_middle_name = Entry(
    entries_frame, textvariable=middle_name, font=("Calibri", 16), width=15)
# inserts string value, pseudo-placeholder
txt_middle_name.insert(0, 'Enter Middle Name')
txt_middle_name.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender:", font=(
    "Calibri", 16), bg="#EDCDBB", fg="black")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=(
    "Calibri", 16), width=13, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblRecord = Label(entries_frame, text="Student Record", font=(
    "Calibri", 17, "bold"), bg="#EDCDBB", fg="black")
lblRecord.grid(row=15, column=1, padx=10, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    student_number.set(row[0])
    last_name.set(row[1])
    first_name.set(row[2])
    middle_name.set(row[3])
    gender.set(row[4])
    yearlevel.set(row[5])
    sport.set(row[6])


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def dispalyAllButton():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)
    messagebox.showinfo("Success", "Table Refreshed")


def add_stud():
    if txtNumber.get() == "" or txt_last_name.get() == "" or txt_first_name.get() == "" or txt_middle_name.get() == "" or comboGender.get() == "" or yearlevel.get() == False or sport.get() == False:
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    db.insert(txtNumber.get(), txt_last_name.get(), txt_first_name.get(),
              txt_middle_name.get(), comboGender.get(), yearlevel.get(), sport.get())
    messagebox.showinfo("Success", "Record Successfully Saved")
    clearAll()
    dispalyAll()


def update_stud():
    if txtNumber.get() == "" or txt_last_name.get() == "" or txt_first_name.get() == "" or txt_middle_name.get() == "" or comboGender.get() == "" or yearlevel.get() == False or sport.get() == False:
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    db.update(txtNumber.get(), txt_last_name.get(), txt_first_name.get(),
              txt_middle_name.get(), comboGender.get(), yearlevel.get(), sport.get())
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    dispalyAll()


def delete_stud():
    if txtNumber.get() == "" or txt_last_name.get() == "" or txt_first_name.get() == "" or txt_middle_name.get() == "" or comboGender.get() == "" or yearlevel.get() == False or sport.get() == False:
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    delete_stud = messagebox.askyesno(
        "Junior High School Olympics Registration", "Are you sure you want to delete this entry?")
    if delete_stud > 0:
        db.remove(student_number.get())
        clearAll()
        dispalyAll()
    else:
        return


def clearAll():
    first_name.set("Enter First Name")
    last_name.set("Enter Last Name")
    middle_name.set("Enter Middle Name")
    student_number.set("")
    gender.set("")
    yearlevel.set(False)
    sport.set(False)


def clearAllButton():
    first_name.set("Enter First Name")
    last_name.set("Enter Last Name")
    middle_name.set("Enter Middle Name")
    student_number.set("")
    gender.set("")
    yearlevel.set(False)
    sport.set(False)
    messagebox.showinfo("Success", "All fields cleared")


def iExit():
    iExit = messagebox.askyesno(
        "Junior High School Olympics Registration", "Do you want to exit?")
    if iExit > 0:
        root.destroy()
        return


btn_frame = Frame(entries_frame, bg="#FFEDDB")
btn_frame.grid(row=5, column=0, columnspan=20, padx=10, sticky="w", rowspan=10)

# save
Button(entries_frame, command=add_stud, text="Submit Entry", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#e9aa73", bd=0).grid(row=4, column=2, padx=10, pady=10, sticky='w')
# update
Button(entries_frame, command=update_stud, text="Update Entry", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#f3d2b5",
       bd=0).grid(row=4, column=3, padx=10, pady=10, sticky='w')
# delete
Button(entries_frame, command=delete_stud, text="Delete Entry", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#c2c2c2",
       bd=0).grid(row=4, column=4, padx=10, pady=10, sticky='w')

# clear
Button(entries_frame, command=clearAllButton, text="Clear Fields", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#c2c2c2",
       bd=0).grid(row=3, column=4, padx=10, pady=10, sticky='w')

# radiobutton
Label(btn_frame, text="Year Level:", font=("Calibri", 16), bg="#EDCDBB",
      fg="black").grid(row=0, column=0, pady=10, padx=10, sticky='w')

Radiobutton(btn_frame, text="Grade 7", value="Grade 7", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0).grid(row=1, column=0, padx=10, pady=10, sticky='w')

Radiobutton(btn_frame, text="Grade 8", value="Grade 8", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0).grid(row=1, column=1, padx=10, pady=10, sticky='w')

Radiobutton(btn_frame, text="Grade 9", value="Grade 9", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0).grid(row=1, column=2, padx=10, pady=10, sticky='w')

Radiobutton(btn_frame, text="Grade 10", value="Grade 10", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0).grid(row=1, column=3, padx=10, pady=10, sticky='w')

# checkbutton
Label(btn_frame, text="Sports:", font=("Calibri", 16), bg="#EDCDBB",
      fg="black").grid(row=2, column=0, pady=10, padx=10, sticky='w')

Radiobutton(btn_frame, text="Badminton", value="Badminton", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, ).grid(row=3, column=0, sticky='w')
Radiobutton(btn_frame, text="Volleyball", value="Volleyball", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0,).grid(row=3, column=1, sticky='w')
Radiobutton(btn_frame, text="Basketball", value="Basketball", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, ).grid(row=3, column=2, sticky='w')
Radiobutton(btn_frame, text="Gymnastics", value="Gymnastics", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, ).grid(row=4, column=0, sticky='w')
Radiobutton(btn_frame, text="Swimming", value="Swimming", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, ).grid(row=4, column=1, sticky='w')
Radiobutton(btn_frame, text="Soccer", value="Soccer", width=15, variable=sport,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, ).grid(row=4, column=2, sticky='w')

# View
Button(entries_frame, command=dispalyAllButton, text="Refresh Table", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#B85C38", bd=0).grid(row=15, column=4, padx=10, pady=10, sticky="w")

# Close
Button(entries_frame, command=iExit, text="Close", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#B85C38",
       bd=0).grid(row=1, column=4, padx=10, pady=10, sticky='w')

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=10, y=600, width=1076, height=200)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))

scrolly = Scrollbar(tree_frame, orient="vertical")
scrolly.pack(side="right", fill="y")
scrollx = Scrollbar(tree_frame, orient="horizontal")
scrollx.pack(side="bottom", fill="x")
tv = ttk.Treeview(tree_frame, columns=(
    1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

tv.heading("1", text="Student Number")
tv.heading("2", text="Last Name")
tv.column("2", width=120)
tv.heading("3", text="First Name")
tv.column("3", width=120)
tv.heading("4", text="Middle Name")
tv.column("4", width=140)
tv.heading("5", text="Gender")
tv.column("5", width=100)
tv.heading("6", text="Year Level")
tv.column("6", width=120)
tv.heading("7", text="Sports")
# tv.column("7", width=100)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
scrolly.config(command=tv.yview)
scrollx.config(command=tv.xview)


# graphs


def filterYearLevel():
    keys = []
    values = []
    datas = db.filterYearLevel()

    for x in datas:
        keys.append(x[0])
        values.append(x[1])

    fig, ax = plt.subplots()

    year_level_label = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Year Level')
    ax.set_title('Number of students per Year Level')
    ax.bar_label(year_level_label)
    plt.show()


def filterSports():
    keys = []
    values = []
    datas = db.filterSports()

    for x in datas:
        keys.append(x[0])
        values.append(x[1])

    fig, ax = plt.subplots()

    sports = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Sports')
    ax.set_title('Number of students per Sports')
    ax.bar_label(sports)
    plt.show()


def filterSex():
    keys = []
    values = []
    datas = db.filterSex()

    for x in datas:
        keys.append(x[0])
        values.append(x[1])

    fig, ax = plt.subplots()

    gender = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Gender')
    ax.set_title('Number of students per Gender')
    ax.bar_label(gender)
    plt.show()


Label(entries_frame, text="Show Graph:", font=("Calibri", 16), bg="#EDCDBB",
      fg="black").grid(row=15, column=0, pady=10, padx=10, sticky='w')

Button(entries_frame, command=filterYearLevel, text="Year Level", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#e9aa73", bd=0).grid(row=15, column=1, padx=10, pady=10, sticky="w")
Button(entries_frame, command=filterSports, text="Sports", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#e9aa73", bd=0).grid(row=15, column=2, padx=10, pady=10, sticky="w")
Button(entries_frame, command=filterSex, text="Gender", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#e9aa73", bd=0).grid(row=15, column=3, padx=10, pady=10, sticky="w")

# hello
dispalyAll()
root.mainloop()
