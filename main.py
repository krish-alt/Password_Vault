from hash import*
from popup import*
from initialize import*
from connection import*
from windowscreen import*
from loginscreen import *
from vaultscreen import *
   

mycursor.execute("select * from master")

if mycursor.fetchall() :
    loginscreen() 
else:
    windowscreen()

window.mainloop()