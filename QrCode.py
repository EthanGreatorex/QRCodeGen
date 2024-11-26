import qrcode
import tkinter as tk
import tempfile
import os

# Variables
BGCOLOR = '#0b0f12'
FONT = ("Arial", 30)
TEXTCOLOR = '#abff94'
WIDTH = 700
HEIGHT = 700
temp_dir = tempfile.mkdtemp()
file_path = os.path.join(temp_dir, "my_qrcode.png")

# Functions

def on_input_click(event):
  if website_input.get() == placeholder:
    website_input.delete(0,'end')

def on_input_leave(event):
  if website_input.get() == "":
    website_input.insert(0,placeholder)

def generateQrCode():
  # Get the website link the user entered
  website_link = website_input.get()

  # Generate a QR code instance
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
  )

  # Add data to the qr code
  qr.add_data(website_link)
  qr.make(fit=True)

  # Create an image from the QR code
  img = qr.make_image(fill_color="black", back_color="white")

  # Save the image and display to the user
  img.save(file_path)
  img.show()

def cleanup_temp_dir(temp_dir):
  import shutil
  shutil.rmtree(temp_dir)
  window.destroy()


# Create the window
window = tk.Tk()
window.title("QR Code Generator")

# Removes the border & title from the window


# Add some colour and sizing to the window
window.configure(background=BGCOLOR, width=WIDTH, height=HEIGHT)
window.eval('tk::PlaceWindow . center') # Places the window in the center of the screen


# Button to close the window
exit_button = tk.Button(window, text="X", command=window.destroy)

# Style the button and place it in the top left of the window
exit_button.configure(foreground=TEXTCOLOR, background=BGCOLOR,activebackground=BGCOLOR, activeforeground=TEXTCOLOR, font=FONT, borderwidth=0)
exit_button.place(x=640,y=10)

# Text for the header
header = tk.Label(window,text="Paste in your website link to generate\n a QR code",foreground=TEXTCOLOR, background=BGCOLOR, font=FONT)
header.place(x=20,y=120)

# Entry placeholder
placeholder = "Enter link here"
placeholder_colour = TEXTCOLOR

# Input for the user to enter website link
website_input = tk.Entry(window, width=20, fg=placeholder_colour, background="#152429", borderwidth=0 ,font=FONT, justify="center")
website_input.insert(0,placeholder)
website_input.bind("<FocusIn>", on_input_click)
website_input.bind("<FocusOut>", on_input_leave)

# Place the input on screen
website_input.place(x=130,y=350)

# Button to sumbit the input field
input_submit_button = tk.Button(window, text="Generate", command=generateQrCode)
input_submit_button.configure(background="#152429", foreground=TEXTCOLOR, width=10, borderwidth=0, font=FONT, activebackground=BGCOLOR, activeforeground=TEXTCOLOR)
input_submit_button.place(x=225,y=500)

# Set up the protocol handler for window close
window.protocol("WM_DELETE_WINDOW", lambda: cleanup_temp_dir(temp_dir))

# Updates the window continuously
window.mainloop()
