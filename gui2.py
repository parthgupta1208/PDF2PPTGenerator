import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import tkinter.ttk as ttk

# Define a function to handle the file selection


def select_file():
    # Use the filedialog.askopenfilename() method to open a file dialog
    file_path = filedialog.askopenfilename(
        initialdir='/', title='Select a file', filetypes=[('PDF files', '*.pdf')])
    # Open the selected PDF file using PyPDF2 to check if it is a valid PDF file
    try:
        with open(file_path, 'rb') as file:
            print("{file_path}")
            messagebox.showinfo("taskbar", "your presentation is ready")
            file_path = filedialog.asksaveasfilename(defaultextension='.pptx',
                                                     filetypes=[('PowerPoint files', '*.pptx'),
                                                                ('All files', '*.*')])
        print(file_path)

        if file_path:
            os.system("START {file_path}")
    except:
        print(f"Error: Invalid PDF file selected ({file_path})")


# Create a Tkinter window
window = tk.Tk()
window.title("PDF File Selector")
window.geometry('600x400')

# Set the window to always be on top
window.attributes('-topmost', 1)

# Set the background color of the window using the configure method
window.configure(bg='#f2f2f2')

# Create a label widget
label = tk.Label(window, text="Please select a PDF file:",
                 bg='#f2f2f2', fg='#333333', font=('Arial', 14, 'bold'))
label.pack(pady=10)

# Create a button widget that triggers the select_file() function when clicked
button = tk.Button(window, text='Select File', command=select_file,
                   bg='#333333', fg='#f2f2f2', font=('Arial', 12, 'bold'), padx=10, pady=5)
button.pack(side=tk.BOTTOM, pady=10)

# Pack the label widget to fill the remaining space above the button
label.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
window.mainloop()
