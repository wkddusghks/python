import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("BMI 계산기")
window.geometry("640x400+300+300")
window.resizable(False, False)

he = tkinter.StringVar()
we = tkinter.StringVar()

def btn_click() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = w_value / (h_value * h_value)
    tkinter.messagebox.showinfo("결과", result)

label = tkinter.Label(window, text = "BMI 계산기")
label.config(font = ("Arial", 25))
label.config(fg = "red")
label.pack()

heightlabel = tkinter.Label(window, text = "신장")
heightlabel.config(font = ("Arial", 24))
heightlabel.place(x = 30, y = 70)

weightlabel = tkinter.Label(window, text = "체중")
weightlabel.config(font = ("Arial", 24))
weightlabel.place(x = 30, y = 140)

heightEntry = tkinter.Entry(window, textvariable = he)
heightEntry.place(x = 110, y = 82)

weightEntry = tkinter.Entry(window, textvariable = we)
weightEntry.place(x = 110, y = 152)

btn = tkinter.Button(window, text = "확인", command = btn_click)
btn.place(x = 30, y = 250)

window.mainloop



