from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout

import math
import datetime

class basla(RelativeLayout):

	def __init__(self,**kwargs):
		
		super(basla,self).__init__(**kwargs)
		
		self.sn = 0
		self.dk = 0
		self.sa = 0
		
		Clock.schedule_interval(self.saniye, 0.5)

		Window.size = (500,500)
		
		
		
		
	def saniye(self,sn):
		
		self.an = datetime.datetime.now()
		
		self.canvas.clear()
		 
		with self.canvas:
			
			
			Color(0.2,0.2,0.2)
			
			Line(points = [self.width/2,self.height/2,self.width/2 + math.sin(self.an.second * 6 * math.pi/180) * self.width/2.3,self.height/2 + math.cos(self.an.second * 6 * math.pi/180)*self.height/2.3], width = 2)
								
			Color(0.3,0.2,0.4)
				
			Line(points = [self.width/2,self.height/2,self.width/2 + math.sin(self.an.minute * 6 * math.pi/180)*self.width/2.75,self.height/2 + math.cos(self.an.minute * 6 * math.pi/180)*self.height/2.75],width = 2)
			
			Color(0.2,0.2,0.2)
			
			Line(points = [self.width/2,self.height/2,self.width/2 + math.sin((self.an.hour * 30 + self.an.minute/2) * math.pi/180)*self.width/3.5,self.height/2 + math.cos((self.an.hour * 30 + self.an.minute/2) * math.pi/180)*self.height/3.5],width = 2)
			
			
			if self.sn % 360 == 6:
				self.dk += 6
			
			if self.sn % 3600 == 6:
				self.sa += 6
				
			
		self.sn += 6
		
			
					
			

		
class yerlesim(RelativeLayout):
	
	pass
	
	
		

class saat(App):
	
	def build(self):
		
		self.basla = basla()
		

		
		self.yerlesim = yerlesim()
		
		self.yerlesim.add_widget(self.basla)

		
		return self.yerlesim

if __name__ == "__main__":
	

	saat().run()
