import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import io
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

def generate_qr(event=None):
    url = url_entry.get()
    if not url:
        qr_label.config(image='')
        return
    
    error_correction = error_correction_var.get()
    color = color_var.get()
    size = size_var.get()

    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill=color, back_color='white')
    
    img.thumbnail((200, 200))
    
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    global qr_image
    qr_image = img

def save_qr():
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("SVG files", "*.svg"), ("PDF files", "*.pdf")])
        if file_path:
            if file_path.endswith(".png"):
                qr_image.save(file_path)
            elif file_path.endswith(".svg"):
                save_svg(file_path)
            elif file_path.endswith(".pdf"):
                save_pdf(file_path)
            messagebox.showinfo("Saved", f"QR code saved as {file_path}")
    else:
        messagebox.showerror("Error", "No QR code to save")

def save_svg(file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction_var.get(),
        box_size=size_var.get(),
        border=4,
    )
    qr.add_data(url_entry.get())
    qr.make(fit=True)
    img = qr.make_image(fill=color_var.get(), back_color='white')
    img.save(file_path, format="SVG")

def save_pdf(file_path):
    svg_path = io.BytesIO()
    save_svg(svg_path)
    svg_path.seek(0)
    drawing = svg2rlg(svg_path)
    renderPDF.drawToFile(drawing, file_path)

app = tk.Tk()
app.title("QR Code Generator")

url_label = tk.Label(app, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)
url_entry.bind("<KeyRelease>", generate_qr)

error_correction_var = tk.StringVar(value=qrcode.constants.ERROR_CORRECT_L)
color_var = tk.StringVar(value='black')
size_var = tk.IntVar(value=10)

options_frame = tk.Frame(app)
options_frame.pack(pady=10)

error_label = tk.Label(options_frame, text="Error Correction Level:")
error_label.grid(row=0, column=0, padx=5)

error_menu = tk.OptionMenu(options_frame, error_correction_var,
                           qrcode.constants.ERROR_CORRECT_L,
                           qrcode.constants.ERROR_CORRECT_M,
                           qrcode.constants.ERROR_CORRECT_Q,
                           qrcode.constants.ERROR_CORRECT_H)
error_menu.grid(row=0, column=1, padx=5)

color_label = tk.Label(options_frame, text="QR Color:")
color_label.grid(row=1, column=0, padx=5)

color_entry = tk.Entry(options_frame, textvariable=color_var)
color_entry.grid(row=1, column=1, padx=5)

size_label = tk.Label(options_frame, text="QR Size:")
size_label.grid(row=2, column=0, padx=5)

size_entry = tk.Entry(options_frame, textvariable=size_var)
size_entry.grid(row=2, column=1, padx=5)

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

qr_label = tk.Label(app)
qr_label.pack(pady=10)

save_button = tk.Button(app, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

qr_image = None

app.mainloop()
