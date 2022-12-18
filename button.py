import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('Tkinter Button Demo')

exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit()).pack()

root.mainloop()