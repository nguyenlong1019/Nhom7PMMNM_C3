#creating popup menu in tkinter 
import tkinter 

class A: 
	#creates parent window 
	def __init__(self): 
			
		self.root = tkinter.Tk() 
		self.root.geometry('500x500') 

		self.frame1 = tkinter.Label(self.root, 
									width = 400, 
									height = 400, 
									bg = '#AAAAAA') 
		self.frame1.pack() 

	#create menu 
	def popup(self): 
		self.popup_menu = tkinter.Menu(self.root, 
									tearoff = 0) 
		
		self.popup_menu.add_command(label = "say hi", 
									command = lambda:self.hey("hi")) 
		
		self.popup_menu.add_command(label = "say hello", 
									command = lambda:self.hey("hello")) 
		self.popup_menu.add_separator() 
		self.popup_menu.add_command(label = "say bye", 
									command = lambda:self.hey("bye")) 

	#display menu on right click 
	def do_popup(self,event): 
		try: 
            # popup tại vị trí chuột
			self.popup_menu.tk_popup(event.x_root, 
									event.y_root) 
		finally: 
			self.popup_menu.grab_release() 

	def hey(self,s): 
		self.frame1.configure(text = s) 
		
	def run(self): 
		self.popup() 
		self.root.bind("<Button-3>",self.do_popup) 
		tkinter.mainloop() 

a = A() 
a.run() 
