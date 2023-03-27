import tkinter

window = tkinter.Tk()

window.title("GUI program by wkddusghks")
window.geometry("640x400+100+100")
window.resizable(False, False)

def btnClick():
    label.config(font=("Arial", 40))
    label.config(text = "안산공업고등학교 컴퓨터과")
    label.config(fg = "blue")
    
label = tkinter.Label(window, text = "안산공업고등학교")
label.pack()

button = tkinter.Button(window, text = "확인", command = btnClick)
button.pack()
window.mainloop()
