from tkinter import  *
from tkinter import  messagebox
import  base64
import  os




def encrypt():
    global en_password
    en_password = code.get()
    mess = text1.get(1.0, END)
    ch = check(mess)
    if ch==True:
        messagebox.showerror("decryption", "Enter proper message")
    else:
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.config(bg="#ed3833")
        screen1.resizable(False,False)
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=10)
        text2 = Text(screen1, font="Roboto", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
        code.set("")
        text1.delete(1.0, END)

def check(mess):
    try:
        base64.b64encode(base64.b64decode(mess)) == mess
        return True
    except Exception:
        return  False



def decrypt():
    de_password = code.get()
    mess=text1.get(1.0, END)
    ch=check(mess)

    #s=text1.get(1.0,END)

    if ch==False:
        messagebox.showerror("decryption", "Invalid text")
        #print(mess)
        #print(ch)
    elif en_password == de_password:
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.config(bg="#00bd56")
        screen2.resizable(False, False)
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=10)
        text2 = Text(screen2, font="Roboto", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
        code.set("")
        text1.delete(1.0, END)
    elif de_password != en_password:
        messagebox.showerror("decryption", "wrong secret key")




def main_screen():

    global  screen
    global  code
    global text1




    screen=Tk()
    screen.geometry("500x600")

    #icon
    #image_icon=PhotoImage()
    #screen.iconphoto(image_icon)

    def reset():                                                      #function to text in the textbox
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=50,y=10)
    text1=Text(font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=0,y=50,width=500,height=150)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=30,y=250)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=30,y=300)

    Button(text="ENCRYPT",height="2",width=25,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=30,y=370)                         #encryption button
    Button(text="DECRYPT", height="2", width=25, bg="#00BD56", fg="white", bd=0,command=decrypt).place(x=260, y=370)                  #decryption button
    Button(text="RESET" ,height="2",width=54, bg="#1089ff",fg="white",bd=0,command=reset).place(x=30,y=430)           #reset button


    screen.title("Encrypter")
    screen.resizable(False,False)
    screen.mainloop()

main_screen()



