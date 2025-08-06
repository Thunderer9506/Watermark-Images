import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from watermark import watermark

imagePath = ""

def open_file():
    global imagePath
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Images", "*.jpg"), ("All files", "*.*"))
    )

    if file_path:
        try:
            imagePath = file_path
            org_image = Image.open(file_path)
            resize_image = org_image.resize((192,108))
            tk_image = ImageTk.PhotoImage(resize_image)
            label_image['image'] = tk_image
            label_image.image = tk_image
            watermark_button.config(state=tk.NORMAL)
        except Exception as e:
            label_image["text"] = e

def addWatermark():
    status = watermark(imagePath)
    if status == True:
        messagebox.showinfo(title='Success',message="Image has been watermarked")
    else:
        messagebox.showerror(title='Error', message=status)

root = tk.Tk()
root.title("Watermark Image")
root.geometry("400x400")

label_image = tk.Label(root,text="Add an Image")
label_image.pack(pady=10)

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

watermark_button = tk.Button(root, text="Add WaterMark",state=tk.DISABLED,command=addWatermark)
watermark_button.pack(pady=10)




root.mainloop()
