import json
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#from twitter_streaming import StdOutListener
from Tkinter import *

#Variables that contains the user credentials to access Twitter API 
access_token = '2874054435-t8ARu4lPounEZ75lJGLJygdSRrNdlMtRctySSTZ'
access_token_secret = 'lxl0sw2fRJuZns9RuEpYMnrwe1SiEoILwHtmh7JJioANx'
consumer_key = 'MVps6OFMNCkYfMnA2W7TVCmLs'
consumer_secret = 'Js2qWnSvNbLq0wRiQCP4ZBeRd1lpQr6A5tvS7JvPxHYzvdGXWu'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	#search = 'the'
	def __init__(self):
		self.information = ""
		self.n = 0
		self.m = 1
	def on_data(self, data):
		if self.n < self.m:
			json_load = json.loads(data)
			texts = json_load['text']
			coded = texts.encode('utf-8')
			s = str(coded)
			print(s)
			self.information += s
			f = open('mydata.txt', 'a')
			f.write(s)
			f.write('\n')
			f.close()
			self.n += 1
			return s
		else:
			return None
		
	def on_error(self, status):
		print(status)


class MyGUI:


	def __init__(self):
		self.streams = []
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		#print("Clicked the button4")
		self.myauth = StdOutListener()
		self.stream = Stream(auth, self.myauth)
		
		
		
		self.root = Tk()
		# modify
		self.root.title("Basic Twitter Data Mining")
		self.root.pack_propagate(0)
		self.root["height"] = 200;
		self.root["width"] = 400;
		

		# label
		self.myLabel = Label(self.root, text="Enter a search term.")
		self.myLabel.pack(side=TOP)
		# myLabel2.pack(side=BOTTOM)

		# frame user define
		self.frame1 = Frame(self.root)
		self.frame1.pack(side=TOP)

		
		# Buttons
		# button2
		self.button2 = Button(self.frame1, padx=10, pady=10, bd=2, text="Stop", fg="black")
		self.button2.pack(side=RIGHT)
		# button1
		self.button1 = Button(self.frame1, padx=10, pady=10, bd=2, text="Search", fg="black", command = self.clickSearch)
		#self.button1.bind("<Button-1>", self.onClick)
		self.button1.pack(side=RIGHT)

		
		# entry box
		self.entry1 = Entry(self.frame1, bd =5)
		self.entry1.pack(side = LEFT)
		#another label to edit
		# frame user define
		self.frame2 = Frame(self.root)
		self.frame2.pack(side=TOP)
		
		
		
		# Buttons
		# button2
		self.button3 = Button(self.frame2, padx=10, pady=10, bd=2, text="Clear", fg="black", command = self.cleartext)
		self.button3.pack(side=RIGHT)


		
		# entry box
		self.display1 = Text(self.frame2, width=40, height=10, bd =5)
		self.display1.pack(side = LEFT)

		# Menus
		# menu user define
		self.menubar = Menu(self.root)
		

		# menu1
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="About", command=self.test)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.root.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.root.config(menu=self.menubar)
		# menu2
		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="How does this work", command=self.help)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
		self.root.config(menu=self.menubar)

		# run program
		mainloop()
		
	def test(self):
		tmpy = "nothing"
		self.display1.insert("1.0", tmpy)
		#self.replaceL.configure(text='tmpy')
		print("nope!")

	def program():
		execfile("twitter_streaming.py")

	def code1():
		print("Open Basic GUI.py In IDLE To Change This!")

	def help():
		print("I'm helping.")
	def cleartext(self):
		self.display1.delete('1.0', 'end')
	def clickSearch(self):
		for stream in self.streams:
			stream.disconnect()
		self.display1.delete('1.0', 'end')
		#l = StdOutListener()
		print("Clicked the button5")
		#print("Clicked the button6")
		#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
		self.streams.append(self.stream)
		self.stream.filter(track=[self.entry1.get()], async=True)
		timeswaited = 0
		while self.myauth.information == "":
			if timeswaited > 10:
				print("took too long, returning to normal runtime.")
				break
			time.sleep(3)
			print("waiting for data...")
			timeswaited += 1
		#print("Clicked the button1")
		#print(self.myauth.information)
		#print("Clicked the button2")
		temp = self.myauth.information
		self.display1.insert('1.0', temp)
		self.myauth.information = ""
		#print("Clicked the button")
		#self.stream.disconnect()
		
		

if __name__ == "__main__":
	myGUI = MyGUI()
