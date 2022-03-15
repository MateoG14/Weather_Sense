from pydoc import describe
import tkinter as tk
from tkinter import font
import requests
from turtle import left

HEIGHT = 800
WIDTH = 900

def test_function(entry):
    print("This is a new entry:", entry)

    # api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
    # 6a7d95f1facf8c561df9ac493d7e337c

def formant_response(weather):
    print(weather)
    try:
       name =  (weather['name'])
       desc=  (weather['weather'][0]['description'])
       temp = (weather['main']['temp'])

       last_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc,temp )
    except:
       last_str = 'There is a problem in retriving that information'

    return last_str

def get_weather(city):
     weather_key = '6a7d95f1facf8c561df9ac493d7e337c'
     url = 'http://api.openweathermap.org/data/2.5/weather'
     params= {'APPID' : weather_key,'q': city, 'units': 'imperial' }
     response = requests.get(url, params=params)
     weather = response.json()
     
     label ['text'] = formant_response(weather)
  

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH )
canvas.pack()

background_image = tk.PhotoImage(file= 'weather.png')
background_label =tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


frame= tk.Frame(root, bg='#ffcc00', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry= tk.Entry(frame, font=30)
entry.place( relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font= '30', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth= 0.3,)

lower_frame = tk.Frame(root, bg= '#ffcc00', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight= 0.6, anchor= 'n')

label = tk.Label(lower_frame, font = ('MS Serif', 18))
label.place( relwidth=1, relheight=1)


root.mainloop()
