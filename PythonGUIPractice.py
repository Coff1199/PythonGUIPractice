import customtkinter
import os.path

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

root=customtkinter.CTk()
root.geometry('1200x900')
root.title('Login Test')

def login():
    print('Test')

    login_button.configure(state='disabled')

    username=username_entry.get()
    password=password_entry.get()

    if rem_checkbox.get()==1:
        with open('User_Login.txt','w') as file:
            file.write(username+'\t'+password)

    label.pack_forget()
    username_entry.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    rem_checkbox.pack_forget()

    print(username,password)

    label2 =customtkinter.CTkLabel(master=frame,text=f'Welcome {username}',font=('Arial',70))
    label2.pack(pady=44,padx=40)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=80,padx=120, fill='both',expand=True)

label = customtkinter.CTkLabel(master=frame,text='Login',font=('Arial',50))
label.pack(pady=44,padx=40)

username_entry = customtkinter.CTkEntry(master=frame,placeholder_text='Username',width=200,height=50)
username_entry.pack(pady=44, padx=40)

password_entry = customtkinter.CTkEntry(master=frame,placeholder_text='Password',show='*',width=200,height=50)
password_entry.pack(pady=44, padx=40)

if os.path.exists('User_Login.txt') and os.stat("User_Login.txt").st_size != 0:
    with open('User_Login.txt','r') as file:
        txt=file.read().split('\t')
    username_entry.insert(0,txt[0])
    password_entry.insert(0,txt[1])

login_button = customtkinter.CTkButton(master=frame,text='Login',command=login,width=200,height=50)
login_button.pack(pady=44,padx=40)

rem_checkbox=customtkinter.CTkCheckBox(master=frame, text='Remember me?',width=100,height=25)
rem_checkbox.pack(pady=44,padx=40)

root.mainloop()
