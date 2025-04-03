import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os


def select_pdf():
    filepath = filedialog.askopenfilename(
        filetypes=[("DPF files", "*.pdf")], title="Select a PDF file"
    )
    if filepath:
        file_input.set(filepath)


def convert_pdf():
    pdf_path = file_input.get()
    if not pdf_path or not os.path.exists(pdf_path):
        messagebox.showerror(title="Error", message="Plaese select a valid PDF ")  # msg
        return

    docx_path = os.path.splitext(pdf_path)[0] + ".docx"

    try:
        converter = Converter(pdf_path)
        converter.convert(docx_path, start=0, end=None)
        converter.close()
        messagebox.showinfo(
            title="Sucess", message=f"Conversion completes! \nFile saved"
        )
    except Exception as e:
        messagebox.showerror(
            title="Error", message="An error occurred while converting the pdf"
        )


window = tk.Tk()
window.title("PDF to DOCX Converter")
window.geometry("400x200")
window.resizable(width=False, height=False)

file_input = tk.StringVar()

frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True, fill="both")

entry = tk.Entry(frame, textvariable=file_input, width=50)
entry.pack()

browse_button = tk.Button(frame, text="Browse PDF", command=select_pdf)
browse_button.pack(pady=5)

convert_button = tk.Button(frame, text="Convert to DOCX", command=convert_pdf)
convert_button.pack(pady=10)

window.mainloop()
