import datetime
import tkinter as tk

def update_time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_date = datetime.datetime.now().strftime('%B %d, %Y')  
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title('Digital Clock')
root.configure(bg='black')

font_family = 'Roboto'
time_font_size = 80
date_font_size = 30

time_font = (font_family, time_font_size, 'bold')
date_font = (font_family, date_font_size)

time_label = tk.Label(root, font=time_font, bg='black', fg='white')
time_label.pack(pady=50)

date_label = tk.Label(root, font=date_font, bg='black', fg='white')
date_label.pack()

update_time()
root.mainloop()
