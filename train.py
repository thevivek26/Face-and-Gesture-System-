from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

os.makedirs("Images_Data", exist_ok=True)


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500+250+100")
        self.root.title("Train Data")

        # -------- Main Background --------
        self.root.configure(bg="#f2f2f2")  # soft light gray

        # -------- Title --------
        title_label = Label(
            self.root,
            text="Train Face Dataset",
            font=("Segoe UI", 22, "bold"),
            bg="#f2f2f2",
            fg="#333333",
        )
        title_label.pack(pady=30)
        
        # -------- Info Text --------
        info_label = Label(
            self.root,
            text="Click the button below to train the model using captured images.",
            font=("Segoe UI", 11),
            bg="#f2f2f2",
            fg="#555555",
        )
        info_label.pack(pady=10)

        # -------- Train Button --------
        train_btn = Button(
            self.root,
            text="Start Training",
            command=self.train_classifier,
            font=("Segoe UI", 12, "bold"),
            bg="#4CAF50",  # soft green
            fg="white",
            activebackground="#45a049",
            cursor="hand2",
            relief=FLAT,
            width=18,
            height=2,
        )
        train_btn.pack(pady=40)
    
    # -------- Training Logic (Placeholder) --------
    
    def train_classifier(self):
        data_dir = "Images_Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        if not path:
            messagebox.showerror("Error", "No images found in Images_Data folder")
            return

        faces = []
        ids = []
        for image_path in path:
            img = Image.open(image_path).convert("L")  # grayscale
            img_np = np.array(img, "uint8")
            id = int(os.path.split(image_path)[1].split(".")[1])

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)

        # -------- Train Classifier --------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        # self.root.update()

        messagebox.showinfo(
            "Training Completed",
            "Model trained successfully!\nclassifier.xml saved.",
            parent=self.root,
        )


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
