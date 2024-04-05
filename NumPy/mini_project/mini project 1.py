import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    global photo  # Declare photo as a global variable
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)  # Update the image in the label
        frame3.grid(row=1, column=0, padx=20, pady=20, sticky='s')  # Move frame3 to the bottom


root = tk.Tk()
root.title("Image Editing Software")
root.configure(bg="white")

# Define brand color
brand_color = "#8A2BE2"  # Violet color code

# Function to set bold font
def bold_font(font_size):
    return f"{{Helvetica}} {font_size} bold"

# Frame to contain the label and button
frame1 = tk.Frame(root, bg="white", bd=2, relief=tk.RAISED)
frame1.grid(row=0, column=0, padx=20, pady=20)

frame2 = tk.Frame(root, bg="white", bd=2)
frame2.grid(row=1, column=0)

frame3 = tk.Frame(root, bg="white", bd=2)
frame3.grid(row=2, column=0, padx=20, pady=20, columnspan=2)

# Label with welcome text
welcome_label = tk.Label(frame1, text="Welcome to Image Editing Software!", bg="white", fg=brand_color, font=bold_font(14))
welcome_label.grid(row=0, column=0, padx=10, pady=10)

# Label to display the image
image_label = tk.Label(frame2, bg="white")
image_label.grid(row=0, column=0, padx=10, pady=10)

# Button to upload image
upload_button = tk.Button(frame3, text="Upload Image", bg=brand_color, fg="white", font=bold_font(12), command=upload_image)
upload_button.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5)

upload_button = tk.Button(frame3, text="Upload Image", bg=brand_color, fg="white", font=bold_font(12), command=upload_image)
upload_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)

upload_button = tk.Button(frame3, text="Upload Image", bg=brand_color, fg="white", font=bold_font(12), command=upload_image)
upload_button.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=5)


upload_button = tk.Button(frame3, text="Upload Image", bg=brand_color, fg="white", font=bold_font(12), command=upload_image)
upload_button.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=5)



root.mainloop()