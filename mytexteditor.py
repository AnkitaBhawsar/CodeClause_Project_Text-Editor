from tkinter import *
from tkinter import filedialog,messagebox

class MyNotePad:
    current_file = "no-file"
    def exit_file(self):
        s=self.txt_area.get(1.0,END)
        if not s.strip():
            quit()
        else:
            result=messagebox.askyesnocancel("Save Dialog Box","Do you want to save this file")
            if result==True:
                self.saveas_file() 
                quit()   
            elif result==False:
                quit()    


    def clear(self):
        self.txt_area.delete(1.0,END)

    def new_file(self):
        s=self.txt_area.get(1.0,END)
        if not s.strip():
            pass
        else:
            result=messagebox.askyesnocancel("Save Dialog Box","Do you want to save this file")
            if result==True:
                self.saveas_file()
                self.clear()
            elif result==False:
                self.clear()
    
    


    def saveas_file(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
        data=self.txt_area.get(1.0,END)
        f.write(data)
        self.current_file=f.name
        f.close()

    def save_file(self):
        if self.current_file=="no-file":
            self.saveas_file()
        else:
            f=open(self.current_file,mode="w")
            f.write(self.txt_area.get(1.0,END))
            f.close()
          
    

    def open_file(self,event=""):
        result=filedialog.askopenfile(initialdir="/",title="Open File dialog",filetypes=(("Text File","*.txt"),("All File","*.*")))
        #print(result)
        for data in result:
            self.txt_area.insert(INSERT,data)
        self.current_file = result.name
    def cut_file(self):
        self.copy_file()
        self.txt_area.delete('sel.first','sel.last')

    def del_file(self):
        self.txt_area.delete('sel.first','sel.last')

    def copy_file(self):
        self.txt_area.clipboard_clear()
        self.txt_area.clipboard_append(self.txt_area.selection_get())

    def paste_file(self):
        self.txt_area.insert(INSERT,self.txt_area.clipboard_get())    
        
    def __init__(self, master):
        self.master = master
        master.title("My Text Editor")
        master.bind("<Control-o>",self.open_file)
        master.bind("<Control-O>",self.open_file)

        self.txt_area = Text(master,padx=5,pady=5,wrap=WORD,selectbackground="blue", bd=2,insertwidth=3,undo=True)
        self.txt_area.pack(fill=BOTH,expand=1)

        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)
        
        #creating file menu
        self.file_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New",accelerator="Ctrl+n",command=self.new_file)
        self.file_menu.add_command(label="Open",accelerator="Ctrl+o",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save",command=self.save_file)
        self.file_menu.add_command(label="Save As",command=self.saveas_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.exit_file)

        ####################################
        #creating Edit menu
        self.edit_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="EDIT",menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo",command=self.txt_area.edit_undo)
        self.edit_menu.add_command(label="Redo",command=self.txt_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut",command=self.cut_file)
        self.edit_menu.add_command(label="Copy",command=self.copy_file)
        self.edit_menu.add_command(label="Paste",command=self.paste_file)
        self.edit_menu.add_command(label="Delete",command=self.del_file)





root = Tk()
b =MyNotePad(root)
root.mainloop()