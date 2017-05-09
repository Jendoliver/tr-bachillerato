import bge
import puntuacio
import temps_ini 
import temps_fin
temps = timefin - timeini
cont = GameLogic.getCurrentController()
act = cont.actuators["nota"]		
def puntuaciófinal(a, b): 
	return (a + b) / 2

if fails = 0:
	a = 10
elif fails > 0 <= 5:
	a = 9
elif fails > 5 <= 10:
	a = 8
elif fails > 10 <= 15:
	a = 7
elif fails > 15 <= 20:
	a = 6
elif fails > 20 <= 25:
	a = 5
elif fails > 25 <= 30:
	a = 4
elif fails > 30 <= 35:
	a = 3
elif fails > 35 <= 40:
	a = 2
elif fails > 40 <= 45:
	a = 1
else:
	a = 0

if temps < 600:			#10 minuts
	b = 10
elif temps > 600 <= 900:	#15 minuts (+5 minuts sempre)
	b = 9
elif temps > 900 <= 1200:
	b = 8
elif temps > 1200 <= 1500:
	b = 7
elif temps > 1500 <= 1800:
	b = 6
elif temps > 1800 <= 2100:
	b = 5
elif temps > 2100 <= 2400:
	b = 4
elif temps > 2400 <= 2700:
	b = 3
elif temps > 2700 <= 3000:
	b = 2
elif temps > 3000 <= 3300:
	b = 1
else:
	b = 0

c = puntuaciófinal(a, b)

if c = 10	
	act.scene = "10"
elif c = 9
	act.scene = "9"
elif c = 8
	act.scene = "8"
elif c = 7
	act.scene = "7"
elif c = 6
	act.scene = "6"
elif c = 5
	act.scene = "5"
elif c = 4
	act.scene = "4"
elif c = 3
	act.scene = "3"
elif c = 2
	act.scene = "2"
elif c = 1
	act.scene = "1"
elif c = 0
	act.scene = "0"



