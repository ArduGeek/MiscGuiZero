from guizero import *

def add_1():
	display_box.value += "1"
def add_2():
	display_box.value += "2"
def add_3():
	display_box.value += "3"
def add_4():
	display_box.value += "4"
def add_5():
	display_box.value += "5"
def add_6():
	display_box.value += "6"
def add_7():
	display_box.value += "7"
def add_8():
	display_box.value += "8"
def add_9():
	display_box.value += "9"
def add_0():
	display_box.value += "0"
def plus():
	display_box.value += "+"
def minus():
	display_box.value += "-"
def reset():
	display_box.value = ""
def result():
	wynik = 0
	stos = []
	for i in display_box.value:
		stos.append(i)
	for i in range(0,len(stos)):
		if(stos[i] == "+"):
			a = int(stos[i-1])
			b = int(stos[i-2])
			stos[i-1] = "0"
			stos[i-2] = "0"
			wynik = a+b
			stos[i] = str(wynik)
		elif(stos[i] == "-"):
			a = int(stos[i-1])
			b = int(stos[i-2])
			stos[i-1] = "0"
			stos[i-2] = "0"
			wynik = b-a
			stos[i] = str(wynik)
		else:
			continue
	pos = len(stos)
	display_box.value = str(stos[pos-1])
			
app = App(title="Kalkulator wersja ONP",height=500,width=500,bg="white")
app.text_size = 20
show_box = Box(app, align="top", width="fill", height="fill")
ButtonEq = PushButton(show_box, text="=", align="right" , width="fill" , height="fill",command=result)
ButtonReset = PushButton(show_box, text="RESET", align="right" , width="fill" , height="fill",command=reset)
display_box = TextBox(show_box, align="left", width="fill", height="fill")
console_box = Box(app, width="fill", height="fill")
Button1 = PushButton(console_box,text="1",align="left" ,width="fill", height="fill",command=add_1)
Button2 = PushButton(console_box,text="2",align="left" ,width="fill", height="fill",command=add_2)
Button3 = PushButton(console_box,text="3",align="left" ,width="fill", height="fill",command=add_3)
console_box2 = Box(app, width="fill", height="fill")
Button4 = PushButton(console_box2,text="4",align="left" ,width="fill", height="fill",command=add_4)
Button5 = PushButton(console_box2,text="5",align="left" ,width="fill", height="fill",command=add_5)
Button6 = PushButton(console_box2,text="6",align="left" ,width="fill", height="fill",command=add_6)
console_box3 = Box(app, width="fill" , height="fill")
Button7 = PushButton(console_box3,text="7",align="left", width="fill", height="fill",command=add_7)
Button8 = PushButton(console_box3,text="8",align="left" ,width="fill", height="fill",command=add_8)
Button9 = PushButton(console_box3,text="9",align="left" ,width="fill", height="fill",command=add_9)
console_box4 = Box(app, width="fill", height="fill")
Button_Plus = PushButton(console_box4,text="+", align="left" ,width="fill", height="fill",command=plus)
Button0 = PushButton(console_box4,text="0",align="left" ,width="fill", height="fill",command=add_0)
Button_Minus = PushButton(console_box4,text="-", align="left", width="fill", height="fill",command=minus) 
app.display()
