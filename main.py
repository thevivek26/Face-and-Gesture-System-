from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendance import Attendance
from gesture import GestureRecognition


class Face_Gesture_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+0+0")
        self.root.title("Face Gesture System")
        
        
        # ---------------- Background Image -------------
        img=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Background_Image.jpg")
        img=img.resize((1200, 700), Image.LANCZOS)
        
        self.bg_image = ImageTk.PhotoImage(img)
        
        # ----------- Set image as background using Label ----------
        bg_label = Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # ---------------- Title ------------------------
        title_label = Label(self.root,text="Face Gesture System",font=("Segoe UI", 28, "bold"),bg="black",fg="white")
        title_label.place(x=0, y=0, relwidth=1, height=60)
          
        
        # ---------------- Student Button ----------------
        img_student=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Students.jpg")
        img_student=img_student.resize((200, 200), Image.LANCZOS)
        self.student_img=ImageTk.PhotoImage(img_student)
        student_btn = Button(
            self.root,
            image=self.student_img,
            text="Student Details",
            command=self.student_details,
            compound="top",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        student_btn.place(x=100,y=120,width=200,height=220)
        
        # ---------------- Detect Face Button ----------------
        img_detect=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Detect_Face.webp")
        img_detect=img_detect.resize((200, 200), Image.LANCZOS)
        self.detect_img=ImageTk.PhotoImage(img_detect)
        detect_btn = Button(
            self.root,
            image=self.detect_img,
            text="Detect Face",
            command=self.face_data,
            compound="top",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        detect_btn.place(x=350, y=120, width=200, height=220)
        
        
        # ---------------- Attendance Button ----------------
        img_attendance=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Attendance_Image.jpeg")
        img_attendance=img_attendance.resize((200,200),Image.LANCZOS)
        self.attendance_img=ImageTk.PhotoImage(img_attendance)
        attendance_btn = Button(
            self.root,
            image=self.attendance_img,
            text="Attendance Details",
            command=self.attendance_data,
            compound="top",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        attendance_btn.place(x=600, y=120, width=200, height=220)
        
        
        
        # ---------------- Gesture Button ----------------
        img_gesture=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Photo.jpg")
        img_gesture = img_gesture.resize((200, 200), Image.LANCZOS)
        self.gesture_img = ImageTk.PhotoImage(img_gesture)
        
        gesture_btn = Button(
            self.root,
            image=self.gesture_img, 
            text="Gestures",
            command=self.open_gesture,
            compound="top",
            # bg="#2196F3",
            # fg="white",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        gesture_btn.place(x=100, y=380, width=200, height=220)
        
        
        
        # ---------------- Train Button ----------------
        img_train=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Train_Image.jpg")
        img_train = img_train.resize((200, 200), Image.LANCZOS)
        self.train_img = ImageTk.PhotoImage(img_train)
        train_btn = Button(
            self.root,
            image=self.train_img,
            text="Train Data",
            command=self.train_data,
            compound="top",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        train_btn.place(x=350, y=380, width=200, height=220)
        
        # ---------------- Photos Button ----------------
        img_photo=Image.open(r"C:\Users\vivek\OneDrive\Desktop\Face_Gesture_System\Images\Photo.jpg")
        img_photo = img_photo.resize((200, 200), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img_photo)
        
        photo_btn = Button(
            self.root,
            image=self.photo_img, 
            text="Photos",
            command=self.open_img,
            compound="top",
            font=("Segoe UI", 14, "bold"),
            cursor="hand2",
            borderwidth=0
        )
        photo_btn.place(x=600, y=380, width=200, height=220)
        
    # ------------ Open Images --------------
    
    def open_img(self):
        os.startfile("Images_Data")
        
    # ------------- Function Button ----------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def open_gesture(self):
        gesture = GestureRecognition()
        gesture.start()

    
    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Gesture_System(root)
    root.mainloop()