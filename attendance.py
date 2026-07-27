from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

os.makedirs("Images_Data", exist_ok=True)

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+0+0")
        self.root.title("Attendance Details")

        title_label = Label(
            self.root,
            text="Attendance Details",
            font=("Segoe UI", 22, "bold"),
            bg="#f2f2f2",
            fg="#333333",
        )
        title_label.pack(pady=30)

        # ---------------- Main Frame ----------------
        main_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        main_frame.place(x=0, y=80, width=1200, height=640)

        # ---------------- Left Frame ----------------
        left_frame = LabelFrame(
            main_frame,
            text="Student Attendance Details",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
        )
        left_frame.place(x=20, y=20, width=560, height=580)

        # ---------------- Labels & Entries ----------------

        # ----------Attendance ID --------------
        attendance_id = Label(
            left_frame, text="Attendance Id :", font=("Segoe UI", 12), bg="white"
        )
        attendance_id.place(x=20, y=40)
        self.attendance_id = StringVar() # variable
        self.txt_attendance = ttk.Entry(
            left_frame,
            textvariable=self.attendance_id,
            font=("Segoe UI", 12),
            width=25
        )
        self.txt_attendance.place(x=180, y=40)

        # -------------Name--------------
        name_lbl = Label(left_frame, text="Name :", font=("Segoe UI", 12), bg="white")
        name_lbl.place(x=20, y=90)
        self.name = StringVar() # variable
        self.txt_name = ttk.Entry(
            left_frame, 
            textvariable=self.name, 
            font=("Segoe UI", 12), 
            width=25
        )
        self.txt_name.place(x=180, y=90)

        #  ---------Roll NO --------------------
        roll_lbl = Label(
            left_frame, text="Roll No. :", font=("Segoe UI", 12), bg="white"
        )
        roll_lbl.place(x=20, y=140)
        self.roll_no = StringVar()  # variable
        self.txt_roll = ttk.Entry(
            left_frame, 
            textvariable=self.roll_no, 
            font=("Segoe UI", 12), 
            width=25
        )
        self.txt_roll.place(x=180, y=140)
        
        # ---------------------- Department ---------------------------
        departmet_lbl = Label(
            left_frame, text="Department :", font=("Segoe UI", 12), bg="white"
        )
        departmet_lbl.place(x=20, y=190)
        self.department = StringVar()
        self.txt_department = ttk.Entry(
            left_frame, 
            textvariable=self.department, 
            font=("Segoe UI", 12), 
            width=25
        )
        self.txt_department.place(x=180, y=190)

        # -----------Date----------------
        date_lbl = Label(left_frame, text="Date :", font=("Segoe UI", 12), bg="white")
        date_lbl.place(x=20, y=240)
        self.date = StringVar()
        self.txt_date = ttk.Entry(
            left_frame, 
            textvariable=self.date, 
            font=("Segoe UI", 12), 
            width=25
        )
        self.txt_date.place(x=180, y=240)

        # ---------------Time-------------
        time_lbl = Label(left_frame, text="Time :", font=("Segoe UI", 12), bg="white")
        time_lbl.place(x=20, y=290)
        self.time = StringVar()
        self.txt_time = ttk.Entry(
            left_frame, 
            textvariable=self.time, 
            font=("Segoe UI", 12), 
            width=25
        )
        self.txt_time.place(x=180, y=290)

        # -------------Attendance Lable ---------------
        attendance_lbl = Label(
            left_frame, text="Attendance Status", font=("Segoe UI", 12), bg="white"
        )
        attendance_lbl.place(x=20, y=340)
        self.attendance_lbl = StringVar()
        attend_combo = ttk.Combobox(
            left_frame,
            textvariable=self.attendance_lbl,
            font=("Segoe UI", 10),
            width=23,
            state="readonly",
        )
        attend_combo["values"] = ("Status", "Present", "Absent")
        attend_combo.current(0)
        attend_combo.place(x=180, y=340)

        # ---------------- Buttons ----------------
        btn_import_csv= Button(
            left_frame,
            text="Import CSV",
            width=12,
            command=self.importCSV,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2",
        )
        btn_import_csv.place(x=80, y=470)

        btn_export_csv = Button(
            left_frame,
            text="Export CSV",
            width=12,
            command=self.exportCSV,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2",
        )
        btn_export_csv.place(x=220, y=470)

        btn_reset = Button(
            left_frame,
            text="Reset",
            width=12,
            command=self.reset_data,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2",
        )
        btn_reset.place(x=360, y=470)

        # ---------------- Right Frame (Reserved for Photo / Table) ----------------
        right_frame = LabelFrame(
            main_frame,
            text="Attendance",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
        )
        right_frame.place(x=610, y=20, width=560, height=580)

        # ---------------- Table Frame ----------------
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=536, height=470)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id", "roll_no", "name", "dept", "date", "time", "atten_status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll_no", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dept", text="Department")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("atten_status", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll_no", width=100)
        self.AttendanceReportTable.column("name", width=120)
        self.AttendanceReportTable.column("dept", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("atten_status", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_curser)
        
        
    # ----------- Fetch Data --------------
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children()
            )
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)
    
    # ------------ Import CSV ---------
    def importCSV(self):
        global mydata
        mydata.clear()
        file_name=filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    # ------------ Export CSV -----------
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror(
                    "No Data",
                    "No data found to export",
                    parent=self.root
                    )
                return
            file_name = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                # defaultextension=".csv",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            )
            with open(file_name,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Success","CSV exported successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Due to : {str(es)}",
                parent=self.root
            )

            
    # ------------- Get Curser--------------------
    def get_curser(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.attendance_id.set(rows[0])
        self.name.set(rows[2])
        self.roll_no.set(rows[1])
        self.department.set(rows[3])
        self.date.set(rows[4])
        self.time.set(rows[5])
        self.attendance_lbl.set(rows[6])
        
    #  -------------- Reset Button ------------------
    def reset_data(self):
        self.attendance_id.set("")
        self.name.set("")
        self.roll_no.set("")
        self.department.set("")
        self.date.set("")
        self.time.set("")
        self.attendance_lbl.set("Select Status")
        # self.gender_var.set("Select Gender")
        
        # Clear Treeview selection
        self.student_table.selection_remove(
            self.student_table.selection()
        )
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
