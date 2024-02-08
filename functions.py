from tkinter.filedialog import askopenfilename,asksaveasfilename

def openFile(window,text,ttk):
    file = askopenfilename(filetypes=[("Text Files","*.txt")])
    if not file:
        return
    text.delete(1.0,ttk.END)

    with open(file,'r') as files:
        content = files.read()
        text.insert(ttk.END,content)
    window.title(f'file: {file}')

def savefile(window,text,ttk):
    file = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    file += ".txt"
    if not file:
        return
    with open(file,"w") as files:
        content = text.get(1.0,ttk.END)
        files.write(content)
    window.title(f'file: {file}')
