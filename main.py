"""
main.py

A simple Tkinter GUI application to add a watermark to images.
- Allows users to select an image file.
- Displays the selected image in the window.
- Adds a watermark to the image using the watermark() function from watermark.py.

Dependencies:
- tkinter
- PIL (Pillow)
- watermark.py (custom module)
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from watermark import watermark

# Global variable to store the path of the selected image
imagePath = ""

def open_file():
    """
    Opens a file dialog for the user to select an image.
    Displays the selected image in the GUI.
    Enables the watermark button if an image is selected.
    """
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
            label_image.image = tk_image  # Keep a reference to avoid garbage collection
            watermark_button.config(state=tk.NORMAL)
        except Exception as e:
            label_image["text"] = e

def addWatermark():
    """
    Calls the watermark function to add a watermark to the selected image.
    Shows a success or error message based on the result.

    In watermark function you can add dest_path to store watermarked image
    """
    status = watermark(imagePath)
    if status == True:
        messagebox.showinfo(title='Success', message="Image has been watermarked")
    else:
        messagebox.showerror(title='Error', message=status)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Watermark Image")
root.geometry("400x400")

# Label to display the image or instructions
label_image = tk.Label(root, text="Add an Image")
label_image.pack(pady=10)

# Button to open an image file
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Button to add a watermark (disabled until an image is loaded)
watermark_button = tk.Button(root, text="Add WaterMark", state=tk.DISABLED, command=addWatermark)
watermark_button.pack(pady=10)

# Start the Tkinter event loop