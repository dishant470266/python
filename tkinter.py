import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')

#create labels
name_label = ttk.Label(win,text='Enter your name :').grid(row=0,column=0)
name_label.grid(row=0,column=0, sticky=tk.W)

email_label = ttk.Label(win,text='Enter your email : ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label = ttk.Label(win,text='Enter your age : ')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text='Select your gender  : ')
gender_label.grid(row=3,column=0,sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable= name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()


email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable= name_var)
email_entrybox.grid(row=1,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable= name_var)
age_entrybox.grid(row=2,column=1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=14, textvariable=gender_var,state='readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#radio button
#studnt ,teacher
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student', value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn1 = ttk.Radiobutton(win,text='Teacher', value='Teacher',variable=usertype)
radiobtn1.grid(row=4,column=0)

#check button
checkbtn = ttk.Checkbutton(win,text='check if you want to newslettrs0',variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

#create button
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f'{username} is {userage} years old, {user_email}')
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    print(user_gender,user_type,subscribed)

    with open('file.txt' , 'a') as f:
        f.write(f'{username},{userage},{user_email},{user_gender},{subscribed}\n')
    
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#b388ff')

    submit_button.configure(foreground='Blue')

# write to csv files
def action(): 
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    user_type = usertype.get()
    user_gender = gender_var.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    
    # write to csv file
    with open('file.csv','a') as f:
        dict_writer = DictWriter(f,fieldnames=['UserName','User Email Address','User Age','User Gender','User type','Subcribed'])
        if os.stat('file.csv').st_size==0:
        dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName' : username,
            'User Email Address' : user_email,
            'User Age' : userage,
            'user Gender' : user_gender,
            'User Type' : user_type,
            'Subscribed' : subscribed
        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#b388ff')

submit_button = ttk.Button(win,text='Submit', command=action)
submit_button.grid(row=6,column=0)




#pack,grid
win = mainloop()