from tkinter import *

window = Tk()
window.geometry('350x650')
window.title("Clicker")
window.config(bg='palegoldenrod')
clicks = 0

def check():
    global clicks
    clicks += 1
    reloadCounter()

def reloadCounter():
    checkClicks.config(text=f'Score: {clicks}')

def reset():
    global clicks
    clicks = 0
    reloadCounter()

logo = Label(text='Clicker', bg='darksalmon',font=('Montserrat', '20'), foreground='bisque')
checkClicks = Label(text=f'Score: {clicks}', font=('Arial', '14', 'bold'), bg='palegoldenrod', foreground='black')

click = Button(text='Click Here', font=('Montserrat', '10'), activebackground='deepskyblue', foreground='white', bg='crimson', command=check)

resetClick = Button(text='Reset Score', font=('Montserrat', '14'), activebackground='deepskyblue', foreground='white', bg='crimson', command=reset)

window.resizable(False, False)
logo.place(relx=0.3785, rely=0.1)
checkClicks.place(relx=0.39, rely=0.45)
click.place(relx=0.41, rely=0.75)
resetClick.place(relx=0.34, rely=0.575)
window.mainloop()