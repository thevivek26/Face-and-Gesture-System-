from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
os.makedirs("Images_Data",exist_ok=True)

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+0+0")
        self.root.title("Students Details")
        
        # ---------------- Title ------------------------
        title_label = Label(
            self.root,
            text="Student Details",
            font=("Segoe UI", 22, "bold"),
            bg="#f2f2f2",
            fg="#333333",
        )
        title_label.pack(pady=30)
        # title_label.lift()
        
        
        # ---------------- Main Frame ----------------
        main_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        main_frame.place(x=0, y=80, width=1200, height=640)

        # ---------------- Left Frame ----------------
        left_frame = LabelFrame(
            main_frame,
            text="Student Information",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )
        left_frame.place(x=20, y=20, width=560, height=580)
        
        
        # ---------------- Labels & Entries ----------------
        
        # ---------------- Student ID ----------------
        lbl_id = Label(left_frame, text="Student ID:", font=("Segoe UI", 12), bg="white")
        lbl_id.place(x=20, y=40)
        self.std_id_var=StringVar()
        self.txt_id = ttk.Entry(
            left_frame,
            font=("Segoe UI", 12),
            width=25,
            textvariable=self.std_id_var
        )
        self.txt_id.place(x=180, y=40)
        
        # ---------------- Course ----------------
        lbl_course = Label(left_frame, text="Course:", font=("Segoe UI", 12), bg="white")
        lbl_course.place(x=20, y=90)

        self.course_var = StringVar()
        course_combo = ttk.Combobox(
            left_frame,
            textvariable=self.course_var,
            font=("Segoe UI", 10),
            width=23,
            state="readonly"
        )
        course_combo["values"] = ("Select Course","B.Tech", "BCA", "MCA", "M.Tech")
        course_combo.current(0)
        course_combo.place(x=180, y=90)
        
        # ---------------- Department ----------------
        lbl_department = Label(left_frame, text="Department:", font=("Segoe UI", 12), bg="white")
        lbl_department.place(x=20, y=140)

        self.dep_var = StringVar()
        dep_combo = ttk.Combobox(
            left_frame,
            textvariable=self.dep_var,
            font=("Segoe UI", 10),
            width=23,
            state="readonly"
        )
        dep_combo["values"] = ("Select Department","CSE", "IT", "ECE", "ME", "Civil")
        dep_combo.current(0)
        dep_combo.place(x=180, y=140)
        

        # ---------------- Name ----------------
        lbl_name = Label(left_frame, text="Name:", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=20, y=190)
        self.name_var = StringVar()
        self.txt_name = ttk.Entry(
            left_frame,
            font=("Segoe UI", 12),
            width=25,
            textvariable=self.name_var
        )
        self.txt_name.place(x=180, y=190)

        

        # ---------------- Semester ----------------
        lbl_sem = Label(left_frame, text="Semester:", font=("Segoe UI", 12), bg="white")
        lbl_sem.place(x=20, y=240)

        self.sem_var = StringVar()
        sem_combo = ttk.Combobox(
            left_frame,
            textvariable=self.sem_var,
            font=("Segoe UI", 10),
            width=23,
            state="readonly"
        )
        sem_combo["values"] = ("Select Semester","1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.place(x=180, y=240)

        # ---------------- Roll No ----------------
        lbl_roll = Label(left_frame, text="Roll No:", font=("Segoe UI", 12), bg="white")
        lbl_roll.place(x=20, y=290)
        self.roll_var=StringVar()
        self.txt_roll = ttk.Entry(
            left_frame,
            font=("Segoe UI", 12),
            width=25,
            textvariable=self.roll_var
        )
        self.txt_roll.place(x=180, y=290)

        # ---------------- Phone ----------------
        lbl_phone = Label(left_frame, text="Phone No:", font=("Segoe UI", 12), bg="white")
        lbl_phone.place(x=20, y=340)
        self.phone_var=StringVar()
        self.txt_email = ttk.Entry(
            left_frame,
            font=("Segoe UI", 12),
            width=25,
            textvariable=self.phone_var
        )
        self.txt_email.place(x=180, y=340)

        # ---------------- Gender ----------------
        lbl_gender = Label(left_frame, text="Gender:", font=("Segoe UI", 12), bg="white")
        lbl_gender.place(x=20, y=390)

        self.gender_var = StringVar()
        gender_combo = ttk.Combobox(
            left_frame,
            textvariable=self.gender_var,
            font=("Segoe UI", 10),
            width=23,
            state="readonly"
        )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.place(x=180, y=390)

        # ---------------- Buttons ----------------
        btn_save = Button(
            left_frame,
            text="Save",
            width=12,
            command=self.add_data,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2"
        )
        btn_save.place(x=80, y=470)
        
        btn_update=Button(
            left_frame,
            text="Update",
            width=12,
            command=self.update_data,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2"            
        )
        btn_update.place(x=220,y=470)

        btn_reset = Button(
            left_frame,
            text="Reset",
            width=12,
            command=self.reset_data,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white",
            cursor="hand2"
        )
        btn_reset.place(x=360, y=470)
        
        
        # ---------------- Generate Dataset Button ----------------
        btn_dataset = Button(
            left_frame,
            text="Generate Dataset",
            width=25,
            command=self.generate_dataset,
            font=("Segoe UI", 12, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2"
        )
        btn_dataset.place(x=140, y=520)

        
        
        # ---------------- Right Frame (Reserved for Photo / Table) ----------------
        right_frame = LabelFrame(
            main_frame,
            text="Student Record",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )
        right_frame.place(x=610, y=20, width=560, height=580)
        
        #  ---------------Search System -------------------
        search_lbl=Label(right_frame, text="Search By:", font=("Segoe UI", 12), bg="white")
        search_lbl.place(x=20, y=40)
        self.search_var=StringVar()
        search_combo=ttk.Combobox(
            right_frame,
            textvariable=self.search_var,
            font=("Segoe UI", 10),
            width=18,
            state="readonly"
        )
        search_combo["values"] = ("Select", "Student ID", "Roll No", "Name")
        search_combo.current(0)
        search_combo.place(x=120, y=40)
        
        
        self.search_txt = ttk.Entry(
            right_frame,
            font=("Segoe UI", 10),
            width=18
        )
        self.search_txt.place(x=300, y=40)

        search_btn = Button(
            right_frame,
            text="Search",
            width=10,
            font=("Segoe UI", 11, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2"
        )
        search_btn.place(x=120, y=80)

        show_btn = Button(
            right_frame,
            text="Show All",
            width=10,
            font=("Segoe UI", 11, "bold"),
            bg="green",
            fg="white",
            cursor="hand2"
        )
        show_btn.place(x=240, y=80)
        
        
        
        # ---------------- Table Frame ----------------
        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        table_frame.place(x=10, y=130, width=540, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "id", "course", "dept","sem",
                "name","roll", "phone","gender"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("phone", text="Phone NO")
        self.student_table.heading("gender", text="Gender")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("sem", width=80)
        self.student_table.column("name", width=120)
        self.student_table.column("roll", width=100)
        self.student_table.column("phone", width=120)
        self.student_table.column("gender", width=80)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.curser_update)
        self.fetch_data()
    
    
    
    #  ---------- Function Decleration ----------------
    def add_data(self):
        if (
            self.std_id_var.get() == "" or
            self.name_var.get() == "" or
            self.course_var.get() == "Select Course" or
            self.dep_var.get() == "Select Department" or
            self.sem_var.get() == "Select Semester"
        ):
            messagebox.showerror("Error", "All fields are requireds",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vivek@#(vivek260)",
                    database="face_gesture"
                    )
                my_cursor = conn.cursor()
                
                my_cursor.execute(
                    """
                    INSERT INTO student
                    (course, dept, semester, student_id, name, roll_no, phone_no, gender)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        self.course_var.get(),
                        self.dep_var.get(),
                        self.sem_var.get(),
                        self.std_id_var.get(),
                        self.name_var.get(),
                        self.roll_var.get(),
                        self.phone_var.get(),
                        self.gender_var.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo(
                    "Success",
                    "Student details added successfully",
                    parent=self.root
                )
            except Exception as es:
                messagebox.showerror(
                    "Database Error",
                    f"Error due to : {str(es)}",
                    parent=self.root
                )
    
    # -----------Frtch Data --------------
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Vivek@#(vivek260)",
            database="face_gesture"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * from student")
        data=my_cursor.fetchall()
        
        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=(
                    i[3],  # student_id
                    i[0],  # course
                    i[1],  # dept
                    i[2],  # semester
                    i[4],  # name
                    i[5],  # roll_no
                    i[6],  # phone_no
                    i[7]   # gender
                    )
                )
            conn.commit()
        conn.close()
        
    # ----------------- Curser Update ----------------
    def curser_update(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.std_id_var.set(data[0])
        self.course_var.set(data[1])
        self.dep_var.set(data[2])
        self.sem_var.set(data[3])
        self.name_var.set(data[4])
        self.roll_var.set(data[5])
        self.phone_var.set(data[6])
        self.gender_var.set(data[7])

    # ---------- Update Button -------------
    def update_data(self):
        if (
            self.std_id_var.get() == "" or
            self.name_var.get() == "" or
            self.course_var.get() == "Select Course" or
            self.dep_var.get() == "Select Department" or
            self.sem_var.get() == "Select Semester"
        ):
            messagebox.showerror("Error", "All fields are requireds",parent=self.root)
        else:
            try:
                update=messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details?",
                    parent=self.root
                )
                
                if(update):
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Vivek@#(vivek260)",
                        database="face_gesture"
                    )
                    my_cursor=conn.cursor()
                    my_cursor.execute(
                        """
                        UPDATE student SET
                        course=%s,
                        dept=%s,
                        semester=%s,
                        name=%s,
                        roll_no=%s,
                        phone_no=%s,
                        gender=%s
                        WHERE student_id=%s
                        """,
                        (
                            self.course_var.get(),
                            self.dep_var.get(),
                            self.sem_var.get(),
                            self.name_var.get(),
                            self.roll_var.get(),
                            self.phone_var.get(),
                            self.gender_var.get(),
                            self.std_id_var.get()
                        )
                    )
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo(
                    "Success",
                    "Student details updated successfully",
                    parent=self.root
                )
            except Exception as es:
                messagebox.showerror(
                    "Database Error",
                    f"Error due to : {str(es)}",
                    parent=self.root
                )
                
    #  -------------- Reset Button ------------------
    def reset_data(self):
        self.std_id_var.set("")
        self.name_var.set("")
        self.roll_var.set("")
        self.phone_var.set("")
        self.course_var.set("Select Course")
        self.dep_var.set("Select Department")
        self.sem_var.set("Select Semester")
        self.gender_var.set("Select Gender")
        
        # Clear Treeview selection
        self.student_table.selection_remove(
            self.student_table.selection()
        )        
                
    # ------------- Generate data set ------------------
    def generate_dataset(self):
        if (
            self.std_id_var.get() == "" or
            self.name_var.get() == "" or
            self.course_var.get() == "Select Course" or
            self.dep_var.get() == "Select Department" or
            self.sem_var.get() == "Select Semester"
        ):
            messagebox.showerror("Error", "All fields are requireds",parent=self.root)
            return
        else:
            try:
                # ----------------- LOad Predifined data Frontal Face from opencv ----------------
                
                face_classifier = cv2.CascadeClassifier(
                    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                
                def crop_face(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if not ret:
                        break
                    # ✅ Always show live camera
                    cv2.imshow("Camera", my_frame)
                    face = crop_face(my_frame)
                    if face is not None:
                        img_id+=1
                        face=cv2.resize(face,(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name = f"Images_Data/user.{self.std_id_var.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name, face)
                        cv2.putText(
                            face, str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2
                        )
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result",
                    "Dataset generation completed!",
                    parent=self.root
                )
            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due to: {str(es)}",
                    parent=self.root
                )
                            
                    
                    
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 