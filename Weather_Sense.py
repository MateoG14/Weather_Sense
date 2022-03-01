import tkinter as tk
from turtle import left

HEIGHT = 800
WIDTH = 900

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

button = tk.Button(frame, text="Test Button", font= '30',)
button.place(relx=0.7, relheight=1, relwidth= 0.3,)

lower_frame = tk.Frame(root, bg= '#ffcc00', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight= 0.6, anchor= 'n')

label = tk.Label(lower_frame)
label.place( relwidth=1, relheight=1)

root.mainloop()
