import tkinter as ttk
from tkinter.filedialog import askopenfilename,asksaveasfilename


window = ttk.Tk()
window.title('text editor')
window.geometry('1045x650')
window.rowconfigure(0,minsize=45)
window.columnconfigure(1,minsize= 200)


def openFile(window,text):
    file = askopenfilename(filetypes=[("Text Files","*.txt")])
    if not file:
        return
    text.delete(1.0,ttk.END)

    with open(file,'r') as files:
        content = files.read()
        text.insert(ttk.END,content)
    window.title(f'file: {file}')




def main():
    
    text = ttk.Text(window,font='Helvetica 18')
    text.grid(row=1,column=0)
    frames = ttk.Frame(window,bd=2,relief=ttk.RAISED)
    frames.grid(row=0,column=0)
    save_btn = ttk.Button(frames,text="Save")
    open_btn = ttk.Button(frames,text="Open", command=lambda: openFile(window,text))


    save_btn.grid(row=0,column=0,sticky='w')
    open_btn.grid(row=0,column=1,sticky='w')



    window.mainloop()

main()