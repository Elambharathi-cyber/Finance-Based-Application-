from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
windowh = Tk()
windowh.title('ETS Finance')
windowh.iconbitmap(r"C:/Users/Elambharathi/Downloads/Bharathi/CCC/myicon.ico")
imge = Image.open("C:/Users/Elambharathi/Downloads/Bharathi/CCC/DD.png")
photo = ImageTk.PhotoImage(imge)
lab = Label(image = photo)
lab.pack()

def quiting():
    quit()
def ourinfo():
    messagebox.showinfo("Info",'This application is developed for our Class XII C.S Project')
def copyinfo():
    messagebox.showinfo("Ownership",'This application is solely developed and owened by B.M.Thanvanth and P.T.Elambharathi of class XII')
    
    
    
def loanform():
    windowh.destroy()
    import sqlite3
    from tkinter import messagebox
    from PIL import Image,ImageTk
    window1 = Tk()
    window1.title('Home')
    window1.geometry('1366x768')
    img = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/loantitle1.png')
    photo = ImageTk.PhotoImage(img)
    lab1 = Label(image = photo)
    lab1.pack()
    large_font = ('Verdana',15)
    window1.iconbitmap(r"C:/Users/Elambharathi/Downloads/Bharathi/CCC/myicon2.ico")



    #Input definitons
    name_entered      = StringVar()
    age_entered       = StringVar()
    dob_entered       = StringVar()
    dob_entered.set("DD/MM/YYYY")
    address_entered   = StringVar() 
    zip_entered       = StringVar()
    phone_entered     = StringVar()
    email_entered     = StringVar()
    amount_entered    = IntVar()
    interest_entered  = DoubleVar()
    male_box          = IntVar()
    female_box        = IntVar()
    loanterm_entered  = StringVar()
    loanterm2_entered = StringVar()
    minterest_entered = IntVar()
    
    def validateclicked():
        name       = name_entered.get()
        age        = age_entered.get()
        dob        = dob_entered.get()
        zip1       = zip_entered.get()
        phone      = phone_entered.get()
        address    = address_entered.get()
        email      = email_entered.get()
        amount     = amount_entered.get()
        interest   = interest_entered.get()
        male       = male_box.get()
        female     = female_box.get()
        loanterm   = loanterm_entered.get()
        loanterm2  = loanterm2_entered.get()
        loanfinal  = ''
        loantype = ''
    
        if name=='' or age =='' or dob =="DD/MM/YYYY" or zip1 =='' or address == '' or phone =='' or email =='' or interest==0 or amount==0 or (male_box.get() ==False and female_box.get() == False) or (loanterm=='Select term' and loanterm2 =='Select term') :
            messagebox.showinfo("Error",'Please enter all the fields')
        
        else:
            global value1
            value1 = (amount)*((interest)/100)
            labelinterestvalue = Label(window1,text=value1,bg='white',font=('Halvetica',15)).place(x=310,y=665)

    def submitclicked():
        name       = name_entered.get()
        name       = name.upper() 
        age        = age_entered.get()
        address    = address_entered.get()
        dob        = dob_entered.get()
        zip1       = zip_entered.get()
        phone      = phone_entered.get()
        email      = email_entered.get()
        amount     = amount_entered.get()
        interest   = interest_entered.get()
        male       = male_box.get()
        female     = female_box.get()
        loanterm   = loanterm_entered.get()
        loanterm2  = loanterm2_entered.get()
        loanfinal  = ''
        loantype = ''
        gender = ''
    
    
        if male==True:
            gender = 'Male'
        elif female == True:
            gender = 'Female'
        if loanterm=='Select term':
            loanfinal = loanterm2
            loantype = 'Long Term'
        elif loanterm2 =='Select term':
            loanfinal = loanterm
            loantype = 'Short term'

        conn = sqlite3.connect("firstdb.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute('INSERT INTO FINALE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,age,dob,gender,address,zip1,email,phone,amount,interest,value1,loanfinal,loantype))
        conn.commit()
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("cccetsfinance@gmail.com", "financelogin")
        SUBJECT = 'Loan Approved'
        TEXT = 'Hi '+(name+','+'\n'+'\n')+('Your Loan application is successfully submited !'+'\n'+'\n')+('Loan Amount is: '+(str(amount)+'\n'))+('Monthly Interest is: '+(str(value1)+'\n'))+('Loan Durations is: '+(loanfinal+'\n'))+('Loan Type is: '+(loantype+'\n'+'\n'))+'Warmest Regards'+'\n'+'ETS Finance'           
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("cccetsfinance@gmail.com",email, message)
        s.quit()
        messagebox.showinfo("Successful",'Application Submited')
        
        
        
    def exitclicked():
        quit()


    #Font definitions
    large_font = ('Verdana',15)


    #List of Check Buttons,Buttons
    check_male      = Checkbutton(window1,text='',font=('Halvetica',15),var=male_box).place(x=560,y=145)
    check_female    = Checkbutton(window1,text='',font=('Halvetica',15),var=female_box).place(x=680,y=145)

    imgsubmit = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/submit1.png')
    photosubmit = ImageTk.PhotoImage(imgsubmit)
    button_submit     = Button(window1,image= photosubmit,command = submitclicked).place(x=820,y=650)

    imgquit = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/quit1.png')
    photoquit = ImageTk.PhotoImage(imgquit)
    button_quit     = Button(window1,image= photoquit,command = exitclicked).place(x=950,y=650)

    imgvalidate = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/validate1.png')
    photovalidate = ImageTk.PhotoImage(imgvalidate)
    button_validate     = Button(window1,image= photovalidate,command = validateclicked).place(x=1070,y=650)
    

    #List of Entry Widgets
    entry_name      = Entry(window1,textvar=name_entered,font=large_font,width=20).place(x=200,y=112)
    entry_age       = Entry(window1,textvar=age_entered,font=large_font,width=5).place(x=850,y=110)
    entry_dob       = Entry(window1,textvar=dob_entered,font=large_font,width=15).place(x=1140,y=110)
    entry_address   = Entry(window1,textvar=address_entered,font=large_font,width=50).place(x=200,y=232)
    entry_zip       = Entry(window1,textvar=zip_entered,font=large_font,width=15).place(x=1105,y=230)
    entry_phone     = Entry(window1,textvar=phone_entered,font=large_font,width=25).place(x=250,y=295)
    entry_email     = Entry(window1,textvar=email_entered,font=large_font,width=25).place(x=920,y=297)
    entry_amount    = Entry(window1,textvar=amount_entered,font=large_font,width=15).place(x=240,y=585)
    entry_interest  = Entry(window1,textvar=interest_entered,font=large_font,width=15).place(x=920,y=585)


    #List of Drop Lists
    loanterm_list=['1 Months','2 Months','3 Months','4 Months','5 Months','6 Months']
    droplist=OptionMenu(window1,loanterm_entered,*loanterm_list)
    loanterm_entered.set('Select term')
    droplist.config(width=20)
    droplist.place(x=210,y=435)

    loanterm2_list = ['12 Months','18 Months','24 Months','30 Months','36 Months','42 Months']
    droplist2 =OptionMenu(window1,loanterm2_entered,*loanterm2_list)
    loanterm2_entered.set('Select term')
    droplist2.config(width=20)
    droplist2.place(x=870,y=435)
    window1.mainloop()

def loanstatus():
    windowh.destroy()
    import sqlite3
    from tkinter import messagebox
    from PIL import Image,ImageTk
    windows = Tk()
    windows.geometry('911x517')
    windows.title('Loan Status Chech')
    
    img = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/titled.png')
    photo = ImageTk.PhotoImage(img)
    lab1 = Label(image = photo)
    lab1.pack()
    windows.iconbitmap(r"C:/Users/Elambharathi/Downloads/Bharathi/CCC/myicon3.ico")
    t=''

    imgotp = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/otp.png')
    photootp = ImageTk.PhotoImage(imgotp)
    

    imgcheck = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/check.png')
    photocheck = ImageTk.PhotoImage(imgcheck)
    

    imgquit = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/quit.png')
    photoquit = ImageTk.PhotoImage(imgquit)

    global out_entered
    otp_entered=IntVar()
    dob_entered=StringVar()
    dob_entered.set("DD/MM/YYYY")
    global name_entered
    name_entered=StringVar()

    large_font = ('Verdana',15)

    def exitclicked():
        quit()
    def newcmd():
        
        global name
        name = name_entered.get()
        name = name.upper()
        otp  = otp_entered.get()
        global dob
        dob = dob_entered.get()
        if otpval==otp:
            if (name,) in data1 and (dob,) in data2:
                windows.destroy()
                conn = sqlite3.connect("firstdb.db")
                with conn:
                    cursor = conn.cursor()
                genderdata = cursor.execute("select Gender from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for i in genderdata:
                    global gendervalue
                    gendervalue = i
                
                gendervalue = gendervalue[0]
                addressdata = cursor.execute("select Address from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for j in addressdata:
                    global addressvalue
                    addressvalue = j
                
                addressvalue = addressvalue[0]
                pindata = cursor.execute("select PIN_Code from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for k in pindata:
                    global pinvalue
                    pinvalue = k
               
                pinvalue = pinvalue[0]
                emaildata = cursor.execute("select Email from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for l in emaildata:
                    global emailvalue
                    emailvalue = l
                
                emailvalue = emailvalue[0]
                phonedata = cursor.execute("select Phone from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for m in phonedata:
                    global phonevalue
                    phonevalue = m
                
                phonevalue = phonevalue[0]
                lamountdata = cursor.execute("select Loan_Amount from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for n in lamountdata:
                    global lamountvalue
                    lamountvalue = n
                
                lamountvalue = lamountvalue[0]
                linterestdata = cursor.execute("select Loan_Interest from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for o in linterestdata:
                    global linterestvalue
                    linterestvalue = o
                
                linterestvalue = linterestvalue[0]
                minterestdata = cursor.execute("select Monthly_Interest from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for p in minterestdata:
                    global minterestvalue
                    minterestvalue = p
                
                minterestvalue = minterestvalue[0]
                termdata = cursor.execute("select Loan_Term from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for q in termdata:
                    global termvalue
                    termvalue = q
                
                termvalue = termvalue[0]
                typedata = cursor.execute("select Loan_Type from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for r in typedata:
                    global typevalue
                    typevalue = r
                
                typevalue = typevalue[0]
                agedata = cursor.execute("select Age from FINALE WHERE Name='%s' and DOB='%s'"%(name,dob))
                for s in agedata:
                    global agevalue
                    agevalue = s
                agevalue = agevalue[0]
            
                conn.commit()
                window3 = Tk()
                window3.geometry('1366x768')
                window3.title('Client Info')
                from PIL import Image,ImageTk
                img = Image.open(r'C:/Users/Elambharathi/Downloads/Bharathi/CCC/infopage1.png')
                photo = ImageTk.PhotoImage(img)
                lab1 = Label(image = photo)
                lab1.pack()
                window3.iconbitmap(r"C:/Users/Elambharathi/Downloads/Bharathi/CCC/myicon4.ico")

                namedisplay1 = Label(window3,text ='                                                                          ',bg='white').place(x=625,y=43)
                namedisplay = Label(window3,text =name,bg='white').place(x=625,y=43)

                agedisplay1 = Label(window3,text ='                                                                          ',bg='white').place(x=625,y=83)
                agedisplay = Label(window3,text=agevalue,bg='white').place(x=625,y=83)

                dobdisplay1 = Label(window3,text ='                                                                          ',bg='white').place(x=625,y=123)
                dobdisplay = Label(window3,text =dob,bg='white').place(x=625,y=123)

                genderdisplay1 = Label(window3,text ='                                                                          ',bg='white').place(x=625,y=163)
                genderdisplay = Label(window3,text=gendervalue,bg='white').place(x=625,y=163)

                addressdisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=203)
                addressdisplay = Label(window3,text=addressvalue,bg='white').place(x=625,y=203)

                pindisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=243)
                pindisplay = Label(window3,text=pinvalue,bg='white').place(x=625,y=243)

                emaildisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=283)
                emaildisplay = Label(window3,text=emailvalue,bg='white').place(x=625,y=283)

                phonedisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=323)
                phonedisplay = Label(window3,text=phonevalue,bg='white').place(x=625,y=323)

                lamountdisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=363)
                lamountdisplay = Label(window3,text=lamountvalue,bg='white').place(x=625,y=363)

                linterestdisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=403)
                linterestdisplay = Label(window3,text=linterestvalue,bg='white').place(x=625,y=403)

                minterestdisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=523)
                minterestdisplay = Label(window3,text=minterestvalue,bg='white').place(x=625,y=523)

                termdisplay1 = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=443)
                termdisplay = Label(window3,text=termvalue,bg='white').place(x=625,y=443)

                typedisplay = Label(window3,text ='                                                                           ',bg='white').place(x=625,y=483)
                typedisplay = Label(window3,text=typevalue,bg='white').place(x=625,y=483)

                def screen1():
                    import pyautogui
                    pyautogui.screenshot(r"C:/Users/Elambharathi/Downloads/Bharathi/CCC/"+name+".png")

                def screen2():
                    filename = "C:/Users/Elambharathi/Downloads/Bharathi/CCC/"+name+".txt"
                    fileout = open(filename,"w")

                    fileout.write("Name              :"+name)
                    fileout.write('\n')

                    fileout.write("Age               :"+str(agevalue))
                    fileout.write('\n')

                    fileout.write("DOB               :"+dob)
                    fileout.write('\n')

                    fileout.write("Gender            :"+gendervalue)
                    fileout.write('\n')

                    fileout.write("Address           :"+addressvalue)
                    fileout.write('\n')

                    fileout.write("PIN Code          :"+str(pinvalue))
                    fileout.write('\n')

                    fileout.write("Email             :"+emailvalue)
                    fileout.write('\n')

                    fileout.write("Phone             :"+str(phonevalue))
                    fileout.write('\n')

                    fileout.write("Loan Amount       :"+str(lamountvalue))
                    fileout.write('\n')

                    fileout.write("Loan Interest     :"+str(linterestvalue))
                    fileout.write('\n')

                    fileout.write("Monthly Interest  :"+str(minterestvalue))
                    fileout.write('\n')

                    fileout.write("Loan Term         :"+termvalue)
                    fileout.write('\n')

                    fileout.write("Loan Type         :"+typevalue)
                    fileout.write('\n')

                    fileout.close()

                def what():
                    import webbrowser
                    text1 = "https://wa.me/91"+str(phonevalue)+"?text=Hi "+name+", We are ETS Finance, We would like to inform you that you are due with your payment and we suggest you make it soon"
                    webbrowser.open(text1)
                    

                button_save1  = Button(window3,text='Save as image',font=('Halvetica',10,'bold'),width=12,bg='SeaGreen1',command = screen1).place(x=455,y=580)
                button_save2   = Button(window3,text='Save as note',font=('Halvetica',10,'bold'),width=12,bg='azure2',command = screen2).place(x=605,y=580)
                button_what   = Button(window3,text='Remind client',font=('Halvetica',10,'bold'),width=12,bg='misty rose',command=what).place(x=755,y=580)
                mainloop()
            else:
               messagebox.showerror("Error",'Enter the proper details')
                

        else:
            messagebox.showinfo("Error",'Enter the correct OTP')

    def gettingotp():
        name = name_entered.get()
        name = name.upper()
        dob = dob_entered.get()
        conn = sqlite3.connect("firstdb.db")
        with conn:
            cursor = conn.cursor()
        execute1 = cursor.execute("select Name from FINALE")
        global data1
        data1 = cursor.fetchall()
        execute2 = cursor.execute("select DOB from FINALE")
        global data2
        data2 = cursor.fetchall()
        if (name,) in data1 and (dob,) in data2:
            import random
            global otpval
            otpval = random.randint(100000,999999)
            import smtplib
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("cccetsfinance@gmail.com", "financelogin")
            SUBJECT = 'OTP'
            TEXT = 'Your One Time Password is:'+str(otpval)
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail("cccetsfinance@gmail.com","goodboybharathi@gmail.com", message)
            s.quit()
        else:
            messagebox.showerror("Error",'Enter the proper details')
            

    #Font definitions
    large_font = ('Verdana',15)

    button_otp     = Button(windows,image= photootp,command = gettingotp).place(x=220,y=380)
    button_check     = Button(windows,image= photocheck,command = newcmd).place(x=400,y=380)
    button_quit     = Button(windows,image= photoquit,command = exitclicked).place(x=580,y=380)

    #List of Entry Widgets
    entry_name      = Entry(windows,textvar=name_entered,font=large_font,relief='groove',width=30,bg="linen").place(x=310,y=65)
    entry_dob      = Entry(windows,textvar=dob_entered,font=large_font,relief='groove',width=30,bg="linen").place(x=310,y=115)
    entry_otp      = Entry(windows,textvar=otp_entered,font=large_font,relief='groove',width=30,bg="linen").place(x=310,y=165)
    windows.mainloop()

menu = Menu(windowh)
windowh.config(menu=menu)
subm1 = Menu(menu)
subm2 = Menu(menu)
subm3 = Menu(menu)
menu.add_cascade(label='Menu',menu=subm1)
menu.add_cascade(label='Info',menu=subm3)
menu.add_cascade(label='Quit',menu=subm2)
subm3.add_command(label='About',command=ourinfo)
subm3.add_command(label='Copyrights',command=copyinfo)
subm1.add_command(label='Loan Form',command=loanform)
subm1.add_command(label='Loan Status',command=loanstatus)
subm2.add_command(label='Quit',command=quiting)
windowh.mainloop()
