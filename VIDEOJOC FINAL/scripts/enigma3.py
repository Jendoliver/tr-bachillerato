from bge import logic as GL
import puntuacio
from correctes import correctes as a
action = own.actuators['porta3']
cont = GL.getCurrentController()
sensor = cont.sensors['Mouse3']


if sensor.positive and a = 0:
       seleccionat = sensor.hitObject
       if seleccionat.name == 'Solució_3-1a':
		a =+ 1
       elif seleccionat.name == 'Solució_3-2b':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_3-3c':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_3-4':
		puntuacio.fails = puntuacio.fails + 1

if sensor.positive and a == 1:
	seleccionat = sensor.hitObject
	if seleccionat.name == 'Solució_3-1a':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_3-2b':
		a =+ 1
	elif seleccionat.name == 'Solució_3-3c':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_2-4':
		puntuacio.fails = puntuacio.fails + 1
		a = 0

if sensor.positive and a == 2:
	seleccionat = sensor.hitObject
	if seleccionat.name == 'Solució_3-1a':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_3-2b':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_3-3c':
		action.action = 'porta3'
		cont.activate(action)
	elif seleccionat.name == 'Solució_2-4':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
