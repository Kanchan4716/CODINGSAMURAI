from tkinter import *
from tkinter import Tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import requests

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getweather():
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")    
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06497c2598107663f54e68bc75fb1110"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp_celsius = int(json_data['main']['temp'] - 273.15)
        temp_fahrenheit = int(temp_celsius * 9/5 + 32)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        if temp_unit.get() == "Celsius":
            temperature = f"{temp_celsius}°C"
        else:
            temperature = f"{temp_fahrenheit}°F"
    
        t.config(text=(temperature,"°"))
        c.config(text=(condition,"|","FEELS","LIKES",temperature,"°"))
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)


    except Exception as e:
      messagebox.showerror("Weather App","Invalid Entry!!")
      

search_image = PhotoImage(file="C:/Users/Dell/Downloads/search.png-removebg-preview.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)  # Adjust padx and pady as needed

text_field = Entry(root, justify='center', width=17, font=("poppins", 25, "bold"), bg="black", border=0, fg="white")
text_field.place(x=60, y=40)  # Place the Entry widget in the same row as the image
text_field.focus()

search_icon = PhotoImage(file="C:/Users/Dell/Downloads/imgonline-com-ua-resize-PdRCmpyuSh3gxHm.png")
my_image_icon = Button(image=search_icon, borderwidth=0,cursor="hand2", height=40, width=60,background="black",command=getweather)
my_image_icon.place(x=400, y=38)  # Adjust the x and y coordinates as needed

logo_image = PhotoImage(file="C:/Users/Dell/Downloads/download (3).png")
logo = Label(image=logo_image)
logo.place(x=170, y=116)

Frame_image = PhotoImage(file="C:/Users/Dell/Downloads/imgonline-com-ua-resize-W6KaSrRlNZrqLgU.png")
Frame_my_image = Label(image=Frame_image)
Frame_my_image.pack(padx=5,pady=5,side=BOTTOM)

temp_unit = StringVar()
temp_unit.set("Celsius")  # Default selection

celsius_radio = Radiobutton(root, text="Celsius", font=("Algerian",15,'bold'),variable=temp_unit, value="Celsius")
celsius_radio.place(x=500, y=41)

fahrenheit_radio = Radiobutton(root, text="Fahrenheit",font=("Algerian",15,'bold'), variable=temp_unit, value="Fahrenheit")
fahrenheit_radio.place(x=650, y=41)

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

label1=Label(root,text="WIND",font=("Helvetica",17,'bold'),fg="white",bg="#ffd700")
label1.place(x=140,y=380)

label2=Label(root,text="HUMIDITY",font=("Helvetica",17,'bold'),fg="white",bg="#ffd700")
label2.place(x=260,y=380)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",17,'bold'),fg="white",bg="#ffd700")
label3.place(x=440,y=380)

label4=Label(root,text="PRESSURE",font=("Helvetica",17,'bold'),fg="white",bg="#ffd700")
label4.place(x=650,y=380)

t=Label(font=("algerian",50,"bold"),fg="#ee666d")
t.place(x=400,y=142)

c=Label(font=("algerian",27,"bold"))
c.place(x=400,y=220)

w=Label(text="...",font=("arial",20,"bold"),bg="#ffd700")
w.place(x=141,y=415)

h=Label(text="...",font=("arial",20,"bold"),bg="#ffd700")
h.place(x=285,y=415)

d=Label(text="...",font=("arial",20,"bold"),bg="#ffd700")
d.place(x=450,y=415)

p=Label(text="...",font=("arial",20,"bold"),bg="#ffd700")
p.place(x=670,y=415)

root.mainloop()