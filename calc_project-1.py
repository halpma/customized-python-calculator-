# O W Holmes 
# 22/09/2022
#########################################################
# Python Calculator For A Young Age Group (5-7 Years Old)
#########################################################
 

from tkinter import * # import the tkinter libary 

def button_press(num):    # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():       # the equals sing
    global equation_text    
    
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:        # If calculation dosent make sense or dosent work

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("Arithmetic Error")

        equation_text = ""

def clear():             # The clear button clears the sum on the display
    global equation_text 

    equation_label.set("")

    equation_text = ""


# Desinging the user interface

window = Tk()
window.title("Python Calculator")
window.geometry("500x625")
window.configure(bg="#ffda00")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="dark grey", width=24, height=2)
label.pack()

#############################################################################################################
# All of the numbers
#############################################################################################################

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width =9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width =9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width =9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width =9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width =9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width =9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width =9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width =9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width =9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width =9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=1)

# create operation buttons

plus = Button(frame, text='PLUS', height=4, width =9, font=35, command=lambda: button_press('+'))
plus.grid(row=3, column=2)

# create equal button

equal = Button(frame, text='EQUALS', height=4, width =9, font=35, command=equals)
equal.grid(row=3, column=0)

# create clear button

clear = Button(window, text='New Sum', height=4, width =12, font=35, command=clear)
clear.pack()



window.mainloop()
