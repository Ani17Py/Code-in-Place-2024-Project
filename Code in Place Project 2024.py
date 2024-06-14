from bs4 import BeautifulSoup
import re
import requests
import tkinter
from tkinter import *


gui = tkinter.Tk()
gui.title('Price History Retriever')
gui.geometry('300x350')
gui.configure(bg='grey')
lb1 = Label(gui, text='Paste product URL from: "https://pricehistory.app/"', fg='black', bg='green')
lb1.place(x=10, y=0)
ur_lb1 = Label(gui, text='Paste the URL here ', fg='black', bg='green')
ur_lb1.place(x=90, y=40)
url = ''
pasted_url = Entry(gui)
pasted_url.place(x=10, y=80, width=280)
hum = []
lb2 = Label(gui, text='', fg='black', bg='DarkOrchid4')
lb3 = Label(gui, text='', fg='black', bg='steel blue')
lb4 = Label(gui, text='', fg='black', bg='OrangeRed3')
lb5 = Label(gui, text='', fg='black', bg='HotPink3')
lb6 = Label(gui, text='', fg='black', bg='OrangeRed3')


def fetched():
    btn1.configure(text='Fetched!', fg='black', bg='DarkGoldenrod1')


def fetch(url):
    ur_eq = requests.get(url)
    return ur_eq.text


def find_price():
    W_url = pasted_url.get()
    paper_data = fetch(W_url)
    page_str = str(BeautifulSoup(paper_data, 'html.parser'))
    lest = str(re.search(r'Lowest Price: ', page_str))
    n1 = lest.find('(')
    n2 = lest.find(',')
    finn3 = int(lest[n1+1:n2])
    rough = page_str[finn3:finn3+150]
    clean_up = rough.find('"')
    n = clean_up-1
    final = rough[0:n]
    lister = list(final.split())
    print(final)
    while True:
        for char in final:
            if char == ':':
                n1 = final.index(char)
                if '|' in final:
                    n2 = final.find('|')
                    var = final[n1 + 1:n2 - 1].lstrip(' ')
                    hum.append(var) if len(var) < 12 else hum.append(var[0:12])
                    fine = final.replace(final[0:n2 + 2], '')
                    final = fine
                    fine = ''
                else:
                    n3 = final.find('₹')
                    hum.append(final[n3:].lstrip(' '))
        lb2.configure(text=hum[0])
        lb3.configure(text=hum[1])
        lb4.configure(text=hum[2])
        lb5.configure(text=hum[3])
        lb6.configure(text=hum[4])
        break


btn1 = Button(gui, text='Fetch', fg='black', bg='bisque3', command=fetched)
btn1.place(x=115, y=120, width=50)
btn2 = Button(gui, text='Lowest Price', fg='black', bg='DarkOrchid4', command=find_price)
btn3 = Button(gui, text='Average Price', fg='black', bg='steel blue', command=find_price)
btn4 = Button(gui, text='Highest Price', fg='black', bg='OrangeRed3', command=find_price)
btn5 = Button(gui, text='MRP', fg='black', bg='HotPink3', command=find_price)
btn6 = Button(gui, text='Current Price', fg='black', bg='OrangeRed3', command=find_price)
btn2.place(x=20, y=160, width=82)
btn3.place(x=20, y=200, width=82)
btn4.place(x=20, y=240, width=82)
btn5.place(x=20, y=280, width=82)
btn6.place(x=20, y=320, width=82)
lb2.place(x=200, y=160, width=82, height=25)
lb3.place(x=200, y=200, width=82, height=25)
lb4.place(x=200, y=240, width=82, height=25)
lb5.place(x=200, y=280, width=82, height=25)
lb6.place(x=200, y=320, width=82, height=25)














gui.mainloop()


