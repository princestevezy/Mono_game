from tkinter import*
import platform
from ttkbootstrap.constants import*
import ttkbootstrap as b
import random
from PIL import Image,ImageTk
from tkinter import messagebox
root=b.Window(themename="darkly")
root.geometry('500x350')
root.title('Mono Game')
icon=b.PhotoImage(file='m.png')
root.iconphoto(False, icon)
frame=b.Frame(root,height=800)
frame.pack(fill=BOTH,expand=True)

canvas=b.Canvas(frame,scrollregion=(0,0,200,500))
canvas.pack(side=LEFT,fill=BOTH,expand=True)
scroll=b.Scrollbar(frame,orient=VERTICAL, bootstyle='danger round', command=canvas.yview)
scroll.pack(side=RIGHT,fill=Y)
canvas.config(yscrollcommand=scroll.set)

frame_inner=b.Frame(canvas)
canvas.create_window((0,0), window=frame_inner)


number1=[]
number2=[10,11,12,13]
Wallet=int(0)
attempts=StringVar()
a1=0
mywins=StringVar()
w1=0
n=b.StringVar()
n2=b.StringVar()

     
def startgame():
    global Wallet
    global number1
    global number2
    global a1
    global w1
    check_option()
    if (len(ge.get()))==2:
       c=ge.get()
       if int(c) in number1:
          pass
          anwser=random.choice(number1)
          if ge.get()==str(anwser):
              Wallet+=int(2000)
              n.set(str(Wallet))
              x=combo.get()
              a1+=int(1)
              attempts.set(str(a1))
              w1+=int(1)
              mywins.set(str(w1))
              messagebox.showinfo('Oposition Response (Level:'+str(x)+')','Your Oposition Guessed ' +str(anwser)+' Which you Predicted Correctly,2000 Naira has been added to your wallet')
              del number1[:]
          else:
                 x=combo.get()
                 a1+=int(1)
                 attempts.set(str(a1))
                 messagebox.showinfo('Oposition Response (Level:'+str(x)+')','Your Oposition Guessed ' +str(anwser)+' Which You Predicted Wrongly')
                 del number1[:]
                 
       else:
              messagebox.showerror('Invalid Value','The Number you inputted is not part of the Game number set')
              del number1[:]
               
    else:
              messagebox.showerror('Invalid Value Lenght','Please Make Sure Your Max Value Is 2')
              del number1[:]
              




def check_option():
     global number1
     global number2
     x=combo.get()
     if x=='Easy':
         number1.extend([11,12,13,14,15,16])
         n2.set(str(number1))
         pass
     elif x=='Hard':
         number1.extend([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
         n2.set(str(number1))
         pass
     elif x=='Very Hard':
         number1.extend([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
         n2.set(str(number1))
         pass   
     else:
        messagebox.showerror('Invalid Value','Option not found') 




attempts.set(str(a1))
mywins.set(str(w1))
c=b.Label(text='',font=("Helvetica",60),bootstyle=DEFAULT)
c.pack(pady=10)
img=Image.open('m.png')
img_tk=ImageTk.PhotoImage(img)
label=b.Label(frame_inner,image=img_tk)
label.pack(padx=10,pady=5)
n.set(str(Wallet))
amount=b.Label(frame_inner,text='Amount/Naira',font=("Helvetica",12),bootstyle=DEFAULT)
amount.pack(padx=10,pady=5)
amount1=b.Label(frame_inner,textvariable=f'{n}',font=("Helvetica",12),bootstyle=DEFAULT)
amount1.pack(pady=10)
win=b.Label(frame_inner,text='Win:' ,font=("Helvetica",12),bootstyle=DEFAULT)
win.pack(pady=5)
win1=b.Label(frame_inner,textvariable=f'{mywins}',font=("Helvetica",12),bootstyle=DEFAULT)
win1.pack(pady=10)
at=b.Label(frame_inner,text='Attempts',font=("Helvetica",12),bootstyle=DEFAULT)
at.pack(pady=5)
attempts1=b.Label(frame_inner,textvariable=f'{attempts}',font=("Helvetica",12),bootstyle=DEFAULT)
attempts1.pack(pady=10)
ge=b.Entry(frame_inner,font=("Helvetica",20),width='4',bootstyle=DEFAULT)
ge.pack(pady=20)
c=b.Label(frame_inner,text='',font=("Helvetica",10),bootstyle=DEFAULT)
c.pack(pady=10)
style=b.Style()
style.configure('TCombobox', font=('Helvetica',60))
options=['Easy','Hard','Very Hard']
combo=b.Combobox(frame_inner,values=options,style='TCombobox')
combo.pack(padx=10,pady=10)
c=b.Label(text='',font=("Helvetica",10),bootstyle=DEFAULT)
c.pack(pady=10)
my_style=b.Style()
my_style.configure("TButton",font=("Arial",10))
gb=b.Button(frame_inner,text='Submit Your Number',bootstyle='primary toolbutton,outline', width=40,padding=20,style='TButton',command=startgame)
gb.pack(pady=30)

messagebox.showinfo("About Mono Game","Welcome To Mono.A Game which allows you to Play A Game of Predictions With The System Using Only Numbers.Levels In This Game consist of Easy(For Easy you Will Have To Guess Between 11 to 16).Hard(For Hard You Will Have To Guess Between 11 to 25.Very Hard(For very Hard You Will Have To Guess Between 11 to 30)")
#frame
canvas.place(relx=0.5, rely=0.5,anchor=CENTER)
frame_inner.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()





