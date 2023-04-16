from tkinter import*
root=Tk()

root.title("ASCII keys")
root.geometry("600x600")

word=Entry(root)
word.place(relx=0.5,rely=0.2,anchor=CENTER)


label=Label(root,bg="purple",fg="white")
label.place(relx=0.5,rely=0.3,anchor=CENTER)

def converter():
    w=word.get()
    for i in w:
        label["text"]+=str(ord(i))+" "
        
btn=Button(root,text="ASCII",command=converter)      
btn.place(relx=0.5,rely=0.6,anchor=CENTER)  

root.mainloop()



