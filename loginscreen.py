from initialize import*
from hash import*
from connection import*
from vaultscreen import*


def loginscreen() :
    window.geometry("350x150")
    
    lbl = Label(window, text = "Enter Master Password")
    lbl.config(anchor = CENTER)
    lbl.pack()
    
    txt = Entry(window, width=15,show='*')
    txt.focus()
    txt.pack()
    
    lbl1 = Label(window)
    lbl1.pack()
    
    
    def getPassword() :
        
        
        checkHashedpass = hashedpassword(txt.get().encode('utf-8'))
        mycursor.execute("select * from master where id = 1 and password = ?",[(checkHashedpass)])
        print(checkHashedpass)
        return mycursor.fetchall()
    
    def checkPassword() :
        
        match= getPassword()
        print(match)
        if match :
            passwordVault()
        else :
            txt.delete(0,'end')
            lbl1.config(text="wrong password")
    btn = Button(window,text="Submit",command=checkPassword)
    btn.pack(pady=10)