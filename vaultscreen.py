from initialize import*
from connection import*
from popup import*
from functools import partial


def passwordVault() :
    for widget in window.winfo_children():
        widget.destroy()
        
    def addEntry():
        text1 = "Website"
        text2 = "Username"
        text3 = "Password"
        
        website = popup(text1)
        username = popup(text2)
        password = popup(text3)
        
        insert_fields = """insert into vault(website,username,password) values(?,?,?)"""
        
        mycursor.execute(insert_fields,(website,username,password))
        mydb.commit()
        
        passwordVault()
        
    def removeEntry(input):
        mycursor.execute("delete from vault where Id = ?" , (input,))
        mydb.commit()
        passwordVault()
        
    window.geometry("700x350")
    
  
    
    lbl = Label(window,text = "Your Password vault")
    lbl.grid(column=1)
    
    btn = Button(window,text="+" ,command=addEntry)
    btn.grid(column=1 , pady=10)
    
    lbl = Label(window,text="Website")
    lbl.grid(column=0 , row=2, padx=80)
    lbl = Label(window,text="Username")
    lbl.grid(column=1 , row=2, padx=80)
    lbl = Label(window,text="Password")
    lbl.grid(column=2 , row=2, padx=80)
    
    mycursor.execute("select * from vault")
    if(mycursor.fetchall() != None):
        i=0
        while True :
            mycursor.execute("select * from vault")
            array = mycursor.fetchall()
            
            lbl1 = Label(window,text=array[i][1])
            lbl1.grid(column=0,row=i+3)
            lbl1 = Label(window,text=array[i][2])
            lbl1.grid(column=1,row=i+3)
            lbl1 = Label(window,text=array[i][3])
            lbl1.grid(column=2,row=i+3)
            
            btn =Button(window,text="Delete" , command=partial(removeEntry,array[i][0]))
            btn.grid(column=3 , row= i+3,pady=10)
            
            i=i+1
            
            mycursor.execute("select * from vault")
            
            if(len(mycursor.fetchall())<=i):
                break