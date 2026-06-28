import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("GUI start")
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack()

root.mainloop()