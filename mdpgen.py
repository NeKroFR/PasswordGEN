#import
from random import *
from tkinter import *

#caracter list
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','€','^','¨','£','$','¤','µ','*','ù','%','!','§',':','/',';','.',',','?','<','>','&','é','~',"'",'#','{','(','-','|','è','`','_','\ ','ç','^','à','@','°',')',']','+','=','}','/','*']



#crate the window
window=Tk()
window.title("PASSWORD GENERATOR")
window.geometry("750x500")
window.minsize(750,500)
window.maxsize(750, 500)
window.iconbitmap("img/logo.ico")
window.config(background="#1F2430")

#create the box
label_title = Label(window, text="ENTER THE LENGTH OF THE PASSWORRD HERE :", font=("Courrier", 15), bg=('#1F2430'), fg=('#3C8E81'))
label_title.pack()

entree = Entry(width=5)
entree.pack(padx=220, pady=25)
entree.focus_force()

#generation
def mdp_func (length):
    mdp = ""
    shuffle(characters)
    for x in range (length) :
        mdp+=characters[x]
    print(mdp)

length =int (input('Enter the length:'))
mdp_func(length)
input()

#show
frame.pack(expand=YES)
window.mainloop()
