from tkinter import*
import math
def sair():
    bradesco.destroy()
def calcular():
    ent1 = (entrybradesco.get())
    carc1 = int(ent1[0:1])*5
    carc2 = int(ent1[1:2])*4
    carc3 = int(ent1[2:3])*3
    carc4 = int(ent1[3:4])*2
    total = int(((carc1+carc2+carc3+carc4)%11-11)*-1)
    if (total==10)or(total==11):
        final = "0"
    else:
        final = total
   
    bradescoresult = Label(bradesco,text=final, font="IMPACT 60", bg="DARK GREY").place(x=230,y=135)                               
bradesco = Tk()
bradesco['bg'] = "DARK GREY"
bradesco.title("BRADESCO")
bradesco.geometry("300x350")
bradescotitle = Label(bradesco, text="BRADESCO",font="IMPACT 40", bg="DARK GREY").place(x=40,y=5)
bradescititle2 = Label(bradesco, text="CALCULAR DÍGITO AGÊNCIA", font="IMPACT 15", bg="DARK GREY").place(x=40,y=65)
bradescolinha = Label(bradesco, text="="*99, bg="DARK GREY").place(x=0,y=90)
entrybradesco = Entry(bradesco, font="IMPACT 60", bg="DARK GREY")
entrybradesco.place(x=5,y=150,width=175, height=80)
entryvradescol = Label(bradesco, text="-", font="IMPACT 60", bg="DARK GREY").place(x=180,y=135)
buttonbradesco = Button(bradesco, text="CALCULAR", font="IMPACT 15", bg="DARK GREY", pady=15, padx=20, command=calcular).place(x=2,y=275)
buttonbradesco2 = Button(bradesco, text="SAIR", font="IMPACT 15", bg="DARK GREY", pady=15, padx=50, command=sair).place(x=147,y=275)
bradesco.resizable(0,0)
bradesco.mainloop()
