# Depveloper : Rahul Dhar
# This is a Massage Encript and Decript tool based on base64.
# import Tkinter
from tkinter import StringVar, Frame, Label, Entry, Button, BOTTOM, LEFT, TOP, RIGHT, Tk, SUNKEN, X, Y

# import modules
import base64
import time

#--------------WINDOW--------------------
root = Tk()

root.title("hide me !")
root.geometry("1200x700")
root.resizable(True, True)




#=====================================================================================================
#--------------------                       VARIABLES                       -----------------------------
#=====================================================================================================

Messege = StringVar() 
key = StringVar() 
Result = StringVar()
global end
end = ""

#=====================================================================================================
#--------------------                       FUNCTIONS                        -----------------------------
#=====================================================================================================

#-----------------Encode------------------
def encode(key, msg):
	enc = []
	lblEncript.configure(text = "Messege is Encripted !", fg = "blue")

	for i in range(len(msg)):
		key_c = key[i % len(key)]
		enc_c = chr(ord(msg[i]) + ord(key_c))

		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#-----------------Decode---------------------
def decode(key, enc): 
	dec = [] 
	lblEncript.configure(text = "Messege is Decripted !", fg = "blue")

	enc = base64.urlsafe_b64decode(enc).decode() 
	for i in range(len(enc)): 
		key_c = key[i % len(key)] 
		dec_c = chr(ord(enc[i]) - ord(key_c)) 
							
		dec.append(dec_c) 

	return "".join(dec)

#-------------- Function for call --------------
def func(Event = None): 
	print("Message= ", (Messege.get())) 
	global end
	error_correct()

	#------------ if all ok then run the program -----------
	if ((end != "") and (Messege.get() != "") and (key.get() != "")):
		message = Messege.get() 
		k = key.get()  
		e = end
		
		if (e == 'e'): 
			Result.set(encode(k, message)) 
		else: 
			Result.set(decode(k, message))

	#------------- if any error show error messege -----------
	else:
		if(Messege.get() == ""):
			lblMsgInfo.configure(text = "Messege is empty", fg = "red")

		elif(key.get() == ""):
			lblKeyInfo.configure(text = "Enter a Key", fg = "red")

		elif(end == ""):
			lblEncode_DecodeInfo.configure(text = "Please select mode", fg = "red")

def btnEncode(Event = None):
    global end
    end = 'e'
    btnEncoder.configure(bg = 'green')
    btnDecoder.configure(bg = 'powder blue')

def btnDecode(Event = None):
    global end
    end = 'd'
    btnDecoder.configure(bg = 'green')
    btnEncoder.configure(bg = 'powder blue')


#-------------- reset window ------------------
def Reset(Event = None):  
	global end
	Messege.set("") 
	key.set("") 
	Result.set("") 
	btnDecoder.configure(bg = 'powder blue') 
	btnEncoder.configure(bg = 'powder blue')
	end = ""
	lblEncript.configure(text = "Output :-", fg = "Black")
	error_correct()


#-------------- Copy Function --------------	
def copy(Event = None):
	root.clipboard_clear()
	root.clipboard_append(Result.get())


#---------------ERROR CORRECTION--------------
def error_correct():
	lblEncode_DecodeInfo.configure(text = "Select EnCode or DeCode Mode", fg = "black")
	lblMsgInfo.configure(text = "Input Your Messege", fg = "black")
	lblKeyInfo.configure(text = "Input a Key", fg = "black")


#------------- exit function ----------------------
def quit(Event = None): 
	root.destroy() 



#=====================================================================================================
#--------------------                GRAPHICAL USER INTERFACE                -----------------------
#=====================================================================================================



#--------------------  Frames  -----------------------------

top = Frame(root, width = 1200, relief = SUNKEN)
top.pack(side = TOP, fill = X)

mode = Frame(root, width = 800, relief = SUNKEN)
mode.pack(side = TOP)

body = Frame(root, width = 800, relief = SUNKEN)
body.pack(side = TOP)

shrtcut = Frame(root,bg = "black", relief = SUNKEN)
shrtcut.pack(side = LEFT, padx = 10)

about = Frame(root,bg = "black", relief = SUNKEN)
about.pack(side = RIGHT, padx = 10)

foot = Frame(root, width = 800, relief = SUNKEN)
foot.pack(side = TOP)


#======================== Top Frame ========================

time = time.asctime(time.localtime(time.time()))

info = Label(top, text = "hide ME !", font = ('helvetica', 40, 'bold'), fg = "White",bg = "Black")
info.pack(fill = X)

info = Label(top, font=('arial', 15, 'bold'), text = time, fg = "yellow", bg = 'Black')
info.pack(fill = X, side = BOTTOM)


#++++++++++++++++++++++++++++++ FIELDS (Label, Entry) ++++++++++++++++++++++

#======================== Body Frame ========================

#--------------------Messege---------------------
lblMsg = Label(body, font = ('arial', 12, 'bold'), 
		text = "MESSAGE :-", bd = 12, anchor = "w") 
		
lblMsg.place(x = 20 , y =18)

txtMsg = Entry(body, font = ('arial', 12, 'bold'), 
		textvariable = Messege, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'left', width = 50) 
				
