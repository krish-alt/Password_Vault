from initialize import*
from connection import*
from hash import*
from vaultscreen import*


def windowscreen():
    window.geometry("250x150")
    
    lbl = Label(window,text = "Create a Master password")
    lbl.config(anchor=CENTER)
    lbl.pack()
    txt = Entry(window ,width=15)
    txt.pack()
    txt.focus()
    
    lbl1 = Label(window,text = "Re Enter the  Master password")
    lbl1.pack()
    txt1 = Entry(window ,width=15 ,show='*')
    txt1.pack()
    
    lblerr = Label(window)
    lblerr.pack()
    
    def savePassword():
        if(txt.get() == txt1.get()):
            
                        
            hashedpass = hashedpassword(txt.get().encode('utf-8'))
            
            
            ins = """Insert into master (password)
            values (?);"""
            

            mycursor.execute(ins,[(hashedpass)])

            mydb.commit()
            
            passwordVault()
         
        else :
            txt1.delete(0,'end')
            lblerr.config(text="passwords does not match")
         
    btn = Button(window,text="Save" , command = savePassword)
    btn.pack(pady = 5)