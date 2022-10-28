import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube

def start():
    window = tk.Tk()
    window.geometry('500x300')
    window.resizable = (0,0)
    window.title('Загрузка видео с YouTube')
    header = tk.Label(window, text='Загрузка видео с YouTube', font='tahoma 20 bold')
    header.place(x=70, y=10)
    enter_name = tk.Label(window, text='Введите ссылку для скачивания: ', font='tahoma 15 bold')
    enter_name.place(x=70, y=45)
    link = tk.StringVar()
    link_enter = tk.Entry(window, width = 70, textvariable = link)
    link_enter.place(x=70, y=90)
       
    def download():
        path_to_save = askdirectory()
        url = YouTube(str(link.get()))
        filters = url.streams.get_by_itag('18')
        video = url.streams.first()
        filters.download(output_path=path_to_save)
        downloader = tk.Label(window, text='Скачиваю...', font='tahoma 15 bold')
        downloader.place(x = 100, y = 180)
        messagebox.showinfo("SUCCESSFULLY", "Загружено в папку "  + path_to_save)
        
    button = tk.Button(window, text='Скачать', font='tahoma 15 bold', command=download)
    button.place(x=100, y=125)
    window.mainloop()