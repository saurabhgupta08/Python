from tkinter import *

root = Tk()
root.geometry('600x600')
root.resizable(0, 0)
root.title("Website Blocker")

Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack()
Label(root, text='Saurabh & Suresh', font='arial 20 bold').pack(side=BOTTOM)

host_path = r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

blocked_websites = []

Label(root, text='Enter Website(s):', font='arial 13 bold').place(x=5, y=60)
Websites = Entry(root, font='arial 10', width='40')
Websites.place(x=150, y=60)

listbox = Listbox(root, font='arial 10', width='40', height='10')
listbox.place(x=150, y=200)

def update_listbox():
    listbox.delete(0, END)
    for website in blocked_websites:
        listbox.insert(END, website)

def Blocker():
    website_lists = Websites.get().split()
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in website_lists:
            if website in file_content:
                Label(root, text=f'{website} is Already Blocked', font='arial 12 bold').place(x=300, y=150)
            else:
                host_file.write(ip_address + " " + website + '\n')
                blocked_websites.append(website)
                Label(root, text=f'{website} Blocked', font='arial 12 bold').place(x=300, y=150)
                update_listbox()

def Unblocker():
    website_lists = Websites.get().split()
    with open(host_path, 'r') as host_file:
        lines = host_file.readlines()
    with open(host_path, 'w') as host_file:
        for line in lines:
            if not any(website in line for website in website_lists):
                host_file.write(line)
        for website in website_lists:
            if website in blocked_websites:
                blocked_websites.remove(website)
    Label(root, text=f'{website} Unblocked', font='arial 12 bold').place(x=300, y=150)
    update_listbox()

block_btn = Button(root, text='BLOCK', font='arial 12 bold', command=Blocker, width=6, bg='royal blue1', activebackground='sky blue')
block_btn.place(x=100, y=150)

unblock_btn = Button(root, text='UNBLOCK', font='arial 12 bold', command=Unblocker, width=8, bg='red', activebackground='orange')
unblock_btn.place(x=200, y=150)

root.mainloop()