txtMsg.grid(row = 1, column = 0, padx = 30, pady = 50) 

lblMsgInfo = Label(body, font = ('arial'), 
		text = "Input Your Messege", anchor = "w") 
		
lblMsgInfo.place(x = 200 , y = 95)

# --------------------------key--------------------
lblkey = Label(body, font = ('arial', 12, 'bold'), 
			text = "KEY :-", bd = 12,anchor = "e") 
			
lblkey.place(x = 530 , y =18)

txtkey = Entry(body, font = ('arial', 12, 'bold'), 
		textvariable = key, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right', width = 15) 
				
txtkey.grid(row = 1, column = 1)

lblKeyInfo = Label(body, font = ('arial'), 
		text = "Input a Key", anchor = "w") 
		
lblKeyInfo.place(x = 550 , y = 95)

# -----------------------Result-------------------------
lblEncript = Label(body, font = ('arial', 12, 'bold'), 
			text = "Output :-", bd = 12, anchor = "w") 
			
lblEncript.place(x = 20 , y = 225)

txtEncript = Entry(body, font = ('arial', 12, 'bold'), 
			textvariable = Result, bd = 10, insertwidth = 4, 
					 justify = 'right', width = 50, state="readonly", readonlybackground = "powder blue") 
						
txtEncript.grid(row = 6,column = 0, padx = 30, pady = 50) 
#======================== mode Frame ========================

# Encode/ Decode Label
lblEncode_DecodeInfo = Label(mode, font = ('arial'), 
		text = "Select EnCode or DeCode Mode", anchor = "w") 
		
lblEncode_DecodeInfo.pack()

#======================= About ==========================

lbl1 = Label(shrtcut, text = "Encode --> ctrl+e,", bg = "black", fg = "white", font = ("arial", 12))
lbl1.pack()

lbl2 = Label(shrtcut, text = "     Decode --> ctrl+d,     ", bg = "black", fg = "white", font = ("arial", 12))
lbl2.pack()

lbl7 = Label(shrtcut, text = "Show --> Enter", bg = "black", fg = "white", font = ("arial", 12))
lbl7.pack()

lbl3 = Label(shrtcut, text = "Copy --> alt+c,", bg = "black", fg = "white", font = ("arial", 12))
lbl3.pack()

lbl4 = Label(shrtcut, text = "Reset --> ctrl+r,", bg = "black", fg = "white", font = ("arial", 12))
lbl4.pack()

lbl5 = Label(about, text = "Developer --> Rahul Dhar", bg = "black", fg = "yellow", font = ("arial", 12))
lbl5.pack()

lbl6 = Label(about, text = "Developed in --> python 3.6", bg = "black", fg = "yellow", font = ("arial", 12))
lbl6.pack()

#++++++++++++++++++++++++++++ BUTTONS ++++++++++++++++++++++++++

#======================== mode Frame ========================

# Encode Button
btnEncoder = Button(mode, padx = 12, pady = 5, bd = 14, fg = "black", 
						font = ('arial', 14, 'bold'), width = 10, 
					text = "EnCode", bg = "powder blue", 
						command = btnEncode)
btnEncoder.pack(side = LEFT, padx = 30)

# Decode Button
btnDecoder = Button(mode, padx = 12, pady = 5, bd = 14, fg = "black", 
						font = ('arial', 14, 'bold'), width = 10, 
					text = "DeCode", bg = "powder blue", 
						command = btnDecode)
btnDecoder.pack(side = LEFT, padx = 30)

#======================== body Frame ========================

# Show message button 
Show = Button(body, padx = 12, pady = 8, bd = 14, fg = "black", 
						font = ('arial', 14, 'bold'), width = 10, 
					text = "Show Message", bg = "powder blue", 
						command = func)
Show.grid(row = 4, columnspan = 2)

btnCopy = Button(body, bd = 10, fg = "black", 
						font = ('arial bold', 10, 'bold'), width = 15, 
					text = "Copy", bg = "powder blue", 
						command = copy)
btnCopy.grid(row = 6,column = 1)

#======================== foot Frame ========================

# Reset button 
btnReset = Button(foot, padx = 12, pady = 8, bd = 14, 
				fg = "black", font = ('arial', 14, 'bold'), 
					width = 10, text = "Reset", bg = "blue", 
				command = Reset) 
btnReset.pack(side = LEFT, padx = 30)

# Exit button 
btnExit = Button(foot, padx = 12, pady = 8, bd = 14, 
				fg = "black", font = ('arial', 14, 'bold'), 
					width = 10, text = "Exit", bg = "red", 
				command = quit)
btnExit.pack(side = RIGHT, padx = 30)


#======================= Key Binding ========================

# Show Button
root.bind("<Return>", func)

# Encode
root.bind("<Control - e>", btnEncode)
root.bind("<Control - E>", btnEncode)

# Decode
root.bind("<Control - d>", btnDecode)
root.bind("<Control - D>", btnDecode)

# Reset
root.bind("<Control - r>", Reset)
root.bind("<Control - R>", Reset)

# Direct copy
root.bind("<Alt - c>", copy)
root.bind("<Alt - C>", copy)


# End of GUI
root.mainloop()


# Depveloper : Rahul Dhar
