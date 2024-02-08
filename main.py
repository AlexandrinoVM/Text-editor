import tkinter as ttk

window = ttk.Tk()
window.title('text editor')
window.geometry('1045x650')

window.minsize(1045,650)
window.maxsize(1045,650)

text = ttk.Text(window,font='Helvetica 18')
text.grid(row=0,column=1)



window.mainloop()

