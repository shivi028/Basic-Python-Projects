from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=965ed11065ab651bb839dfd0c61d37d5').json()
    w_label_2.config(text = data['weather'][0]['main'])
    wd_label_2.config(text = data['weather'][0]['description'])
    wt_label_2.config(text = str(int(data['main']['temp'] - 273.15)))
    wp_label_2.config(text= data['main']['pressure'])

win = Tk()

win.title('Weaher\'s Update')
win.config(bg = 'gray')
win.geometry('500x500')

name_label = Label(win, text='Global Weather App', font=('Time New Roman', 30, 'bold'), bg='pink')
name_label.place(x = 25, y = 25, height = 50, width = 450)

city_name = StringVar()
List_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text='Global Weather App', values=List_name, font=('Time New Roman', 15, 'bold'), textvar=city_name)
com.place(x = 25, y = 90, height = 40, width = 450)


w_label = Label(win, text='Weather Climate', font=('Time New Roman', 15, 'bold'), bg='pink')
w_label.place(x = 25, y = 240, height = 50, width = 210)
w_label_2 = Label(win, text='', font=('Time New Roman', 15, 'bold'))
w_label_2.place(x = 250, y = 240, height = 50, width = 210)


wd_label = Label(win, text='Weather Description', font=('Time New Roman', 15, 'bold'), bg='pink')
wd_label.place(x = 25, y = 300, height = 50, width = 210)
wd_label_2 = Label(win, text='', font=('Time New Roman', 15, 'bold'))
wd_label_2.place(x = 250, y = 300, height = 50, width = 210)


wt_label = Label(win, text='Temperature', font=('Time New Roman', 15, 'bold'), bg='pink')
wt_label.place(x = 25, y = 360, height = 50, width = 210)
wt_label_2 = Label(win, text='', font=('Time New Roman', 15, 'bold'))
wt_label_2.place(x = 250, y = 360, height = 50, width = 210)


wp_label = Label(win, text='Pressure', font=('Time New Roman', 15, 'bold'), bg='pink')
wp_label.place(x = 25, y = 420, height = 50, width = 210)
wp_label_2 = Label(win, text='', font=('Time New Roman', 15, 'bold'))
wp_label_2.place(x = 250, y = 420, height = 50, width = 210)

done_btn = Button(win, text='DONE', font=('Time New Roman', 15, 'bold'), command=data_get)
done_btn.place(y = 150, height = 50, width = 100, x = 200)


win.mainloop()