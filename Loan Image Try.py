from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window1 = Tk()
window1.title('Home')
window1.geometry('1366x768')
img = Image.open(r'C:/Users/Elambharathi/Downloads/loantitle1.png')
photo = ImageTk.PhotoImage(img)
lab1 = Label(image = photo)
lab1.pack()
#mainloop()
large_font = ('Verdana',15)


name_entered      = StringVar()
age_entered       = StringVar()
dob_entered       = StringVar()
dob_entered.set("DD/MM/YYYY")
address_entered   = StringVar() 
zip_entered       = StringVar()
phone_entered     = StringVar()
email_entered     = StringVar()
amount_entered    = IntVar()
interest_entered  = IntVar()
male_box          = IntVar()
female_box        = IntVar()
loanterm_entered  = StringVar()
loanterm2_entered = StringVar()
minterest_entered = IntVar()

check_male      = Checkbutton(window1,text='',font=('Halvetica',15),var=male_box).place(x=560,y=125)
check_female    = Checkbutton(window1,text='',font=('Halvetica',15),var=female_box).place(x=680,y=125)


entry_name      = Entry(window1,textvar=name_entered,font=large_font,width=20).place(x=200,y=92)
entry_age       = Entry(window1,textvar=age_entered,font=large_font,width=5).place(x=850,y=90)
entry_dob       = Entry(window1,textvar=dob_entered,font=large_font,width=15).place(x=1140,y=90)
entry_address   = Entry(window1,textvar=address_entered,font=large_font,width=50).place(x=200,y=212)
entry_zip       = Entry(window1,textvar=zip_entered,font=large_font,width=15).place(x=1105,y=210)
entry_phone     = Entry(window1,textvar=phone_entered,font=large_font,width=25).place(x=250,y=275)
entry_email     = Entry(window1,textvar=email_entered,font=large_font,width=25).place(x=920,y=277)
entry_amount    = Entry(window1,textvar=amount_entered,font=large_font,width=15).place(x=240,y=565)
entry_interest  = Entry(window1,textvar=interest_entered,font=large_font,width=15).place(x=920,y=565)


loanterm_list=['1 Months','2 Months','3 Months','4 Months','5 Months','6 Months']
droplist=OptionMenu(window1,loanterm_entered,*loanterm_list)
loanterm_entered.set('Select term')
droplist.config(width=20)
droplist.place(x=210,y=415)

def exitclicked():
    print('')

imgsubmit = Image.open(r'C:/Users/Elambharathi/Downloads/submit1.png')
photosubmit = ImageTk.PhotoImage(imgsubmit)
button_submit     = Button(window1,image= photosubmit,command = exitclicked).place(x=820,y=640)

imgquit = Image.open(r'C:/Users/Elambharathi/Downloads/quit1.png')
photoquit = ImageTk.PhotoImage(imgquit)
button_quit     = Button(window1,image= photoquit,command = exitclicked).place(x=950,y=640)

imgvalidate = Image.open(r'C:/Users/Elambharathi/Downloads/validate1.png')
photovalidate = ImageTk.PhotoImage(imgvalidate)
button_validate     = Button(window1,image= photovalidate,command = exitclicked).place(x=1070,y=640)

loanterm2_list = ['12 Months','18 Months','24 Months','30 Months','36 Months','42 Months']
droplist2 =OptionMenu(window1,loanterm2_entered,*loanterm2_list)
loanterm2_entered.set('Select term')
droplist2.config(width=20)
droplist2.place(x=870,y=415)





