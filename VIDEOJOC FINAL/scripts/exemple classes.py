from time import time

class contador():
	def __init__(self):				#defineix la pr�pia exist�ncia en funci� de "self"
		self.start_time = time.time()			#assigna time del m�dul time.py a "self.start_time", com una propietat
		self.stop_time = False				#nega l'exist�ncia de self.stop_time (elimina residus)
		def stop(self):					#defineix stop en funci� de self
			self.stop_time = time.time()			#assigna time del m�dul time.py a "self.stop_time"
			return self.stop_time - self.start_time		#torna a l'objecte executor la resta de t-t0
