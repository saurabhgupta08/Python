from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Website Blocker")

Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack()
Label(root, text='Saurabh & Suresh', font='arial 20 bold').pack(side=BOTTOM)

host_path = r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root, text='Enter Website(s):', font='arial 13 bold').place(x=5, y=60)
Websites = Entry(root, font='arial 10', width='40')
Websites.place(x=150, y=60)

def Blocker():
    website_lists = Websites.get().split()
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in website_lists:
            if website in file_content:
                Label(root, text=f'{website} is Already Blocked', font='arial 12 bold').place(x=200, y=200)
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text=f'{website} Blocked', font='arial 12 bold').place(x=230, y=200)

block_btn = Button(root, text='BLOCK', font='arial 12 bold', command=Blocker, width=6, bg='royal blue1', activebackground='sky blue')
block_btn.place(x=230, y=150)

root.mainloop()