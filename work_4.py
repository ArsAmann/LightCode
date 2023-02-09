
import tkinter as tk 
import pytube 
from tkinter import messagebox 






win = tk.Tk()

win.minsize(300, 300)
win.resizable(False, False)
win.title('YouTube video saver')


try:
    def main():
        global link, link2 
        lab = tk.Label(win, text='Ссылка для скачивание:', font='Times 14')
        lab.grid(row=4, column=0, columnspan=4)
        link = tk.Entry(win, width=50, bd=5)
        link.grid(row=5, column=0, columnspan=4)

        lab2 = tk.Label(win, text='Путь сохранение:', font='Times 14')
        lab2.grid(row=6, column=0, columnspan=4)
        link2 = tk.Entry(win, width=50, bd=5)
        link2.grid(row=7, column=0, columnspan=4)

    def download():
        video = pytube.YouTube(link.get())
        quality = video.streams.get_highest_resolution()
        quality.download(link2.get())
        with open('file.txt', 'a') as file:
            file = file.writelines(str({'link': link.get(), 'path':link2.get()}))

    down = tk.Button(win, text='Скачать', command=download, width=8, height=4, bg='red', fg='black')
    down.grid(row=8, column=0,  columnspan=4)


except:
    messagebox.showinfo('Error', 'Проверьте корректность введенных данных!')








main()
win.mainloop()

