from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np
import os



os.makedirs("Images_Data", exist_ok=True)


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+0+0")
        self.root.title("Face Recognition System")
        
        
        # -------- Title --------
        title_label = Label(
            self.root,
            text="Face Recognition",
            font=("Segoe UI", 22, "bold"),
            bg="#f2f2f2",
            fg="#333333",
        )
        title_label.pack(pady=30)
        
        detect_btn = Button(
            self.root,
            text="Start Face Recognition",
            command=self.face_recognition,
            font=("Segoe UI", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=22,
            height=2,
            relief=FLAT,
            cursor="hand2"
        )
        detect_btn.pack(pady=40)
        
        
    # -------------Mark Attendance -------------
    def mark_attendance(self, student_id, roll_no, name, dept):
        with open("marking.csv", "a+", newline="") as f:
            f.seek(0)
            lines = f.readlines()
            existing_ids = [line.split(",")[0] for line in lines]
            if str(student_id) not in existing_ids:
                now = datetime.now()
                time_str = now.strftime("%H:%M:%S")
                date_str = now.strftime("%d/%m/%Y")
                f.write(f"{student_id},{roll_no},{name},{dept},{time_str},{date_str},Present\n")
    
    
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            
            for (x, y, w, h) in features:
                id_, predict = clf.predict(gray[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
                
                if confidence > 80:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Vivek@#(vivek260)",
                        database="face_gesture"
                    )
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT student_id, name, dept, roll_no FROM student WHERE student_id=%s",
                        (id_,)
                    )
                    result = cursor.fetchone()
                    conn.close()
                    
                    if result:
                        student_id, name, dept, roll_no = result
                        
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                        cv2.putText(img, f"ID: {student_id}", (x, y-75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Name: {name}", (x, y-50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Dept: {dept}", (x, y-25),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Roll: {roll_no}", (x, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                        
                        # ✅ MARK ATTENDANCE HERE
                        self.mark_attendance(student_id, roll_no, name, dept)
                
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            
            return img
        faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            
            img = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            cv2.imshow("Face Recognition", img)
            
            if cv2.waitKey(1) == 13:  # ENTER
                break
        video_cap.release()
        cv2.destroyAllWindows()

    
    
    
    
       
#     # def face_recognition(self):
#     #     def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#     #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     #         features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
#     #         for (x, y, w, h) in features:
#     #             id_, predict = clf.predict(gray[y:y+h, x:x+w])
#     #             confidence = int(100 * (1 - predict / 300))
                
#     #             if confidence > 80:
#     #                 conn = mysql.connector.connect(
#     #                     host="localhost",
#     #                     username="root",
#     #                     password="Vivek@#(vivek260)",
#     #                     database="face_gesture"
#     #                 )
#     #                 my_cursor = conn.cursor()

#     #                 my_cursor.execute(
#     #                     "SELECT student_id, name, dept, roll_no FROM student WHERE student_id=%s",
#     #                     (id_,)
#     #                 )
#     #                 result = my_cursor.fetchone()
#     #                 conn.close()

#     #                 if result:
#     #                     student_id, name, dept, roll_no = result

#     #                     cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
#     #                     cv2.putText(img, f"ID: {student_id}", (x, y-75),
#     #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
#     #                     cv2.putText(img, f"Name: {name}", (x, y-50),
#     #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
#     #                     cv2.putText(img, f"Dept: {dept}", (x, y-25),
#     #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
#     #                     cv2.putText(img, f"Roll: {roll_no}", (x, y),
#     #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
#     #             else:
#     #                 cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
#     #                 cv2.putText(img, "Unknown", (x, y-10),
#     #                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
#     #         return img
#     #     faceCascade = cv2.CascadeClassifier(
#     #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
#     #         )
#     #     clf = cv2.face.LBPHFaceRecognizer_create()
#     #     clf.read("classifier.xml")
        
#     #     video_cap = cv2.VideoCapture(0)
#     #     while True:
#     #         ret, img = video_cap.read()
#     #         if not ret:
#     #             break
#     #         img = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
#     #         cv2.imshow("Face Recognition", img)
#     #         if cv2.waitKey(1) == 13:  # Enter key
#     #             break
#     #     video_cap.release()
#     #     cv2.destroyAllWindows()


# # ----------------Mark Attendance --------------
# def mark_attendance(self,id,roll_no,name,dept):
#     with open("marking.csv","r+",newline="\n") as atten:
#         my_data_list=atten.readlines()
#         name_list=[]
#         for line in my_data_list:
#             entry=line.split((","))
#             name_list.append(entry[0])
        
#         if((id not in name_list) and (roll_no not in name_list)and (name not in name_list)and (dept not in name_list)):
#             now=datetime.now()
#             date=now.strftime("%d/ %m/ %y")
#             dateString=now.strftime("%H:%M:%S")
#             atten.writelines(f"\{id},{roll_no},{name},{dept},{dateString},{date},Present")
            
        
#     def face_recognition(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
#             gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbour)
            
#             coord=[]
#             for(x,y,w,h) in features:
#                 cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
#                 id,predict=clf.predict(gray_img[y:y+h,x:x+w])
#                 confidence=int((100*(1-predict/300)))
                
#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     username="root",
#                     password="Vivek@#(vivek260)",
#                     database="face_gesture"
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("""SELECT student_id from student
#                                   WHERE student_id=""" +str(id))
#                 fetch_student_id=my_cursor.fetchone()
#                 fetch_student_id="+".join(fetch_student_id)
                
#                 my_cursor.execute("""SELECT dept from student
#                                   WHERE student_id=""" +str(id))
#                 fetch_dept=my_cursor.fetchone()
#                 fetch_dept="+".join(fetch_dept)
                
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("""SELECT name from student
#                                   WHERE student_id=""" +str(id))
#                 fetch_name=my_cursor.fetchone()
#                 fetch_name="+".join(fetch_name)
                
#                 my_cursor.execute("""SELECT roll_no from student
#                                   WHERE student_id=""" +str(id))
#                 fetch_roll_no=my_cursor.fetchone()
#                 fetch_roll_no="+".join(fetch_roll_no)
                
                
#                 my_cursor.execute("""SELECT student_id from student
#                                   WHERE student_id=""" +str(id))
#                 fetch_Id_for_attedance=my_cursor.fetchone()
#                 fetch_Id_for_attedance="+".join(fetch_Id_for_attedance)
                
#                 if(confidence>80):
#                     cv2.putText(
#                         img,f"student_id:{fetch_Id_for_attedance}",
#                         (x,y-55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255,255,255),
#                         2
#                     )
#                     cv2.putText(
#                         img,f"dept:{fetch_dept}",
#                         (x,y-55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255,255,255),
#                         2
#                     )
#                     cv2.putText(
#                         img,f"name:{fetch_name}",
#                         (x,y-55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255,255,255),
#                         2
#                     )
#                     cv2.putText(
#                         img,f"roll_no:{fetch_roll_no}",
#                         (x,y-55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255,255,255),
#                         2
#                     )
#                     self.mark_attendance(id,roll_no,name,dept)
#                 else:
#                     cv2.rectangle(img(x,y),(x+w.y+h),(0,0,255),3)
#                     cv2.putText(
#                         img,f"Unknown",
#                         (x,y-55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255,255,255),
#                         2
#                     )
#                 coord=[x,y,w,h]
#             return coord
        
#         def recognise(img,clf,faceCascade):
#             coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
#             return img
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")
        
#         video_cap=cv2.VideoCapture(0)
        
#         while True:
#             ret,img=video_cap.read()
#             img=recognise(img,clf,faceCascade)
#             cv2.imshow("Welcome to face recognition",img)
            
#             if(cv2.waitKey(1)==13):
#                 break
            
#             video_cap.release()
#             cv2.destroyAllWindows()
                
        
  
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()